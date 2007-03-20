# -*- coding: utf-8 -*-
import string
from sampleData import *

class PropertyInfo :
    def __init__(self, propertyName, propertyType):
        self.propertyName = propertyName
        self.propertyType = propertyType
        # self.capPropertyName = capitalize1(propertyName)

        self.trTdString=''
        self.line=''

    def getTest(self):

        return '1111'

    def setLine(self, line):
        self.line = line


def setAttributesOfPropertyInfo1(doc, aMasterInfo):
    myAttributeList = doc.getElementsByTagName('property')

    for myAttribute in myAttributeList:
        propertyName   = myAttribute.getAttribute('name')
        propertyType   = myAttribute.getAttribute('type')
        line           = myAttribute.getAttribute('line')

        aPropertyInfo = PropertyInfo(propertyName, propertyType)
        aPropertyInfo.setLine(line)

        aMasterInfo.addPropertyInfoList(aPropertyInfo)


    setScreenObjectStatements(aMasterInfo)
    setButtons(aMasterInfo,doc)
    
    aMasterInfo.sampleDataMasterList = setSampleData(doc, aMasterInfo)

    return aMasterInfo

def setScreenObjectStatements(aMasterInfo):
    ml = aMasterInfo.getMaxLine()
    for i in range(1,ml+1):
        rs = aMasterInfo.getLine(i)
        ss = string.split(rs,',')
        j = len(ss)
        if j > 2:
            [n1, t1, n2, t2] = ss
            aMasterInfo.writeLineTr1(n1, t1, n2, t2)
        else:
            [n1, t1] = ss
            aMasterInfo.writeLineTr2(n1, t1, n2, t2)

def setButtons(aMasterInfo, doc):
    aButtonList = doc.getElementsByTagName('button')
    for b in aButtonList:
        s = b.getAttribute('name')
        aMasterInfo.getButtonsStatement(s)
    # 마지막 버튼 이면 템플릿이 다르다
