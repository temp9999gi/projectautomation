class ModelInfo:
	def __init__(self):	
		pass

	def genMethod(self):
	# print 'inXMI: [',inXMI,']'
		aaa = '''
def setXMI(self):
	self.xxx='1111'
	print 'test' 
self.setXMI=setXMI
'''
		exec aaa
		
		
		
aModelInfo = ModelInfo()
aModelInfo.genMethod()
aModelInfo.setXMI(aModelInfo)
print 'dir(aModelInfo): [',dir(aModelInfo),']'
print 'dir(ModelInfo): [',dir(ModelInfo),']'

print 'aModelInfo.xxx: [',aModelInfo.xxx,']'


