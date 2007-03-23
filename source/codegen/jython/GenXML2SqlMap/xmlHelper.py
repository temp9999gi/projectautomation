from java.io import FileInputStream
from javax.xml.parsers import DocumentBuilderFactory

factory = DocumentBuilderFactory.newInstance()
builder = factory.newDocumentBuilder()

class ClassInfoTemp:
	def __init__(self, className, packagePath):
		self.className = className
		self.packagePath = packagePath

class ColumnTemp:
	def __init__(self, name, type, pkYn):
		self.name = name
		self.type = type
		self.pkYn = pkYn

def getClassInfo(inXmlFile,inTagName):
    input = FileInputStream(inXmlFile)
    document = builder.parse(input)
    results = document.getElementsByTagName(inTagName)
    for ix in range(results.getLength()):
        className = results.item(ix).getAttribute('className')
        packagePath = results.item(ix).getAttribute('packagePath')
        aClassInfoTemp = ClassInfoTemp(className,packagePath)
    return aClassInfoTemp


def getProperty(inXmlFile,inTagName):
	input = FileInputStream(inXmlFile)
	document = builder.parse(input)
	results = document.getElementsByTagName(inTagName)
	out_array =[]
	for ix in range(results.getLength()):
		name = results.item(ix).getAttribute('name')
		type = results.item(ix).getAttribute('type')
		pkYn = results.item(ix).getAttribute('pkYn')
		aColumnTemp = ColumnTemp(name,type,pkYn)
		out_array.append(aColumnTemp)
	return out_array


if __name__ in ('__main__','main'):
    inXmlFile = './input/Account.xml'
    for p in getProperty(inXmlFile, 'property'):
        print '[' + p.pkYn + ']'
	
