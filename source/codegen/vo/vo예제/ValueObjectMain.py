#*- coding: utf-8 -*-   

#	private String   acctsCd ;  // 계정과목코드 
#	private String   acctsNm ;  // 계정명 

attribute_name = ['acctsCd', 'acctsNm', 'AcctsBalAmtDrCrFg']
searchListValue = {"class_name":"AcctsVO", "attribute_names":attribute_name}

from Cheetah.Template import Template
t = Template(file="ValueObject.tmpl", searchList=[searchListValue])

print t
