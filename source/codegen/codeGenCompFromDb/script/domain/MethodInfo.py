# -*- coding: utf-8 -*-
import string
from CommonUtil import *
aCommonUtil = CommonUtil()
# start
class MethodInfo:
	def __init__(self):
		self.classId=''
		self.methodId=''
		self.packageId='com.posco.mes.m00???'
	def setAttributes(self, table_Kor, table_Eng, crudGubun, process_Nm, processID):
		self.table_Kor, self.table_Eng , self.crudGubun, self.process_Nm, self.processID = \
			table_Kor, table_Eng, crudGubun, process_Nm, processID

		self.setAttributesByCrudGubun()
		self.capWordTableId = aCommonUtil.getCapWord(table_Eng)
		#self.setClassId(self.capWordTableId,'')

	def setMethod(self, aTableInfo, aMethodInfo, crudGubun, table_Eng, table_Cd, processID):
		#tableIdCapWord = aCommonUtil.getCapWord(table_Cd)
		capWord_table_Eng = aCommonUtil.getCapWord(table_Eng)
		tmpMethodId = crudGubun + capWord_table_Eng

		#R이 두개인 경우 처리
		if aTableInfo.getMethodDictByMethodId(tmpMethodId) is None:
			aMethodInfo.setClassId(capWord_table_Eng, '')
			aMethodInfo.setMethodId(tmpMethodId)
			aTableInfo.setMethodDictByMethodId(aMethodInfo.methodId, aMethodInfo)
		else:
			aMethodInfo.setClassId(capWord_table_Eng, '__' + processID + '_XXX')
			aMethodInfo.setMethodId(crudGubun + capWord_table_Eng + '__' + processID + '_XXX')

	def setTable(self, aTable):
		self.aTable = aTable

	def setSql(self, inSql):
		self.sqlStatement = inSql
		
	def setSql(self, inSql):
		self.sqlStatement = inSql

	def setClassId(self, classId, inProcessId):
		#self.setClassSuffix()
		rt = classId[0].upper() + classId[1:]
		self.classId= rt + inProcessId + self.getClassSuffix()
		
	def getClassSuffix(self):
		return self.classSuffix
	
	def setAttributesByCrudGubun(self):
		if self.crudGubun == 'find':
			self.classSuffix='Find'
			self.crud_Type='R'
		if self.crudGubun == 'add':
			self.classSuffix='Addition'
			self.crud_Type='C'
		if self.crudGubun == 'update':
			self.classSuffix='Update'
			self.crud_Type='U'
		if self.crudGubun == 'delete':
			self.classSuffix='Deletion'
			self.crud_Type='D'
		if self.crudGubun == 'save':
			self.classSuffix='Regist'
			self.crud_Type='S'

	def setMethodKor(self):
		self.methodKor = self.crudGubun + ' ' +self.aTable.table_Kor
		
	def setMethodId(self, methodId):
		self.methodId = methodId
		self.methodEng = methodId
		#Xml 세팅
		self.setFindParagraph()
		self.setUpdateParagraph()
		self.setDeleteParagraph()
		self.setAddParagraph()
		
	def setFindParagraph(self):
		if self.crudGubun == 'find':
			self.findParagraph = """
<activity name="%(classId)s" class="%(packageId)s.%(classId)s">
	<transition name="success" value="end"/>
</activity>
"""% \
          {'methodId' : self.methodId,
           'packageId' : self.packageId,
           'classId'   : self.classId}
		else:
			self.findParagraph=''

	def setUpdateParagraph(self):
		if self.crudGubun == 'update':
			self.updateParagraph = """
<activity name="%(classId)s" class="%(packageId)s.%(classId)s">
	<transition name="success" value="%(capWordTableId)sFind"/>
	<transition name="failure" value="HandleError"/>
</activity>
"""% \
          {'methodId' : self.methodId, 'packageId' : self.packageId,
           'classId'   : self.classId,
           'capWordTableId':self.capWordTableId}
		else:
			self.updateParagraph=''
			
	def setDeleteParagraph(self):
		if self.crudGubun == 'delete':
			self.deleteParagraph = """
<activity name="%(classId)s" class="%(packageId)s.%(classId)s">
	<transition name="success" value="%(capWordTableId)sFind"/>
	<transition name="failure" value="HandleError"/>
</activity>
"""% \
          {'methodId' : self.methodId, 'packageId' : self.packageId,
           'classId'   : self.classId,
           'capWordTableId':self.capWordTableId}
		else:
			self.deleteParagraph=''

	def setAddParagraph(self):
		if self.crudGubun == 'add' or self.crudGubun == 'save':
			self.addParagraph = """
<activity name="%(classId)s" class="%(packageId)s.%(classId)s">
	<transition name="success" value="%(capWordTableId)sFind"/>
	<transition name="failure" value="HandleError"/>
</activity>
"""% \
          {'methodId' : self.methodId, 'packageId' : self.packageId,
           'classId'   : self.classId,
           'capWordTableId':self.capWordTableId}
		else:
			self.addParagraph=''
			
			
