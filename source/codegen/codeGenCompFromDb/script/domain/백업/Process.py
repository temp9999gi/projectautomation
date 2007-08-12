# start

class Process:
	def __init__(self):
		pass
		
	def setAttributes(self, process_Nm, processID, biz_Comp_Nm, biz_Comp_Id, da_Query_ID, table_Kor, table_Eng, crud_Type):
		self.process_Nm, self.processID, self.biz_Comp_Nm, self.biz_Comp_Id, self.da_Query_ID, self.table_Kor, self.table_Eng, self.crud_Type = \
			process_Nm, processID, biz_Comp_Nm, biz_Comp_Id, da_Query_ID, table_Kor, table_Eng, crud_Type
	