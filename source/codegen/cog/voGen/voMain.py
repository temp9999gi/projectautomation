#*- coding: utf-8 -*-
import xml.dom.minidom
import sys
from subprocess import *
from posCogApp.voCommonUtil import *

class ClassInfo :
    def __init__(self):
        self.className = ''
        self.packagePath = ''
    def setAttributes(self,className,packagePath):
        self.className = className
        self.packagePath = packagePath


def parseXml(aClassInfo, classXmlFile):
    # xmlFile = classXmlFile
    doc = xml.dom.minidom.parse(classXmlFile)
    className	= doc.getElementsByTagName("classInfo")[0].getAttribute('className')
    packagePath	= doc.getElementsByTagName("classInfo")[0].getAttribute('packagePath')

    aClassInfo.setAttributes(className,packagePath)

    return aClassInfo

def Run():

    aClassInfo = ClassInfo()
    
    classXmlFile = './input/'+sys.argv[1]

    aClassInfo = parseXml(aClassInfo, classXmlFile)

    # templateName = VO_TEMPLATE
    fileName = OUT_DIR + aClassInfo.className + '.java'

    aTemplate = generateCode(aClassInfo, VO_TEMPLATE)

    writeFile(fileName, aTemplate)
   
    # call('python C:\_tools\Python24\Scripts\cog.py -r ./output/Account.java')

    print 'The End:'
    
if __name__ == "__main__":

    #if len(sys.argv) < 2:
    #    print "USAGE: python genMain.py Class.xml"
    #    sys.exit()

    Run()