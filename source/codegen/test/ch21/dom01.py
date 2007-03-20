# dom01.py 
from xml.dom.minidom import * 
 
dom1 = parse('sample01.xml')  # 파일 이름으로 DOM 트리 생성 
 
f = open('sample01.xml') 
dom2 = parse(f)     # 파일 객체로 DOM 트리 생성 
 
dom3 = parseString('<value><int>1</int></value>')  # 문자열에서 직접 DOM 트리 생성 
