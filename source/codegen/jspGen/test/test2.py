#-*- coding: utf-8 -*-

from xml.dom.minidom import * 


def getAttribute1(doc):
    myAttributeList = doc.getElementsByTagName('property')
    
    for myAttribute in myAttributeList:
        propertyName   = myAttribute.getAttribute('name')
        print propertyName
 



s = open('names2.xml').read()  # ��ü ���ڿ��� �о��. 
s = unicode(s, 'euc-kr').encode('utf-8')  # euc-kr ---> utf-8 ��ȯ 
dom = parseString(s)         # ���ڿ��� �̿��� �Ľ� 
 
result = dom.toxml()

getAttribute1(dom)

# doc = xml.dom.minidom.parse(result)



        


#print result.encode('euc-kr')  # �ٽ� euc-kr�� 
dom.unlink() 