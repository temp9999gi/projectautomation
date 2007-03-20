#*- coding: utf-8 -*-

import cog, handyxml
import re
from commonUtil import *

def writeProperty(test_class, header_file):
	for p in handyxml.xpath('Properties.xml', '//property'):
		#  private String username;
		outStr = '  private %(type)s %(name)s;\n' % \
		            {'type': p.type, 'name': p.name}
		cog.out(outStr, dedent=False, trimblanklines=False)

def writeProperty2(test_class, header_file):
    outStr =''
    #Property 선언부 작성
    for p in handyxml.xpath('Properties.xml', '//property'):
        outStr = declareProperty(p.type, p.name)
        cog.out(outStr, dedent=False, trimblanklines=False)
        
    #get/set Method 작성
    for p in handyxml.xpath('Properties.xml', '//property'):
        outMethod= getSetMethod(p.type, p.name)
        cog.out(outMethod, dedent=False, trimblanklines=False)

				
def declareProperty(type1, name):
    #  private String username;
    outStr = '  private %(type)s %(name)s;\n' % \
                        {'type': type1, 'name': name}
    return outStr                        


def getSetMethod(type1, name):
    capName = capitalize1(name)
    #public String getId() {
    #  return id;
    #}		
    outStr1 = """
  public %(type)s get%(capName)s() {
    return %(name)s;
  }""" % {'type': type1, 'name': name, 'capName': capName}

    #public void setUsername(String username) {
    #  this.username = username;
    #}  
    outStr2 = """
  public void set%(capName)s(String %(name)s) {
    this.%(name)s = %(name)s;
  }

""" % {'type': type1, 'name': name, 'capName': capName}

    outMethod = outStr1 + outStr2
    return outMethod
				
				
