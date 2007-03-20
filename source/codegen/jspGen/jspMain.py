# -*- coding: utf-8 -*-
from xml.dom.minidom import *
import sys
from commonUtil import *
from classDef import *

def parseXml(aMasterInfo, inXmlFile):
    xmlFile = inXmlFile

    doc = getDomEncodeUtf8(xmlFile)
    
    fileName         = doc.getElementsByTagName("masterInfo")[0].getAttribute('fileName')
    crudFlag         = doc.getElementsByTagName("masterInfo")[0].getAttribute('crudFlag')    
    title            = doc.getElementsByTagName("masterInfo")[0].getAttribute('title')
    tableTitle       = doc.getElementsByTagName("masterInfo")[0].getAttribute('tableTitle')    

    aMasterInfo = MasterInfo()
    aMasterInfo.setAttributes(fileName,title,tableTitle,crudFlag)

    aMasterInfo.setAttributesOfPropertyInfo(doc,aMasterInfo)

    return aMasterInfo

def Run():

    aMasterInfo = MasterInfo()

    inXmlFile = './input/'+sys.argv[1]

    aMasterInfo = parseXml(aMasterInfo, inXmlFile)


    #templateName = JSP_TEMPLATE
    #fileName = JSP_OUT_DIR + aMasterInfo.fileName + '.jsp'
    #aTemplate = generateCode(aMasterInfo, templateName)
    #writeFile(fileName, aTemplate)


    templateName = JSP_MAIN_LIST_TEMPLATE 
    fileName = JSP_OUT_DIR + aMasterInfo.fileName + 'MainList.jsp'
    aTemplate = generateCode(aMasterInfo, templateName)
    writeFile(fileName, aTemplate)


    print 'The End:'

if __name__ == "__main__":

    #if len(sys.argv) < 2:
    #    print "USAGE: python genMain.py Class.xml"
    #    sys.exit()

    Run()