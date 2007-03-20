# -*- coding: utf-8 -*-
#
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
# ActiveX Data Objects (ADO)를 사용한다.

from SuperDao import SuperDao

class CrudMatrixDao(SuperDao):
	def __init__(self):
		SuperDao.__init__(self)

	#---------------------------------------------------------------------------
	def selectCrudAccessValueAction(self):
		self.setRecordset()
		rs = self.selectCrudAccessValue()
		return self.getTuple(rs)
		
	def selectCrudAccessValue(self):
		sql = """
		SELECT crudAccessValue.crudGubun, crudAccessValue.accessValue
		FROM crudAccessValue;
		"""
		return self.executeQuery(sql)

	#---------------------------------------------------------------------------
	
	def insertCrudMatrixAction(self, voList):
		self.setRecordset()
		self.setRecordsetForMuliRowInsert()
		self.deleteCrudMatrix()
		self.insertCrudMatrix(voList)
		
		self.setRecordset() #새로 Dispatch한다. 얘를 넣으니싼 에러가 안나네,,,,
		self.deleteCrudMatrixOriginal()
		self.insertCrudMatrixOriginal()
		
		#공통 유스케이스 :insert CommonUsecase
		self.deleteCommonUsecase()
		self.insertCommonUsecase()
		inWhere="""commonYn='Y'"""
		self.deleteCrudMatrixWhere(inWhere)
		
		#참조 유스케이스 :insert ReadOnlyUseCase
		self.deleteReadOnlyUseCase()
		self.insertReadOnlyUseCase()
		self.deleteReadOnlyUseCaseOfCrudMatrix()

	def deleteCrudMatrix(self):
		sql = """
		DELETE FROM crudMatrix;
		"""
		return self.executeQuery(sql)

	def deleteCrudMatrixWhere(self,inWhere):
		sql = """
		DELETE FROM crudMatrix where %(inWhere)s;
		""" \
		% {'inWhere': inWhere}

		return self.executeQuery(sql)

	def selectCrudMatrixForNullRs(self):
		sql="""
		select usecaseName, crudGubun, className, crudGubunOriginal, accessValue,
		    commonYn
		from crudMatrix where 1<>1
		"""
		return sql
	
	def insertCrudMatrix(self, voList):
		sql = self.selectCrudMatrixForNullRs()
		self.executeQuery(sql)
		
		for x in voList:
			self.rs.AddNew() #Add New Row
			
			# Add new Column Data
			(self.rs["usecaseName"] 	, \
			self.rs["crudGubun"] 		, \
			self.rs["className"] 		, \
			self.rs["crudGubunOriginal"], \
			self.rs["accessValue"],\
			self.rs["commonYn"]) = x
			
		self.rs.UpdateBatch()
		#self.rs.Close()

	def deleteCrudMatrixOriginal(self):
		sql = """
		DELETE FROM crudMatrixOriginal;
		"""
		return self.executeQuery(sql)

	def insertCrudMatrixOriginal(self):
		sql="""
		INSERT INTO crudMatrixOriginal
			( usecaseName, crudGubun, className,
			crudGubunOriginal, accessValue, commonYn )
		SELECT crudMatrix.usecaseName, crudMatrix.crudGubun, crudMatrix.className,
			crudMatrix.crudGubunOriginal, crudMatrix.accessValue, crudMatrix.commonYn
		FROM crudMatrix;
		"""
		self.executeQuery(sql)

	def deleteCommonUsecase(self): 
		sql = """
		DELETE FROM commonUsecase;
		"""
		return self.executeQuery(sql)
	def insertCommonUsecase(self):
		sql="""
		INSERT INTO commonUsecase ( usecaseName, crudGubun, className, crudGubunOriginal, accessValue, commonYn )
		SELECT crudMatrix.usecaseName, crudMatrix.crudGubun, crudMatrix.className, crudMatrix.crudGubunOriginal, crudMatrix.accessValue, crudMatrix.commonYn
		FROM crudMatrix
		WHERE (((crudMatrix.commonYn)="Y"));
		"""
		self.executeQuery(sql)
		
	#---------------------------------------------------------------------------
	def deleteReadOnlyUseCase(self):
		sql = """
		DELETE FROM readOnlyUseCase;
		"""
		return self.executeQuery(sql)
	def insertReadOnlyUseCase(self):
		sql="""
		INSERT INTO readOnlyUseCase ( usecaseName, crudGubun, className, crudGubunOriginal, accessValue, commonYn )
		SELECT crudMatrix.usecaseName, crudMatrix.crudGubun, crudMatrix.className, crudMatrix.crudGubunOriginal, crudMatrix.accessValue, crudMatrix.commonYn
		FROM
		(SELECT selReadOnlyCrudGubunCount.usecaseName,
			Sum(IIf(selReadOnlyCrudGubunCount.crudGubun="R",1,0)) AS rCount,
			Sum(IIf(selReadOnlyCrudGubunCount.crudGubun="R",0,1)) AS cudCount
		FROM selReadOnlyCrudGubunCount
		GROUP BY selReadOnlyCrudGubunCount.usecaseName
		HAVING (((Sum(IIf([selReadOnlyCrudGubunCount].[crudGubun]="R",0,1)))=0))
		) selReadOnlyAction
		INNER JOIN crudMatrix ON selReadOnlyAction.usecaseName=crudMatrix.usecaseName;
		"""
		self.executeQuery(sql)
		
	def deleteReadOnlyUseCaseOfCrudMatrix(self):
		sql = """
		DELETE FROM crudMatrix
		WHERE crudMatrix.usecaseName in
		(select usecaseName
		FROM readOnlyUseCase  );
		"""
		return self.executeQuery(sql)

	#===========================================================================
	def selectAllTbNameKorAndNull(self):
		sql = """
		SELECT tbNameKorAndNull.elementWordEng,
		  tbNameKorAndNull.nameKorAndNull,
		  tbNameKorAndNull.columnEng, tbNameKorAndNull.seq,
		  tbNameKorAndNull.tableEng
	    FROM tbNameKorAndNull;
				"""
		return sql
	
	
	
	
if __name__ == '__main__':
	aCrudMatrixDao = CrudMatrixDao()

# 	voList=[]
# 	for tb  in tl:
# 		for cl  in tb.columnList:
# 			xx=(cl.checkColumn, cl.columnEng, tb.tableEng)
# 			voList.append(xx)

	voList=[]
	usecaseName='1'; crudGubun='1'; className='1'; crudGubunOriginal='1'; accessValue='1'
	xx=(usecaseName, crudGubun, className, crudGubunOriginal, accessValue)
	voList.append(xx)
	usecaseName='2'; crudGubun='1'; className='1'; crudGubunOriginal='1'; accessValue='1'	
	xx=(usecaseName, crudGubun, className, crudGubunOriginal, accessValue)
	voList.append(xx)
	
	
	rs=aCrudMatrixDao.insertCrudMatrixAction(voList)

	#print rs
