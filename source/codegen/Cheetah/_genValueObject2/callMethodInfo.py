#*- coding: utf-8 -*-

from commonUtil import *
from Constants import *

class CallMethodInfo :
	def __init__(self, sqlId,resultClass,parameterClass,sqlText, crud):
		self.whereArgList = []
		self.sqlId = sqlId
		self.resultClass = resultClass
		self.parameterClass = parameterClass
		self.sqlText = sqlText
		self.setWhereArg(sqlText)
		self.crud = crud

	def appendMethodBody(self,aSqlMaster):
    #---------------------------------------------------------------------------
	# select Method의 파라미터 세팅 문장을 추가적으로  write
	# 예)
    #    Account account = new Account();
    #    account.setUsername(username);
    #    account.setPassword(password);
    #---------------------------------------------------------------------------

		className = aSqlMaster.className
		lowerClassName = aSqlMaster.lowerClassName

		appendStatement = '%(className)s %(lowerClassName)s = new %(className)s();' % \
		      {'className': className, 'lowerClassName': lowerClassName}

		if self.crud == 'select' and (len(self.whereArgList) > 1) :
			for whereArg in self.whereArgList:
				cap1WhereArg = capitalize1(whereArg)

				#account.setUsername(username);
				ss = SPC4 + '%(lowerClassName)s.set%(cap1WhereArg)s(%(whereArg)s);' % \
				      {'lowerClassName': lowerClassName, 'cap1WhereArg': cap1WhereArg, \
				       'whereArg': whereArg}

				appendStatement = appendStatement + '\n' + ss

			appendStatement = appendStatement + '\n' + SPC4 + self.methodBody
			self.methodBody = appendStatement

	def setWhereArg(self, sqlText):
		self.whereArgList = getWhereInArg(sqlText)

	def setMethodBody(self, methodBody):
		self.methodBody = methodBody


	def getMethodBody(self, aSqlMaster, aCallMethodInfo, crud):
		aReturnString = self.getCallMethodReturnString(aSqlMaster,crud)
		aMethodName   = self.getCallMethodMethodName(crud)
		inputArgument = self.getCallMethodInputArgument(aSqlMaster, aCallMethodInfo)
		
		#update("insertAccount", account);
		methodBody = '%(aReturnString)s%(aMethodName)s("%(sqlId)s", %(inputArgument)s);' % \
	                      {'aReturnString' : aReturnString,
	                       'aMethodName'   : aMethodName,
	                       'sqlId'         : aCallMethodInfo.sqlId,
	                       'inputArgument' : inputArgument}
	
		return methodBody

	def getCallMethodReturnString(self, aSqlMaster,crud):
		returnStr = 'return'
		aReturnString = ''
		if crud == 'select':
		    # return (Account) queryForObject("getAccountByUsername", username);
		    aReturnString = '%(aReturnString)s (%(className)s) ' % \
		    		          {'aReturnString': returnStr, 'className': aSqlMaster.className}
		elif crud == 'insert':
		    aReturnString = ''
		elif crud == 'update':
		    #                  update("insertAccount", account);
		    aReturnString = ''
		else:
			aReturnString = ''
		return aReturnString

	def getCallMethodMethodName(self, crud):
		aMethod=''
		if crud == 'select':
			aMethod = 'queryForObject'
		elif crud == 'insert' or crud == 'update':
			aMethod = 'update'
		elif crud == 'delete':
			aMethod = 'delete'
			
		return aMethod

	def getCallMethodInputArgument(self, aSqlMaster, aCallMethodInfo):
		#예)
		#  return (Account) queryForObject("getAccountByUsernameAndPassword", account);
		#  return (Account) queryForObject("getAccountByUsername", username);
		#위 문장 중 "account", "username" 파라미터를 리턴한다.
		#XML파일에서 parameterClass="string"와 같은 형태로 기재해야 한다.
		# -parameterClass="java.lang.String" <== 이런 형태가 아님
		# definition 파일에서 위를 세팅해주는 방법도 있을 것임
		
		inputArgument=''
		if aCallMethodInfo.parameterClass == 'string':
			s=''
			for x in aCallMethodInfo.whereArgList:
				s = s + x + ', '
			inputArgument = s[:-2] 
		else:
			inputArgument= aCallMethodInfo.parameterClass
			
		return inputArgument


