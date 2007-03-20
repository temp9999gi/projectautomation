# xslt03.py 
from Ft.Xml.Xslt.Processor import Processor 
 
proc = Processor() 
proc.appendStylesheetUri('sample04.xsl') 
result = proc.runUri('sample04.xml') 
print result 
