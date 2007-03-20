# -*- coding: utf-8 -*-
import re
import string

def lowerFirstChar(inText):
    return string.lower(inText[0]) + inText[1:]
    
def capitalize1(inText):
    return string.capitalize(inText)	

class ClassInfo :
    def __init__(self):    
        self.propertyInfoList = []
    def addPropertyInfoList(self, aPropertyInfo):
        self.propertyInfoList.append(aPropertyInfo)       
					
class PropertyInfo :
    def __init__(self, propertyName, propertyType):
        self.propertyName = propertyName
        self.propertyType = propertyType
        self.capPropertyName = capitalize1(propertyName)					
