# -*- coding: utf-8 -*-

class SampleData :
    def __init__(self):
        self.propertyName = ''
        self.sampleData = ''

    def setAttributes(self,propertyName, dataValue):
        self.propertyName = propertyName
        self.dataValue = dataValue

def setSampleData(doc, aMasterInfo):
    import handyxml
    sampleDataMasterList = []        
    for s in handyxml.xpath(doc, './/listSample'):
        sampleDataList=[]
        for sd in s.data:
            aSampleData = SampleData()
            aSampleData.setAttributes(sd.propertyName, sd.dataValue)
            sampleDataList.append(aSampleData)
        sampleDataMasterList.append(sampleDataList)

    return sampleDataMasterList
        #aMasterInfo.sampleDataMasterList.append(sampleDataList)
