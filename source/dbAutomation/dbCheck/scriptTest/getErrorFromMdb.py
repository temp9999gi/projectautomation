# -*- coding: utf-8 -*-
# 얘는 말야......ddl문을 파싱하는 애야.
from  string import *
import re

#import csv

from classDef import *
from myDao import *

def parseColumInfo(aTable,columText):
    colReader = split(columText,'\n') #라인 단위로 짜른다.
    for curRecord in colReader:
        pattern = '\s*(\w*)\s+(.*),'
        matchObject = re.match(pattern, curRecord , re.I | re.UNICODE)
        try:
            no,columnKor,columnEng,type1,length,null,key,remark= \
                '','','','','','','',''

            columnEng= matchObject.group(1)
            type1= matchObject.group(2)

            if len(columnEng) > 0 :
                aColumn = Column(columnEng)
                aColumn.setAttributes(no,columnKor,type1,length,null,key,remark)
                aColumn.setType1(type1)
                #print type1,'-------type1'
                aTable.addColumnList(aColumn)
        except AttributeError:
            pass



def parseTableInfo(inFile):

    p = re.compile('.*?(create table.*?)tablespace.*?', re.I | re.S | re.UNICODE)

    s = open(inFile).read()
    u = unicode(s, 'euc-kr')    # 유니코드로 변환

    utf8 = u.encode('utf-8')    # utf-8로 변환

    findedList = p.findall(utf8)    # 매치되는 애들을 추출하여 리스트로 리턴한다
    
    
    tableList = []

    for curTableInfo in findedList:
        #pattern = 'create table (.*)\s\((.*)\s\)'
        pattern = 'create table(.*)\s\((.*)\s\)'
        matchObject = re.match(pattern, curTableInfo , re.I | re.S | re.UNICODE)

        #rs = matchObject.group() #매치된 전체 그룹 문자열을 튜플 형식으로 리턴한다.
        tableEng = matchObject.group(1)
        columText = matchObject.group(2)
        #print tableEng, tableEng
        #print columText, columText
        
        tableEng=strip(tableEng)    #앞 뒤 공백 제거
        
        aTable = Table(tableEng)
        tableList.append(aTable)
                
        parseColumInfo(aTable, columText)

    return tableList

def Run():
    # tableList = parseTableInfo(inFile)
    aDao = MyDao()
    #aDao.deleteAll()
    # aDao.setVo(tableList)
    # aDao.insertTable()
    # aDao.insertColumn()

    print '------Error Type-----'    
    rs = aDao.selectErrorType()
    for tableEng, tableKor, columnKor, columnEng, type1 in rs:
        print tableEng, tableKor, columnKor, columnEng, type1



if __name__ == '__main__':
    Run()



