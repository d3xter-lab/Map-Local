#__*__ coding:utf8 __*__
from javax.swing import (JScrollPane, JTable, JPanel, JTextField, JLabel,
     JTabbedPane, JComboBox, BorderFactory, GroupLayout, LayoutStyle,
     JCheckBox, JButton, JTextArea, JMenuItem)
from java.awt import Font, event

class extender():

    def __init__(self):
        self.jLabel1 = JLabel()
        self.jCheckBox1 = JCheckBox()
        self.jScrollPane1 = JScrollPane()
        self.jTable1 = JTable()
        self.jTabbedPane1 = JTabbedPane()
        self.jPanel1 = JPanel()
        self.jButton1 = JButton("Add")
        self.jButton2 = JButton("Remove")
        self.jLabel2 = JLabel()
        self.jLabel3 = JLabel()
        self.jLabel4 = JLabel()
        self.jLabel5 = JLabel()
        self.jLabel6 = JLabel()
        self.jTextField1 = JTextField()
        self.jTextField2 = JTextField()
        self.jTextField3 = JTextField()
        
        method = ["http", "https"]
        self.jComboBox1 = JComboBox(method)
        
        self.jLabel7 = JLabel()
        self.jLabel8 = JLabel()
        self.jTextField4 = JTextField()
        self.jButton3 = JButton()
        self.jPanel2 = JPanel()
        self.jScrollPane3 = JScrollPane()
        self.jTextArea2 = JTextArea()

        self.jLabel1.setFont(Font("굴림", 1, 12))
        self.jLabel1.setText("Use local files to serve remote locations.")

        self.jCheckBox1.setText("Enable Map Local")
        
        self.jScrollPane1.setViewportView(self.jTable1)

        self.jLabel2.setText("Protocol:")

        self.jLabel3.setText("Host:")

        self.jLabel4.setText("Path:")

        self.jLabel5.setText("Query:")

        self.jLabel6.setText("Map From")

        self.jLabel7.setText("Map To")

        self.jLabel8.setText("Local Path:")

        self.jButton3.setText("Choose")
        
        jPanel1Layout = GroupLayout(self.jPanel1)
        self.jPanel1.setLayout(jPanel1Layout)
        
        from java.lang import Short
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addContainerGap()
                        .addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.TRAILING)
                            .addComponent(self.jLabel3)
                            .addComponent(self.jLabel2)
                            .addComponent(self.jLabel4)
                            .addComponent(self.jLabel5)
                            .addComponent(self.jLabel6))
                        .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                            .addComponent(self.jTextField1)
                            .addComponent(self.jTextField2)
                            .addComponent(self.jTextField3)
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addComponent(self.jComboBox1, GroupLayout.PREFERRED_SIZE, 86, GroupLayout.PREFERRED_SIZE)
                                .addGap(0, 0, Short.MAX_VALUE))))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addContainerGap()
                                .addComponent(self.jLabel7))
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addGap(30, 30, 30)
                                .addComponent(self.jLabel8)
                                .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(self.jTextField4, GroupLayout.DEFAULT_SIZE, 2000, Short.MAX_VALUE)
                                .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(self.jButton3, GroupLayout.PREFERRED_SIZE, 95, GroupLayout.PREFERRED_SIZE))
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addGap(0, 0, Short.MAX_VALUE)
                                .addComponent(self.jButton1, GroupLayout.PREFERRED_SIZE, 79, GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(self.jButton2, GroupLayout.PREFERRED_SIZE, 79, GroupLayout.PREFERRED_SIZE)))
                        .addGap(0, 18, Short.MAX_VALUE)))
                .addContainerGap())
        )
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGroup(GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(self.jLabel6)
                .addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self.jLabel2)
                    .addComponent(self.jComboBox1, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self.jLabel3)
                    .addComponent(self.jTextField1, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self.jLabel4)
                    .addComponent(self.jTextField2, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self.jLabel5)
                    .addComponent(self.jTextField3, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addComponent(self.jLabel7)
                .addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self.jLabel8)
                    .addComponent(self.jTextField4, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                    .addComponent(self.jButton3))
                .addGap(18, 18, 18)
                .addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self.jButton1)
                    .addComponent(self.jButton2))
                .addContainerGap(19, Short.MAX_VALUE))
        )

        self.jTabbedPane1.addTab("Edit Mapping", self.jPanel1)

        self.jTextArea2.setColumns(20)
        self.jTextArea2.setRows(5)
        self.jScrollPane3.setViewportView(self.jTextArea2)

        jPanel2Layout = GroupLayout(self.jPanel2)
        self.jPanel2.setLayout(jPanel2Layout)
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(self.jScrollPane3, GroupLayout.DEFAULT_SIZE, 729, Short.MAX_VALUE)
                .addContainerGap())
        )
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(self.jScrollPane3, GroupLayout.DEFAULT_SIZE, 255, Short.MAX_VALUE)
                .addContainerGap())
        )

        self.jTabbedPane1.addTab("Viewer", self.jPanel2)
        
        self.panel = JPanel()
        layout = GroupLayout(self.panel)
        self.panel.setLayout(layout)
        
        layout.setHorizontalGroup(
            layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                    .addComponent(self.jScrollPane1)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                            .addComponent(self.jCheckBox1)
                            .addComponent(self.jLabel1, GroupLayout.PREFERRED_SIZE, 285, GroupLayout.PREFERRED_SIZE))
                        .addGap(0, 0, Short.MAX_VALUE))
                    .addComponent(self.jTabbedPane1))
                .addContainerGap())
        )
        layout.setVerticalGroup(
            layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(self.jLabel1)
                .addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(self.jCheckBox1)
                .addGap(18, 18, 18)
                .addComponent(self.jScrollPane1, GroupLayout.PREFERRED_SIZE, 140, GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(self.jTabbedPane1)
                .addContainerGap())
        )

    