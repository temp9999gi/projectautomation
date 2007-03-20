#*- coding: utf-8 -*-   
# gen.py   
# usage:  python gen.py Class.xml

# generates JavaBean Class.java and database access ClassMgr.java files from XML

# Programming by Eric Rollins
#
# Copyright (c) 2002 Eric Rollins
# www.acm.org/~rollins

# gen comes with Absolutely No Warranty.
# This is free software, and you are welcome to
# redistribute it under certain conditions
# (for details see:GNU General Public License,
# http://www.gnu.org/copyleft/gpl.html)

# version 0.1
# 뭐라고

import sys
import string
import xml.dom.minidom
# uncomment the following line for validation using gen.dtd
from xml.parsers.xmlproc import xmlval

from encodings import cp949


TRUE = 1
FALSE = 0

if len(sys.argv) < 2:
  print "USAGE: python gen.py Class.xml"
  sys.exit()

# uncomment the following two lines for validation using gen.dtd
xv = xmlval.XMLValidator()
xv.parse_resource(sys.argv[1])

doc = xml.dom.minidom.parse(sys.argv[1])
className = doc.getElementsByTagName("name")[0].firstChild.data

#--------------------------------------------------------------------
# generate JavaBean file
#--------------------------------------------------------------------
cFile = open(className + '.java','w')

fieldList = doc.getElementsByTagName("field")

cFile.write('// ' + className + '.java' + '\n\n')
className = doc.getElementsByTagName("name")[0].firstChild.data
# public class Dwarf{
cFile.write('public class ' + className + '{\n')

# 변수선언부 작성
for field in fieldList:
  classAttributeName9 = field.getElementsByTagName("class-field")[0].firstChild.data
  classAtributeType = field.getElementsByTagName("type")[0].firstChild.data
  # private int dwarfId;
  # private String dwarfName;
  cFile.write('  private ' + classAtributeType + ' ' + classAttributeName9 + ';\n')

cFile.write('\n')

#   public Dwarf(
cFile.write('  public ' + className + '(\n')

first = TRUE
# 메소드 Input 파라미터 작성
# Start--------------------------------------------------#
for field in fieldList:
  classAttributeName9 = field.getElementsByTagName("class-field")[0].firstChild.data
  classAtributeType = field.getElementsByTagName("type")[0].firstChild.data

  if first:
    # int dwarfId
    cFile.write('    ' + classAtributeType + ' ' + classAttributeName9)
    first = FALSE
  else:
    # ,\n String dwarfName
    cFile.write(',\n' + '    ' + classAtributeType + ' ' + classAttributeName9)
# ")"
cFile.write(')\n')
# End  --------------------------------------------------#

# 생성자의 메소드 Body를 작성
# Start--------------------------------------------------#
cFile.write('  {\n')
for field in fieldList:
  classAttributeName9 = field.getElementsByTagName("class-field")[0].firstChild.data
  #    this.dwarfId = dwarfId;
  cFile.write('    this.' + classAttributeName9 + ' = ' + classAttributeName9 + ';\n')
cFile.write('  }\n')
# End  --------------------------------------------------#
cFile.write('\n')


# 초기화 생성자의 메소드 Body 작성
# Start--------------------------------------------------#
cFile.write('  public ' + className + '(){\n')
for field in fieldList:
  classAttributeName9 = field.getElementsByTagName("class-field")[0].firstChild.data
  classAtributeType = field.getElementsByTagName("type")[0].firstChild.data
  cFile.write('    this.' + classAttributeName9 + ' = ')

  if classAtributeType == 'String':
    cFile.write('null')
  else:
    cFile.write('0')

  cFile.write(';\n')

cFile.write('  }\n\n')
# End  --------------------------------------------------#

# get,set메소드 작성
# Start--------------------------------------------------#
for field in fieldList:
  classAttributeName9 = field.getElementsByTagName("class-field")[0].firstChild.data
  classAtributeType = field.getElementsByTagName("type")[0].firstChild.data
  upperFName = string.upper(classAttributeName9[0]) + classAttributeName9[1:]
  #  public int getDwarfId() { return dwarfId; }
  cFile.write('  public ' + classAtributeType + ' get' + upperFName + '()' +
    ' { return ' + classAttributeName9 + '; }\n')
  #  public void setDwarfId(int dwarfId) { this.dwarfId = dwarfId; }
  cFile.write('  public void set' + upperFName + '(' + classAtributeType + ' ' +
    classAttributeName9 + ') { this.' + classAttributeName9 + ' = ' + classAttributeName9 + '; }\n\n')

cFile.write('}\n')
# End  --------------------------------------------------#
cFile.close()
#--------------------------------------------------------------------
# End: generate JavaBean file
#--------------------------------------------------------------------


#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
# generate Mgr database access file
#--------------------------------------------------------------------
templateFile = open("Mgr.java.template","r")
template = templateFile.read(1000000)
templateFile.close()


primaryTable = doc.getElementsByTagName("primary-table")[0].firstChild.data
primaryTableBase = string.split(primaryTable)[0]

# $CLASS
template = string.replace(template,"$CLASS",className)

# SELECTSQL
selectSql = 'select '
first = TRUE

for field in fieldList:
  classAttributeName = field.getElementsByTagName("class-field")[0].firstChild.data
  tableColumnName = field.getElementsByTagName("database-field")[0].firstChild.data
  primaryKey = field.getElementsByTagName("primary-key")

  if len(primaryKey) > 0:
    pkColumnName = tableColumnName #d.dwarf_id
    pkColumnNameBase = string.split(pkColumnName,'.')[1] #dwarf_id
    pkfName = classAttributeName #dwarf_id #얘는 사용하지 않음

  if first:
    first = FALSE
  else:
    selectSql = selectSql + ','

  selectSql = selectSql + tableColumnName + ' as ' + string.lower(classAttributeName)

selectSql = selectSql + ' from ' + primaryTable #select d.dwarf_id as dwarfid,d.dwarf_name as dwarfname,d.born as born,d.home_id as homeid,m.mountain_name as homename,d.spouse_id as spouseid,s.dwarf_name as spousename from dwarf d

#join 문장 작성
joinList = doc.getElementsByTagName("join-table")
for table in joinList:
  tName = table.getElementsByTagName("join-name")[0].firstChild.data
  clause = table.getElementsByTagName("clause")[0].firstChild.data
  leftOuter = table.getElementsByTagName("left-outer")
  selectSql = selectSql + ' left join ' + tName + ' on ' + clause

template = string.replace(template,"$SELECTSQL",selectSql)
# End: SELECTSQL


# $SINGLESQL
singleSqlWhereCondition = ' where ' + pkColumnName + ' = ?' # pkColumnName
template = string.replace(template,"$SINGLESQL",singleSqlWhereCondition)

###################################
# $CONSTRUCTARGS
first = TRUE
constructArgs = ''

for field in fieldList:
  classAttributeName = field.getElementsByTagName("class-field")[0].firstChild.data
  classAtributeType = field.getElementsByTagName("type")[0].firstChild.data

  if first:
    first = FALSE
  else:
    constructArgs = constructArgs + ','

  if classAtributeType == 'String':
    constructArgs = constructArgs + 'res.getString("' + string.lower(classAttributeName) + '")'
  else:
    constructArgs = constructArgs + 'res.getInt("' + string.lower(classAttributeName) + '")'

template = string.replace(template,"$CONSTRUCTARGS",constructArgs)

#Insert메소드
# $ADDARGS
addArgs = ''
first = TRUE
for field in fieldList:
  classAttributeName = field.getElementsByTagName("class-field")[0].firstChild.data
  classAtributeType = field.getElementsByTagName("type")[0].firstChild.data
  insertCol = field.getElementsByTagName("insert-col")

  if len(insertCol) == 0:
    continue

  if first:
    first = FALSE
  else:
    addArgs = addArgs + ','

  addArgs = addArgs + classAtributeType + ' ' + classAttributeName
#public static int Add( << String dwarfName,int born,int homeId >> ) throws java.sql.SQLException
template = string.replace(template,"$ADDARGS",addArgs)

# $ADDPARAMS
addParams = ''

for field in fieldList:
  classAttributeName = field.getElementsByTagName("class-field")[0].firstChild.data
  classAtributeType = field.getElementsByTagName("type")[0].firstChild.data
  insertCol = field.getElementsByTagName("insert-col")

  if len(insertCol) == 0:
    continue

  if classAtributeType == 'String':
    #params.add(dwarfName);
    addParams = addParams + 'params.add(' + classAttributeName + ');\n'
  else:
    # if(born!= 0) params.add(new Integer(born)); else params.add(null);
    addParams = addParams + 'if(' + classAttributeName + '!= 0) params.add(new Integer('
    addParams = addParams + classAttributeName + ')); else params.add(null);\n'

template = string.replace(template,"$ADDPARAMS",addParams)

# $INSERTSQL
insertSql = 'insert into ' + primaryTableBase + ' ('
questions = '' #questions 이거 바꾸는 것이 좋을 것 같음
count = 0
first = TRUE

for field in fieldList:
  tableColumnName = field.getElementsByTagName("database-field")[0].firstChild.data
  insertCol = field.getElementsByTagName("insert-col")

  if len(insertCol) == 0:
    continue

  if first:
    first = FALSE
  else:
    insertSql = insertSql + ','
    questions = questions + ','

  insertSql = insertSql + string.split(tableColumnName,'.')[1]
  questions = questions + '?'

insertSql = insertSql + ') values ( ' + questions + ')'

template = string.replace(template,"$INSERTSQL",insertSql)

# $UPDATEARGS
updateArgs = ''
first = TRUE

for field in fieldList:
  classAttributeName = field.getElementsByTagName("class-field")[0].firstChild.data
  classAtributeType = field.getElementsByTagName("type")[0].firstChild.data
  updateCol = field.getElementsByTagName("update-col")

  if len(updateCol) == 0:
    continue 

  if first:
    first = FALSE
  else:
    updateArgs = updateArgs + ','

  updateArgs = updateArgs + classAtributeType + ' ' + classAttributeName

template = string.replace(template,"$UPDATEARGS",updateArgs)

# $UPDATEPARAMS
updateParams = ''

for field in fieldList:
  classAttributeName = field.getElementsByTagName("class-field")[0].firstChild.data
  classAtributeType = field.getElementsByTagName("type")[0].firstChild.data
  updateCol = field.getElementsByTagName("update-col")

  if len(updateCol) == 0:
    continue

  if classAtributeType == 'String':
    updateParams = updateParams + 'params.add(' + classAttributeName + ');\n'
  else:
    updateParams = updateParams + 'if(' + classAttributeName + '!= 0) params.add(new Integer('
    updateParams = updateParams + classAttributeName + ')); else params.add(null);\n'

template = string.replace(template,"$UPDATEPARAMS",updateParams)

# $UPDATESQL
updateSql = 'update ' + primaryTableBase + ' set '
count = 0
first = TRUE

for field in fieldList:
  tableColumnName = field.getElementsByTagName("database-field")[0].firstChild.data
  updateCol = field.getElementsByTagName("update-col")

  if len(updateCol) == 0:
    continue

  if first:
    first = FALSE
  else:
    updateSql = updateSql + ','

  updateSql = updateSql + string.split(tableColumnName,'.')[1] + ' = ? '

updateSql = updateSql + ' where ' + pkColumnNameBase + ' = ? '

template = string.replace(template,"$UPDATESQL",updateSql)

mgrFile = open(className + "Mgr.java","w")
mgrFile.write(template)
mgrFile.close()

