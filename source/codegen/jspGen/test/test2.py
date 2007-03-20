#-*- coding: utf-8 -*-

from xml.dom.minidom import * 


def getAttribute1(doc):
    myAttributeList = doc.getElementsByTagName('property')
    
    for myAttribute in myAttributeList:
        propertyName   = myAttribute.getAttribute('name')
        print propertyName
 



s = open('names2.xml').read()  # 전체 문자열을 읽어낸다. 
s = unicode(s, 'euc-kr').encode('utf-8')  # euc-kr ---> utf-8 변환 
dom = parseString(s)         # 문자열을 이용한 파싱 
 
result = dom.toxml()

getAttribute1(dom)

# doc = xml.dom.minidom.parse(result)



        


#print result.encode('euc-kr')  # 다시 euc-kr로 
dom.unlink() 
