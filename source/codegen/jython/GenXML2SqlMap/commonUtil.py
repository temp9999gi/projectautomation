import airspeed
import xmlHelper
from java.io import *
#from commonClassDef import *

def getTemplate(aTable,inCrud):
	xx = """
\t<%(inCrud)s id="%(inCrud)s${aTable.tableEng}" parameterClass="${aTable.lowNameIndex0}">
\t <![CDATA[
\t\t${aTable.%(inCrud)sSql}
\t ]]>
\t</%(inCrud)s>""" % {'inCrud': inCrud}
	t = airspeed.Template(xx)
	out = t.merge({"aTable": aTable})
	return out

def array2comma(aTable):
	s = ''
	for c in aTable.columnList:
		s = s + c.columnEng +', '
	out = s[0:len(s)-2]
	# print 'array2comma', out
	return out
def getUpdateSetArg(aTable):
	s = ''
	for c in aTable.columnList:
		s = s + c.columnEng +  ' = #' + c.columnEng + '#' + ', '
	out = s[0:len(s)-2]
	return out
def getArray2ValueArg(aTable):
    sValueArg = ''
    for c in aTable.columnList:
        sValueArg = sValueArg + '#' +c.columnEng +'#, '
    out = sValueArg[0:len(sValueArg)-2]
    # print 'array2comma', out
    return out

def writeFile(file_name, aTemplate):
	aFile = File(file_name)
	File(aFile.getParent()).mkdirs()
	outstream = FileOutputStream(aFile)
	outstream.write(aTemplate)
	outstream.close()
	print '(NG) file %s created' % file_name

