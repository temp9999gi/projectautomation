# dom02.py 
from xml.dom.pulldom import * 
 
dom1 = parse('sample01.xml')  # ���� �̸����� DOM Ʈ�� ���� 
 
f = open('sample01.xml') 
dom2 = parse(f)     # ���� ��ü�� DOM Ʈ�� ���� 
 
dom3 = parseString('<value><int>1</int></value>')  # ���ڿ����� ���� DOM Ʈ�� ���� 
