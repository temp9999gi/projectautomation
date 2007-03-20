# -*- coding: utf-8 -*-
import string
from commonUtil import *
from sampleData import *
from propertyInfo import *

class MasterInfo :
    def __init__(self):
        self.fileName = ''
        self.crudFlag = ''
        self.title = ''
        self.tableTitle = ''
        self.titleMgr =''
        self.titleScreen =''

        self.propertyInfoList = []
        self.sampleDataMasterList = []        
        self.sampleDataList = []

        self.screenObjectStatements = []
        self.buttonsStatements = []


    def addPropertyInfoList(self, aPropertyInfo):
        self.propertyInfoList.append(aPropertyInfo)
            

    def setAttributes(self,fileName, title, tableTitle, crudFlag):
        self.fileName = fileName
        self.crudFlag = crudFlag
        self.title = title
        self.tableTitle = tableTitle
        self.setTitle(title)

    def setTitle(self, title):
        (self.titleMgr,self.titleScreen) = string.split(title,'-')

    def setAttributesOfPropertyInfo(self, doc, aMasterInfo):
        return setAttributesOfPropertyInfo1(doc, aMasterInfo)
        
    def getLine(self, line):
        ss =''
        tt = ''
        for p in self.propertyInfoList:
            if p.line == str(line) :
                if len(ss) > 0:
                    tt = ','
                ss  = ss + tt + p.propertyName + ',' + p.propertyType
        return ss


    def getMaxLine(self):
        ss =[]
        for p in self.propertyInfoList:
            ss.append(p.line)
        newList = sorted(ss)
        i = newList[len(self.propertyInfoList)-1]
        return int(i)

    def writeLineTr1(self,n1, t1, n2, t2):
        templateName = TR_TD_TEMPLATE
        ss = {'propertyName1' : n1, 'propertyType1' : t1, 'propertyName2' : n2, 'propertyType2' : t2}
        aTemplate = generateCode(ss, templateName)
        trTdString = str(aTemplate)
        self.screenObjectStatements.append(trTdString)


    def writeLineTr2(self,n1, t1, n2, t2):
        templateName = TR_TD_1LINE_TEMPLATE
        ss = {'propertyName1' : n1, 'propertyType1' : t1}
        aTemplate = generateCode(ss, templateName)
        trTdString = str(aTemplate)
        self.screenObjectStatements.append(trTdString)


    def getButtonsStatement(self,buttonName):
        templateName = JSP_BUTTON_TEMPLATE
        ss = {'buttonName' : buttonName}
        aTemplate = generateCode(ss, templateName)
        s1 = str(aTemplate)
        self.buttonsStatements.append(s1)


