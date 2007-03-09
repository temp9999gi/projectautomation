class IPManager:
		ipmodules=[]

		def registerIPModule(self,m):
				if m not in self.ipmodules:
						for a in ["releaseName","copyright","license","credits","thanks"]:
								if not hasattr(m,a):
										print "IPManager: module",m,"doest not contain attribute",a
										assert(0)												
						self.ipmodules.append(m)

		def getRegisteredIPModules(self):
				return self.ipmodules
