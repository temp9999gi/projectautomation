# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
from SuperDao import SuperDao
class FinderAppDao(SuperDao):
	def __init__(self):
		SuperDao.__init__(self)
		self.setRecordset()
	#---------------------------------------------------------------------------
	def selectCrudMatrixAction(self):
		rs = self.selectCrudMatrix()
		return self.getTuple(rs)

	def selectCrudMatrix(self):
		sql="""
			SELECT crudMatrix.usecaseName, crudMatrix.className, q_SumAccessValue.sumOfAccessValue, [crudMatrix].[accessValue]/[q_SumAccessValue].[sumOfAccessValue] AS limitOfWeight, crudMatrix.crudGubun, crudMatrix.accessValue
			FROM crudMatrix INNER JOIN q_SumAccessValue ON crudMatrix.usecaseName = q_SumAccessValue.usecaseName
			WHERE ((([crudMatrix].[accessValue]/[q_SumAccessValue].[sumOfAccessValue])>=0.35))
			ORDER BY crudMatrix.usecaseName;
		"""
		return self.executeQuery(sql)


	#---------------------------------------------------------------------------
