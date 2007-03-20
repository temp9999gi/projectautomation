# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# CONSTANTS & GLOBALS

SPC2 = '  '
SPC4 = '    '

#file_name = './output/persistence/'
#
#	file_name = './output/persistence/' + aSqlMaster.className + 'SqlMapDao.java'	
#	templateFileName = "./input/template/SqlMapDao.tmpl"

INPUT_DIR = './input/'
OUT_DIR = './output/'

TEMPLATE_DIR = INPUT_DIR +'templates/'

VO_TEMPLATE = TEMPLATE_DIR + "ValueObject.tmpl"

# ----
DAO_TEMPLATE = TEMPLATE_DIR + "SqlMapDao.tmpl"
IDAO_TEMPLATE = TEMPLATE_DIR + "InterfaceDao.tmpl"

DAO_OUT_DIR       = OUT_DIR + 'persistence/sqlmapdao/'
IDAO_OUT_DIR      = OUT_DIR + 'persistence/iface/'

DAO_SUFFIX = 'SqlMapDao.java'
IDAO_SUFFIX = 'Dao.java'

SERVICE_TEMPLATE = TEMPLATE_DIR + "Service.tmpl"
SERVICE_OUT_DIR = OUT_DIR + 'service/'
SERVICE_SUFFIX  = 'Service.java'

DEFINITION_XML = INPUT_DIR +'definition.xml'

