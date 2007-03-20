# -*- coding: utf-8 -*-
from xml.dom.minidom import *

INPUT_DIR = './input/'

OUT_DIR = './output/'

TEMPLATE_DIR = INPUT_DIR +'templates/'

JSP_TEMPLATE = TEMPLATE_DIR + "Jsp.tmpl"

TR_TD_TEMPLATE = TEMPLATE_DIR + "JspTrTd.tmpl"

TR_TD_1LINE_TEMPLATE = TEMPLATE_DIR + "JspTrTd_1Line.tmpl"

JSP_BUTTON_TEMPLATE = TEMPLATE_DIR + "JspButton.tmpl"

JSP_MAIN_LIST_TEMPLATE = TEMPLATE_DIR + "JspMainList.tmpl"

JSP_OUT_DIR = OUT_DIR +'jsp/html/'


def generateCode(objectArray, templateFileName):

	from Cheetah.Template import Template
	aTemplate = Template(file = templateFileName, searchList = [objectArray])

	return aTemplate

def writeFile(fileName, aTemplate):
    new_file = file(fileName, 'w+')
    new_file.write('%s' % aTemplate)
    new_file.close()
    print '(NG) file %s created' % fileName

def getDomEncodeUtf8(xmlFile):
    s = open(xmlFile).read()  # 전체 문자열을 읽어낸다.
    s = unicode(s, 'euc-kr').encode('utf-8')  # euc-kr ---> utf-8 변환
    doc = parseString(s)         # 문자열을 이용한 파싱

    return doc
