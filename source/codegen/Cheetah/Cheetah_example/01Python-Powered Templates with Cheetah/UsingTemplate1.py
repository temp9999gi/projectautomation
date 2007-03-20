

testcaseValue = ['runquery', 'executequery', 'deletequery']
searchListValue = {"classundertest":"query_runner", "testcases":testcaseValue}

from Cheetah.Template import Template
t = Template(file="default_pyunit.tmpl", searchList=[searchListValue])

print t
