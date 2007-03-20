#*- coding: utf-8 -*-
import string

class MethodInfo :
	def __init__(self, aSqlMaster, methodName, callMethodList):
		self.aSqlMaster = aSqlMaster
		self.methodName = methodName
		self.callMethodList = callMethodList
		self.methodReturnType = ''
		self.setMethodArgument()
		self.getMethodReturnType()

	def getMethodReturnType(self):
		for x in self.callMethodList:
			if x.crud == 'select':
				self.methodReturnType = self.aSqlMaster.className
				self.returnStringInMethod = 'return '
			else :
				self.methodReturnType = 'void'
				self.returnStringInMethod = ''

	def setMethodArgument(self):
		for x in self.callMethodList:
			self.getMethodArgument(x.crud, x.whereArgList, x.parameterClass)

	def getMethodArgument(self, crud, inArgumentArray, parameterClass):
		#type1 = capitalize1(parameterClass) + ' '
		#예) public Account getAccount(Account username, Account password) {
		#      return (Account) queryForObject("getAccountByUsernameAndPassword", account);
		#Account-->String이 맞다.
		#Method body의 call Method의 파라미터 클래스
		#select 메소드의 경우는 파라미터를 String으로 처리한다.
		s = ''
		t = ''
		type1 = 'String '
		if crud == 'select':
			for x in inArgumentArray:
				s = s + type1 + x + ', ' #select 메소드의 경우는 파라미터를 String으로 처리한다.
				t = t +         x + ', '
		else :
			s = self.aSqlMaster.className + ' ' + self.aSqlMaster.lowerClassName + ', '
			t = self.aSqlMaster.lowerClassName + ', '

		self.methodArgument = s[:-2]
		self.callArgument = t[:-2]
		#print 'self.methodArgument',self.methodArgument

class SqlMaster :
	def __init__(self, namespace,alias,type1):
		self.namespace = namespace
		self.className = namespace
		self.setLowerClassNameIndex0(namespace)

		self.alias = alias
		self.type1 = type1
        methodInfoList = []

	def setLowerClassNameIndex0(self, className):
		self.lowerClassName = string.lower(className[0]) + className[1:]

	def setCallMethodInfoList(self, callMethodSqlInfoList):
		self.callMethodSqlInfoList = callMethodSqlInfoList

	def setPackagePath(self, packagePath):
		self.packagePath = packagePath

	def setMethodInfoList(self,methodInfoList):
		self.methodInfoList.append(methodInfoList)

