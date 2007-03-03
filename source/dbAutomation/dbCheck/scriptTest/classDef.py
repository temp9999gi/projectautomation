# -*- coding: utf-8 -*-

# usage:  python gen.py Class.xml
# generates JavaBean Class.java and database access ClassMgr.java files from XML
# Programming by KyungUk,Sung
#
# Copyright (c) 2002 KyungUk,Sung


class Table :
    def __init__(self,tableEng):
        self.tableEng = tableEng
        self.tableKor = ''
        self.ColumnList = []
        #print '[',tableKor,']'
        
    def setTableKor(self,tableKor):
        self.tableKor = tableKor
        
    def addColumnList(self,aColumn):
        self.ColumnList.append(aColumn)
        aColumn.setTableEng(self.tableEng)
        #print '['+self.tableKor + ']' #, aColumn

class Column :
    def __init__(self,columnEng):
        self.columnEng = columnEng
        self.tableEng = ''

    def setAttributes(self,no1,columnKor,type1,length,null1,key,remark):
        self.no1 = no1
        self.columnKor = columnKor
        self.type1 = type1
        self.length = length
        self.null1 = null1
        self.key = key
        self.remark = remark

    def setTableEng(self,tableEng):
        self.tableEng = tableEng

    def setType1(self,type1):
        self.type1 = type1

def utf8ToEucKr(inUtf8):
    return unicode(inUtf8, 'utf-8').encode('euc-kr')   # utf-8 --> euc-kr
