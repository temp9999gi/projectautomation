#*- coding: utf-8 -*-

import cog, handyxml
import re
from cogCommonUtil import *
from voCommonUtil import *

def writeProperty2(className, srcFile):
    xmlFile = PROPERTY_XML_FILE_DIR + className + '.xml'
        
    aClassInfo = ClassInfo()
    for p in handyxml.xpath(xmlFile, '//property'):
        (propertyName, propertyType) = (p.name ,p.type)
        aPropertyInfo = PropertyInfo(propertyName, propertyType)
        aClassInfo.addPropertyInfoList(aPropertyInfo)
    
    aTemplate = generateCode(aClassInfo, GET_SET_METHOD_TEMPLATE)
   
    cog.out(str(aTemplate), dedent=False, trimblanklines=False)
    