# -*- coding: utf-8 -*- 
#--------------------------------------------------------------------
# generate JavaBean file
#--------------------------------------------------------------------
import string

TRUE = 1
FALSE = 0

class JavaBeanWriter :

	def __init__(self, classInfo):
		self.classInfo  = classInfo		

	def writeJavaBeanfile(self):
		classInfo  = self.classInfo   
		className = classInfo.className  
		
		cFile = open('./output/' + className + '.java','w')

		cFile.write('// ' + className + '.java' + '\n\n')
		# public class Dwarf{
		cFile.write('public class ' + className + '{\n')

		# ��������� �ۼ�
		for x in classInfo.columnsArray:
		    # private int dwarfId;
			# private String dwarfName;
			cFile.write('  private ' + x.classAtributeType + ' ' + x.classAttributeName + ';\n')
		cFile.write('\n')
		#   public Dwarf(
		cFile.write('  public ' + className + '(\n')


		first = TRUE
		# �޼ҵ� Input �Ķ���� �ۼ�
		# Start--------------------------------------------------#
		for x in classInfo.columnsArray:
		  if first:
		    # int dwarfId
		    cFile.write('    ' + x.classAtributeType + ' ' + x.classAttributeName)
		    first = FALSE
		  else:
		    # ,\n String dwarfName
		    cFile.write(',\n' + '    ' + x.classAtributeType + ' ' + x.classAttributeName)
		# ")"
		cFile.write(')\n')
		# End  --------------------------------------------------#


		# �������� �޼ҵ� Body�� �ۼ�
		# Start--------------------------------------------------#
		cFile.write('  {\n')
		for x in classInfo.columnsArray:
		  #    this.dwarfId = dwarfId;
		  cFile.write('    this.' + x.classAttributeName + ' = ' + x.classAttributeName + ';\n')
		cFile.write('  }\n')
		# End  --------------------------------------------------#
		cFile.write('\n')


		# �ʱ�ȭ �������� �޼ҵ� Body �ۼ�
		# Start--------------------------------------------------#
		cFile.write('  public ' + className + '(){\n')
		for x in classInfo.columnsArray:
		  cFile.write('    this.' + x.classAttributeName + ' = ')
		  if x.classAtributeType == 'String':
		    cFile.write('null')
		  else:
		    cFile.write('0')

		  cFile.write(';\n')

		cFile.write('  }\n\n')
		# End  --------------------------------------------------#

		# get,set�޼ҵ� �ۼ�
		# Start--------------------------------------------------#
		for x in classInfo.columnsArray:
		  upperFName = string.upper(x.classAttributeName[0]) + x.classAttributeName[1:]
		  #  public int getDwarfId() { return dwarfId; }
		  cFile.write('  public ' + x.classAtributeType + ' get' + upperFName + '()' +
		    ' { return ' + x.classAttributeName + '; }\n')
		  #  public void setDwarfId(int dwarfId) { this.dwarfId = dwarfId; }
		  cFile.write('  public void set' + upperFName + '(' + x.classAtributeType + ' ' +
		    x.classAttributeName + ') { this.' + x.classAttributeName + ' = ' + x.classAttributeName + '; }\n\n')

		cFile.write('}\n')
		# End  --------------------------------------------------#

		#--------------------------------------------------------#
		# cFile.close()
		#--------------------------------------------------------#
		cFile.close()
		return 0
	#--------------------------------------------------------#
	# End: generate JavaBean file
	#--------------------------------------------------------#
#--------------------------------------------------------#
# End: class JavaBeanWriter :
#--------------------------------------------------------#
