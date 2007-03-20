INPUT_DIR = './input/'
OUT_DIR = './output/'

TEMPLATE_DIR = INPUT_DIR +'templates/'
VO_TEMPLATE = TEMPLATE_DIR + "VO.tmpl"

GET_SET_METHOD_TEMPLATE = TEMPLATE_DIR + "getSetMethod.tmpl"

PROPERTY_XML_FILE_DIR = INPUT_DIR


def generateCode(objectArray, templateFileName):

	from Cheetah.Template import Template
	aTemplate = Template(file = templateFileName, searchList = [objectArray])
	
	return aTemplate	

def writeFile(fileName, aTemplate):
	# print aTemplate
	new_file = file(fileName, 'w+')
	new_file.write('%s' % aTemplate)
	new_file.close()
	print '(NG) file %s created' % fileName