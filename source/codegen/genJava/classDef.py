# -*- coding: utf-8 -*-
# gen.py
# usage:  python gen.py Class.xml

# generates JavaBean Class.java and database access ClassMgr.java files from XML

# Programming by KyungUk,Sung
#
# Copyright (c) 2002 KyungUk,Sung

# gen comes with Absolutely No Warranty.
# This is free software, and you are welcome to
# redistribute it under certain conditions
# (for details see:GNU General Public License,
# http://www.gnu.org/copyleft/gpl.html)

# version 0.1

# class ClassInfo :
# class Column (ClassInfo) :
# class Master :
# class JoinTable :


import sys
import string

class ClassInfo :
	def __init__(self, className, classDesc, primaryTable, primaryTableBase):
		self.className = className
		self.classDesc = classDesc
		self.primaryTable = primaryTable
		self.primaryTableBase = primaryTableBase

		self.columnInClassInfo =[]
		self.members        = [] #순서를 가진다.
		self.columnsArray   = [] #순서를 가진다.
		self.joinTableArray = [] #순서를 가진다. 클래스 정보를 저장한다.

	def addColumnInClassInfo(self,classInfo) :
		self.columnInClassInfo.append(classInfo)

	def addJoinTableArray(self,_joinTable) :
		self.joinTableArray.append(_joinTable)

	#def setClassName(self,_className) :
	#	self.className = _className

	def addColumnsArray(self,_col) :
		self.columnsArray.append(_col)

	def __len__(self):
		return len(self.members)

	def __getitem__(self, key):
		for x in self.members :
			if x.has_key(key):
				return x[key]
		return None

	def __setitem__(self, key, value):
		item = {} #사전 key로 값을 꺼낸다. hash하고 비슷
		item[key] = value
		self.members.append(item);

	def __delitem__(self, key):
		index = 0
		for x in self.members:
			if x.has_key(key):
				del self.members[index]
			index += 1

	def __contains__(self, item):
		for x in self.members:
			if x.has_key(item):
				return 1
		return 0

	def __getslice__(self, start, stop, step=1):
		sub = []
		for x in range(start, stop, step):
			t = self.members[x]
			sub.append(t[x])
		return sub


class JoinTable :
	def __init__(self, joinName, joinClause, leftOuter):
		self.joinName = joinName
		self.joinClause = joinClause
		self.leftOuter = leftOuter


class Column :
	def __init__(self, classAttributeName, classAttributeDesc, classAtributeType, tableColumnName, className, \
		classDesc, primaryKey, insertCol, updateCol) :
		self.classAttributeName	=  classAttributeName
		self.classAttributeDesc =  classAttributeDesc
		self.classAtributeType  =  classAtributeType
		self.tableColumnName    =  tableColumnName
		self.primaryKey         =  primaryKey
		self.insertCol          =  insertCol
		self.updateCol          =  updateCol

