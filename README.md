# Map Local
## About
<b>Map Local</b> is Burp Suite's extender that maps URL and local files.
A main feature of the extension is the file mapping. For example the following :

* Set http://www.test.com/test.js -> C:\test\test_1.js

If like that, you can see test_1.js contents in this link's response.



## Installation
1.	Download Burp Suite Pro: http://portswigger.net/burp/download.html
2.	Download Jython standalone JAR: http://www.jython.org/downloads.html
3.	Burp Suite -> Extender -> Options -> Python Environment -> Select File -> Choose the Jython standalone JAR
4.  Download Map Local extender.zip -> Unzip
5.  Burp Suite -> Extender -> Add -> Extension type: Python -> Extension file: "map-local.py" -> Next
6.  Go to "Map Local" tab in Burp Suite and configure the extension for your needs



## Next

* Support ContextMenu (Now, no working)
* Support Viewer (Now, no working)
* Support Save and Load



## Contact
Please feel free to contact, if you miss any interesting file checks or discover any bugs. 