# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
SPACE2='  '
COLUMN_PAD_LEN=25
def array2comma(aTable):
	s = SPACE2+' '
	for c in aTable.fieldList:
		s = s + c.columnEng.ljust(COLUMN_PAD_LEN,' ') + '  /*'+c.columnKorName +'*/' +'\n' + SPACE2 +','
		
	out = s[0:len(s)-4]
	return out

"""
    SELECT T1.CHGR_ID             ,  /*변경자ID*/
    FROM ABA01TN T1
"""
def array2CommaForTbAlias(aTable):
	s = SPACE2+' '
	for c in aTable.fieldList:
		s = s + 'T1.'+c.columnEng.ljust(COLUMN_PAD_LEN,' ') + '  /*'+c.columnKorName +'*/' +'\n' + SPACE2 +','

	out = s[0:len(s)-4]
	return out
def getUpdateSetArg(aTable):
	s = SPACE2+' '
	for c in aTable.nonPkColumnList:
		s = s + c.columnEng.ljust(COLUMN_PAD_LEN,' ') +  ' = #' + c.javaName + '#' + '\n' + SPACE2 + ','
	out = s[0:len(s)-4]
	return out

def getArray2ValueArg(aTable):
    sValueArg = SPACE2+' '
    for c in aTable.fieldList:
        sValueArg = sValueArg + '#' + c.javaName +'#'+'\n' + SPACE2 +','
        
    out = sValueArg[0:len(sValueArg)-2]
    # print 'array2comma', out
    return out

