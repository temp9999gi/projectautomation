#*- coding: utf-8 -*-

from classDef import *

#	private String cdId;
#	private String cdNm;
#	private int currentPage;	

aColumn = []

aColumn.append(Column('cdId', 'String'))
aColumn.append(Column('cdNm', 'String'))
aColumn.append(Column('currentPage', 'int'))

aClassInfo = ClassInfo("CdVO",aColumn)

from Cheetah.Template import Template
t = Template(file="ValueObject.tmpl", searchList=[aClassInfo])

print t

file_name = './output/' + aClassInfo.className + '.java'

new_file = file(file_name, 'w+')
#new_file.write('%s' % self.template)
new_file.write('%s' % t)
new_file.close()
print '(NG) file %s created' % file_name
