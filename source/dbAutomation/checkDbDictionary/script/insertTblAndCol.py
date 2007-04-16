# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
from checkDbDictionary import *

def run2():
	inPath = sys.argv[0]
	CONS.setConstant(inPath)

	aReaderAppEnv = ReaderAppEnv.ReaderAppEnv()
	aReaderAppEnv.saveAppEnvInfo(CONS.INPUT_APP_ENV_XML)
	aWriterApp = WriterApp()
	dataSource = sys.argv[2]
	aWriterApp.insertTblAndColAction(aReaderAppEnv, dataSource)

	print "(MSG) Insert OK"


if __name__ == '__main__':
 	if len(sys.argv) < 2:
 		print "USAGE: WriterApp.py input.xls"
 		sys.exit()

	run2()