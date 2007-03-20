# -*- coding: utf-8 -*- 
#--------------------------------------------------------------------
# generate JavaBean file
#--------------------------------------------------------------------
import string

TRUE = 1
FALSE = 0

class MgrWriter :

	def __init__(self, classInfo):
		self.classInfo  = classInfo

	def writeMgrfile(self):
		classInfo  = self.classInfo
		className = classInfo.className
		primaryTableBase  = classInfo.primaryTableBase		
		primaryTable  = classInfo.primaryTable		

		templateFile = open("Mgr.java.template","r")
		template = templateFile.read(1000000)
		templateFile.close()

		# $CLASS
		template = string.replace(template,"$CLASS",className)
		
		# SELECTSQL
		selectSql = 'select '
		first = TRUE
		
		for x in classInfo.columnsArray:
		
		  if len(x.primaryKey) > 0:
		    pkColumnName = x.tableColumnName #d.dwarf_id
		    pkColumnNameBase = string.split(pkColumnName,'.')[1] #dwarf_id
		
		  if first:
		    first = FALSE
		  else:
		    selectSql = selectSql + ','
		
		  selectSql = selectSql + x.tableColumnName + ' as ' + string.lower(x.classAttributeName)
		
		#select d.dwarf_id as dwarfid,d.dwarf_name as dwarfname,d.born as born,d.home_id as homeid,m.mountain_name as homename,
		  #d.spouse_id as spouseid,s.dwarf_name as spousename from dwarf d
		selectSql = selectSql + ' from ' + primaryTable 

		for x in classInfo.joinTableArray:
		  selectSql = selectSql + ' left join ' + x.joinName + ' on ' + x.joinClause

		template = string.replace(template,"$SELECTSQL",selectSql)
		# End: SELECTSQL
		

		# $SINGLESQL
		singleSqlWhereCondition = ' where ' + pkColumnName + ' = ?' # pkColumnName
		template = string.replace(template,"$SINGLESQL",singleSqlWhereCondition)
		
		# $CONSTRUCTARGS
		first = TRUE
		constructArgs = ''
		for x in classInfo.columnsArray:
			if first:
				first = FALSE
			else:
				constructArgs = constructArgs + ','
		
			if x.classAtributeType == 'String':
				constructArgs = constructArgs + 'res.getString("' + string.lower(x.classAttributeName) + '")'
			else:
				constructArgs = constructArgs + 'res.getInt("' + string.lower(x.classAttributeName) + '")'
		
		template = string.replace(template,"$CONSTRUCTARGS",constructArgs)		
		
		#Insert메소드
		# $ADDARGS
		addArgs = ''
		first = TRUE
		for x in classInfo.columnsArray:
		  if len(x.insertCol) == 0:
		    continue
		
		  if first:
		    first = FALSE
		  else:
		    addArgs = addArgs + ','
		
		  addArgs = addArgs + x.classAtributeType + ' ' + x.classAttributeName
		#public static int Add( << String dwarfName,int born,int homeId >> ) throws java.sql.SQLException
		template = string.replace(template,"$ADDARGS",addArgs)		
		
		
		# $ADDPARAMS
		addParams = ''
		for x in classInfo.columnsArray:
		  #classAttributeName = field.getElementsByTagName("class-field")[0].firstChild.data
		  #classAtributeType = field.getElementsByTagName("type")[0].firstChild.data
		  #insertCol = field.getElementsByTagName("insert-col")
		
		  if len(x.insertCol) == 0:
		    continue
		
		  if x.classAtributeType == 'String':
		    #params.add(dwarfName);
		    addParams = addParams + 'params.add(' + x.classAttributeName + ');\n'
		  else:
		    # if(born!= 0) params.add(new Integer(born)); else params.add(null);
		    addParams = addParams + 'if(' + x.classAttributeName + '!= 0) params.add(new Integer('
		    addParams = addParams + x.classAttributeName + ')); else params.add(null);\n'
		
		template = string.replace(template,"$ADDPARAMS",addParams)
		
		
		# $INSERTSQL
		insertSql = 'insert into ' + primaryTableBase + ' ('
		questions = '' # '?' 이것을 의미
		count = 0
		first = TRUE		
		for x in classInfo.columnsArray:
		  #tableColumnName = field.getElementsByTagName("database-field")[0].firstChild.data
		  #insertCol = field.getElementsByTagName("insert-col")
		
		  if len(x.insertCol) == 0:
		    continue
		
		  if first:
		    first = FALSE
		  else:
		    insertSql = insertSql + ','
		    questions = questions + ','
		
		  insertSql = insertSql + string.split(x.tableColumnName,'.')[1]
		  questions = questions + '?'
		
		insertSql = insertSql + ') values ( ' + questions + ')'
		
		template = string.replace(template,"$INSERTSQL",insertSql)		


		# $UPDATEARGS
		updateArgs = ''
		first = TRUE		
		for x in classInfo.columnsArray:
		  #classAttributeName = field.getElementsByTagName("class-field")[0].firstChild.data
		  #classAtributeType = field.getElementsByTagName("type")[0].firstChild.data
		  #updateCol = field.getElementsByTagName("update-col")
		
		  if len(x.updateCol) == 0:
		    continue 
		
		  if first:
		    first = FALSE
		  else:
		    updateArgs = updateArgs + ','
		
		  updateArgs = updateArgs + x.classAtributeType + ' ' + x.classAttributeName
		
		template = string.replace(template,"$UPDATEARGS",updateArgs)


		# $UPDATEPARAMS
		updateParams = ''
		
		for x in classInfo.columnsArray:
		
		  if len(x.updateCol) == 0:
		    continue
		
		  if x.classAtributeType == 'String':
		    updateParams = updateParams + 'params.add(' + x.classAttributeName + ');\n'
		  else:
		    updateParams = updateParams + 'if(' + x.classAttributeName + '!= 0) params.add(new Integer('
		    updateParams = updateParams + x.classAttributeName + ')); else params.add(null);\n'
		
		template = string.replace(template,"$UPDATEPARAMS",updateParams)
				
				
		# $UPDATESQL
		updateSql = 'update ' + primaryTableBase + ' set '
		count = 0
		first = TRUE
		
		for x in classInfo.columnsArray:
		
		  if len(x.updateCol) == 0:
		    continue
		
		  if first:
		    first = FALSE
		  else:
		    updateSql = updateSql + ','
		
		  updateSql = updateSql + string.split(x.tableColumnName,'.')[1] + ' = ? '
		
		updateSql = updateSql + ' where ' + pkColumnNameBase + ' = ? '
		
		template = string.replace(template,"$UPDATESQL",updateSql)		


		mgrFile = open('./output/' + className + "Mgr.java","w")
		mgrFile.write(template)
		#--------------------------------------------------------#
		# mgrFile.close()
		#--------------------------------------------------------#
		mgrFile.close()
		return 0
	#--------------------------------------------------------#
	# End: generate file
	#--------------------------------------------------------#
#--------------------------------------------------------#
# End: class
#--------------------------------------------------------#
