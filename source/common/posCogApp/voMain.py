#*- coding: utf-8 -*-
import xml.dom.minidom
from subprocess import *
from voCommonUtil import *

class ClassInfo :
    def __init__(self):
        self.className = ''
        self.packagePath = ''
    def setAttributes(self,className,packagePath):
        self.className = className
        self.packagePath = packagePath


def parseXml(aClassInfo, classXmlFile):
    xmlFile = './input/' + classXmlFile
    doc = xml.dom.minidom.parse(xmlFile)
    className    = doc.getElementsByTagName("classInfo")[0].getAttribute('className')
    packagePath       = doc.getElementsByTagName("classInfo")[0].getAttribute('packagePath')

    aClassInfo.setAttributes(className,packagePath)

    return aClassInfo

def Run():

    aClassInfo = ClassInfo()
    
    classXmlFile = 'Account.xml'
    aClassInfo = parseXml(aClassInfo, classXmlFile)


    templateName = VO_TEMPLATE
    fileName = OUT_DIR + aClassInfo.className + '.java'

    aTemplate = generateCode(aClassInfo, templateName)

    writeFile(fileName, aTemplate)
   
    # call('python C:\_tools\Python24\Scripts\cog.py -r ./output/Account.java')

    print 'The End:'
    
if __name__ == "__main__":

    #if len(sys.argv) < 2:
    #    print "USAGE: python genMain.py Class.xml"
    #    sys.exit()

    Run()