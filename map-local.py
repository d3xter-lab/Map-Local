#__*__ coding:utf8 __*__
from burp import IBurpExtender, IHttpListener, IContextMenuFactory, ITab
from java.util import ArrayList
from java.awt import BorderLayout
from javax.swing import JMenuItem, table, JFileChooser
import sys, os
import threading
import urlparse
from extender import extender
from exceptions_fix import FixBurpExceptions

class BurpExtender(IBurpExtender, IHttpListener, IContextMenuFactory, ITab):
    def __init__(self):
        global frm
        frm = extender()
        frm.jButton1.addActionListener(self.addMapping)
        frm.jButton2.addActionListener(self.delMapping)
        frm.jButton3.addActionListener(self.selectFile)
        
        tableData = []
        tableColumns = ["#", "Location", "Local Path"]
        global tableModel
        global tableURL
        tableURL = {}
        
        tableModel = table.DefaultTableModel(tableData, tableColumns)
        frm.jTable1.setModel(tableModel)
        if (frm.jTable1.getColumnModel().getColumnCount() > 0):
            frm.jTable1.getColumnModel().getColumn(0).setMinWidth(40)
            frm.jTable1.getColumnModel().getColumn(0).setMaxWidth(40)
    
    def registerExtenderCallbacks(self, callbacks):
        sys.stdout = callbacks.getStdout()
        self.callbacks = callbacks
        
        self.helpers = callbacks.getHelpers()
        self.callbacks.setExtensionName("Map Local")
        self.callbacks.issueAlert("Map Local Loaded Successfully.")
        
        callbacks.registerContextMenuFactory(self)
        callbacks.addSuiteTab(self)
        callbacks.registerHttpListener(self)

        return
    
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if frm.jCheckBox1.isSelected():
            if (toolFlag == self.callbacks.TOOL_PROXY and not messageIsRequest):
                requestInfo = self.helpers.analyzeRequest(messageInfo); 
                dName = str(requestInfo.getUrl())
                parts = urlparse.urlparse(dName)
                hURL = parts.scheme + "://" + parts.hostname + parts.path
                try:
                    if tableURL[hURL] != None:
                        response = messageInfo.getResponse()
                        responseStr = self.callbacks.getHelpers().bytesToString(response)
                        responseParsed = self.helpers.analyzeResponse(response)
                        body = responseStr[responseParsed.getBodyOffset():]
                        headers = responseParsed.getHeaders()
                        
                        with open(tableURL[hURL], mode='rt') as f:
                            rtext = f.read()

                        httpResponse = self.callbacks.getHelpers().buildHttpMessage(headers, rtext)
                        messageInfo.setResponse(httpResponse)
                except:
                    pass  


    def getTabCaption(self):
        return "Map Local"
        
    def getUiComponent(self):
        return frm.panel
    
    def createMenuItems(self, invocation):
        self.context = invocation
        menuList = ArrayList()
        menuItem = JMenuItem("Send to Map Local", actionPerformed=self.createURLFromSelected)
        menuList.add(menuItem)
        return menuList
        
    def createURLFromSelected(self, event):
        t = threading.Thread(target=self.makeURLString)
        t.daemon = True
        t.start()
        
    def makeURLString(self):
        httpTraffic = self.context.getSelectedMessages()
        hostUrls = []
        for traffic in httpTraffic:
            try:
                url = str(traffic.getUrl())
                parts = urlparse.urlparse(url)
                hostUrls.append(parts.scheme + "://" + parts.hostname + parts.path)
            except UnicodeEncodeError:
                continue
        
        print("[*] Selected file name: " + hostUrls[0])
        
    def addDict(self):
        for i in range(0, int(frm.jTable1.getRowCount())):
            tableURL[str(frm.jTable1.getValueAt(i,1))] = str(frm.jTable1.getValueAt(i,2))
            
        print(tableURL)
        
    def addMapping(self, event):
        print("Add !!")
        protocol = frm.jComboBox1.selectedItem
        host = frm.jTextField1.text
        path = frm.jTextField2.text
        query = frm.jTextField3.text
        location = protocol + "://" + host + "/" + path
        localpath = frm.jTextField4.text
        
        tableModel.addRow([frm.jTable1.getRowCount() + 1, location, localpath])
        self.addDict()
        
    def delMapping(self, event):
        print("Remove !!")
        tableURL.pop(str(frm.jTable1.getValueAt(int(frm.jTable1.getSelectedRow()),1)))
        tableModel.removeRow(frm.jTable1.getSelectedRow())
        print(tableURL)
        
        
    def selectFile(self, event):
        print("Choose !!")
        chooseFile = JFileChooser()
        ret = chooseFile.showDialog(frm.panel, "Choose file")
        if ret == JFileChooser.APPROVE_OPTION:
            file = chooseFile.getSelectedFile()
            frm.jTextField4.setText(file.getCanonicalPath())
        
        
        
print("# Map Local")
print("# by d3xter, 2020.02")

try:
    FixBurpExceptions()
except:
    pass