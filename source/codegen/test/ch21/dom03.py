# dom03.py 
from xml.dom.ext.reader.Sax2 import * 
 
f = open('sample01.xml') 
reader = Reader()  # Reader ��ü�� �����Ѵ�. 
dom1 = reader.fromStream(f)  # ���� ��ü�� ���� �о� DOM Ʈ���� �����Ѵ�. 
 
dom2 = reader.fromUri('sample01.xml')  # URI���� DOM Ʈ���� �����Ѵ�. 
 
dom3 = reader.fromString('<value><int>1</int></value>')  # ���ڿ����� DOM Ʈ���� �����Ѵ�. 
