# TODO
#	Optimize CommandHistory

import string
from smw import log
from smw.metamodel import MetaMM
from smw.metamodel import OCLforPython
from smw.metamodel import TransactionManager
from smw import io
import time
from smw import SignalHandling

logger=log.getLogger("Project")


class Profile:
		def __init__(self,name,metamodel,editorModules,blurb=""):
				self.name=name
				self.blurb=blurb
				if type(metamodel)==type(""):
						self.metamodel=__import__(metamodel,globals(),locals(),
																			[string.split(metamodel,'.')[-1]]
																			)
				else:
						self.metamodel=metamodel
				self.editorModules=editorModules

		def description(self):
				s=""				
				if self.blurb:
						s=s+self.blurb+"\n"
				s=s+"This profile is based on the "+self.metamodel.__name__+ \
				" metamodel module.\n\n"
				if self.editorModules:
						s=s+"It uses the following program modules:\n"
				for e in self.editorModules:
						s=s+"	 "+e+"\n"
				return s
						

theProject=None

class Project:

		def __init__(self,name="noname",profile=None,rootElement=None):
			
				self.fileName=None
			 
				self.profile=profile
				self.dragObject=None
				self.dirty=0

				SignalHandling.registerSignalEmitter("savedModel")
				
				try:				
						from smw.modeler.Editor import EditorSet
						from smw.Configuration import Configuration
						self.editorSet=EditorSet()
						self.options=Configuration()
				except:
						self.editorSet=None
						self.options=None
						
				self.history=CommandHistory(self.editorSet) 
				if TransactionManager.theTM!=None:
						raise "It is only possible to instanciate one Project at a time"
				TransactionManager.theTM=self.history
				global theProject
				theProject=self
				if self.profile and not rootElement:
						self.root=self.profile.createModel(name=name)
				else:
						self.root=rootElement

		def __del__(self):
				TransactionManager.theTM=None
				global theProject
				theProject=None
				
		def getRoot(self):
				return self.root

		def setRoot(self,element):
				print "Root element ",element
				self.root=element
				
		def getProfile(self):
				return self.profile

		def loadModel(self,url, toupdate = None):
				if toupdate == None:
						toupdate = {}
				self.dirty=0
				self.history.clear()

				self.root=io.loadModel(url,self.profile.metamodel, toupdate)

				# If we loaded an empty model, we create a default
				if not self.root:
						self.root = self.profile.createModel("Default Model")
						
				self.fileName = url

		def saveModel(self,url='', toupdate = None):
				if toupdate == None:
						toupdate = {}

				if url=='':
						url=self.fileName
				self.fileName=url

				result=io.saveModel(url, self.root, toupdate, self.profile)
				SignalHandling.emit("savedModel", {"toupdate": toupdate} )
				
				self.dirty=0
				return result
				
		def close(self):
				TransactionManager.theTM=None
				global theProject
				theProject=None
				self.root=None
				
		def startDragging(self,e):
				self.dragObject=e

		def stopDragging(self):
				e=self.dragObject
				self.dragObjet=None
				return e

def getProjectInstance():
		global theProject
		if theProject==None:
				theProject=Project()
		return theProject
		
class ModifyCmd:
		def __init__(self,mode):
				self.mode=mode
				self.changesL=[]
				self.newObjects={}
				
		def __repr__(self):
				s=''
				return s

		def getNewElements(self):
				r=OCLforPython.MMSequence()
				for x in self.newObjects.keys():
						if not isinstance(x,MetaMM.Element):
								continue
						r.insert(x)
				return r

		def getNewConnectedElements(self):
				r=OCLforPython.MMSequence()
				for x in self.newObjects.keys():
						if not isinstance(x,MetaMM.Element):
								continue
						if MetaMM.isConnectedTo(x,theProject.getRoot()):
								r.insert(x)
				return r

		def getNewUnconnectedElements(self):
				r=OCLforPython.MMSequence()
				for x in self.newObjects.keys():
						if not isinstance(x,MetaMM.Element):
								continue
						if not MetaMM.isConnectedTo(x,theProject.getRoot()):
								r.insert(x)
				return r
		
		def getUpdatedElements(self):
				r=OCLforPython.MMSequence()
				p={}
				for x in self.changesL:
						o=x[0]
						if isinstance(o,MetaMM.MMAssociationEnd):
								o=o.parent
								if not o:
										continue
						if p.has_key(o) or not isinstance(o,MetaMM.Element):
								continue
						else:
								p[o]=1
						if not self.newObjects.has_key(o) and MetaMM.isConnectedTo(o,theProject.getRoot()):
								r.insert(o)
				return r
		
		def getUnconnectedElements(self):
				r=OCLforPython.MMSequence()
				p={}
				for x in self.changesL:
						if p.has_key(x[0]) or not isinstance(x[0],MetaMM.Element):
								continue
						else:
								p[x[0]]=1
						if not MetaMM.isConnectedTo(x[0],theProject.getRoot()):
								r.insert(x[0])
				return r
		
		def addChange(self,obj,name,previous):
				self.changesL.append([obj,name,previous])
				
		def execute(self):
				self.unexecute()
				
		def unexecute(self):
				print "start unexcute"
				toUpdate={}
				pToUpdate={}
				toKillorRevive={}
				self.changesL.reverse()
				print len(self.changesL)," updates to process",
				for x in self.changesL:
						obj=x[0]
						attr=x[1]
						old=x[2]
						current=getattr(obj,attr,None)
						
						if isinstance(obj,MetaMM.PresentationElement):
								if attr=="oldCanvas" or attr=="editor" or attr=="oldParent":
										print "presentation ",obj,attr,current,old
										if old:
												print "to be revived"
												toKillorRevive[obj]=2
										else:
												print "to be killed"
												toKillorRevive[obj]=1
										pToUpdate[obj]=1
						else:
								if isinstance(obj,MetaMM.Element):
										toUpdate[obj]=1
								elif isinstance(obj,MetaMM.MMAssociationEnd):
										toUpdate[obj.parent]=1
																			 
						x[2]=current
						if attr!="__dead__":
								obj.__dict__[attr]=old
						else:
								if obj.__isDead__():
										del obj.__dict__[attr]
								else:
										obj.__dict__[attr]=old
										
				# update the representations

				print "processing presentations"
				#logger.info("MMAtoms to kill:",toKill)
				for o in toKillorRevive.keys():
						if toKillorRevive[o]==1:
								o.__kill__()
						else:
								o.__revive__()						


				#logger.info("MMAtoms to update:",toUpdate)
				for o in toUpdate.keys():
						if not toKillorRevive.has_key(o):
								#print "updating ",o
								if isinstance(o,MetaMM.Element):
										for p in o.presentation:
												#print "	updating ",p
												p.update()

				#logger.info("Presentations to update:",pToUpdate)
				for o in pToUpdate.keys():
						print o
						o.update()
				print "end unexecute"

class CommandHistoryObserver:
		def onUndoChanged(self,undo):
				pass
		def onRedoChanged(self,redo):
				pass

class Subject:
		def __init__(self):
				self.observers=[]
		def subscribe(self,o):
				if o not in self.observers:
						self.observers.append(o)
		def unsubscribe(self,o):
				if o in self.observers:
						self.observers.remove(o)
		def notify(self,name):				
				for o in self.observers:
						apply(o.__class__.__dict__["on"+name],[o])

						 
class CommandHistory(TransactionManager.TransactionManager,Subject):
		
		def __init__(self,editorSet,debug=1):
				Subject.__init__(self)
				self.editorSet=editorSet
				self.clear()
				self.transactionNumber=0L
				self.maxlength=20
				self.debug=debug
				
		def getTransactionNumber(self):
				return self.transactionNumber
		
		def clear(self):
				# reset history, but do not loose observers
				self.inModifyCmd=0
				self.currentCmd=None
				self.history=[]
				self.present=0
				
		def _do(self,cmd,execute=1):
				#logger.info("do ",cmd)
				assert(not self.inModifyCmd)

				oldU=self.canUndo()
				oldR=self.canRedo()
				
				if self.present>len(self.history)-1:
						self.history.append(cmd)
				else:
						self.history=self.history[:self.present]
						self.history.append(cmd)

				if len(self.history)>self.maxlength:
						#print "triming history..."
						self.history=self.history[1:]
				else:
						self.present=self.present+1

				if execute:
						cmd.execute()

				if oldU!=self.canUndo():
						self.notify("UndoChanged")
				if oldR!=self.canRedo():
						self.notify("RedoChanged")

		def trimFuture(self):
				oldR=self.canRedo()
				if self.present<=len(self.history)-1:
						self.history=self.history[:self.present]
				if oldR!=self.canRedo():
						self.notify("RedoChanged")
						
		def canUndo(self):
				return len(self.history) and self.present
		
		def undo(self):
				oldU=self.canUndo()
				oldR=self.canRedo()
				
				assert(not self.inModifyCmd)
				if len(self.history) and self.present:
						self.present=self.present-1
						self.history[self.present].unexecute()

				if oldU!=self.canUndo():
						self.notify("UndoChanged")
				if oldR!=self.canRedo():
						self.notify("RedoChanged")


		def canRedo(self):
				return self.present<len(self.history)
		
		def redo(self):
				oldU=self.canUndo()
				oldR=self.canRedo()
				
				assert(not self.inModifyCmd)
				if self.present<len(self.history):
						self.history[self.present].execute()
						self.present=self.present+1

				if oldU!=self.canUndo():
						self.notify("UndoChanged")
				if oldR!=self.canRedo():
						self.notify("RedoChanged")

				
		def beginModifyCmd(self,mode=TransactionManager.TransactionManager.relaxedMode):
				if not self.inModifyCmd:
						#print "!!!!>>>>>>>>>>>>>>>>>>>>>>>>>>> BOT "+str(self.transactionNumber)+"<<<<<<<<<<<<<<<<<<<<<<!!!"
						self.inModifyCmd=1
						self.currentCmd=ModifyCmd(mode)
				else:
						self.inModifyCmd=self.inModifyCmd+1

		def partialModifyCmd(self,obj,name,previous):
				assert(self.inModifyCmd)
				obj.__dict__["__timestamp__"]=time.time()
				self.currentCmd.addChange(obj,name,previous)
				

		def newObjectModifyCmd(self,obj):
				#print "new ",obj
				assert(self.inModifyCmd)
				assert(isinstance(obj,MetaMM.MMClass))

				#if not isinstance(obj,MetaMM.Element):
				#		# we don't care about presentations
				#		return							 
													
				if not self.currentCmd.newObjects.has_key(obj):
						self.currentCmd.newObjects[obj]=1

		def endModifyCmd(self,updatePresentations=1):
				assert(self.inModifyCmd)

				if self.inModifyCmd==1 and len(self.currentCmd.changesL):
						theProject.dirty=1
						
						if updatePresentations and self.editorSet:
								for o in self.currentCmd.newObjects.keys():
										self.editorSet.notifyAddElement(o)
										
						# first update presentations
						if updatePresentations:
								updated={}
								logger.info("Changes in current ModifyCmd: ", len(self.currentCmd.changesL))
								for k in self.currentCmd.changesL:
										obj=k[0]
										if isinstance(obj,MetaMM.MMAssociationEnd):
												obj=obj.parent
										if not updated.has_key(obj) and obj not in self.currentCmd.newObjects.keys() :
												# debug mode
												if self.debug and isinstance(obj,MetaMM.Element) \
															 and theProject.root and not theProject.root.isPart(obj):
														print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
														print "Warning: New Object ",obj," is not a part of the root of the model!"
														print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
												if isinstance(obj,MetaMM.Element):
														for p in obj.presentation:
																p.update()
										updated[obj]=1

						

						# then finish the transaction
						print ">>>>>>>> EOT "+str(self.transactionNumber)+"<<<<<<<<<<<"
						self.inModifyCmd=0
						#debug.info("Begin transaction ",self.transactionNumber)
						self._do(self.currentCmd,execute=0)
		
						self.transactionNumber=self.transactionNumber+1
						cmd=self.currentCmd
						self.currentCmd=None

						if cmd.mode==self.strictMode:
								if not theProject.getRoot():
										raise "Project has not root element. Use the method setRoot to define the main element in the project. In UML this element is usually a Model"
								else:
										try:
												wfrAlgorithm1(cmd.changesL)
										except MetaMM.WFRException,e:
												self.undo()
												raise e
						return 1
				else:
						self.inModifyCmd=self.inModifyCmd-1
						return 0

		def lastTransaction(self):
				assert(self.present)
				return self.history[self.present-1]
				
def wfrAlgorithm1(changes):		
	 checked={}
	 for k in changes:
			 objs=[k[0]]
			 if isinstance(objs[0],MetaMM.MMAssociationEnd):
					 objs=[objs[0].parent]+objs[0].items

			 for i in objs:
					 if isinstance(i,MetaMM.Element) and not checked.has_key(i):
							 print "checking ",i
							 try:
									 i.isWellFormed()
							 except MetaMM.WFRException,e:
									 if MetaMM.isConnectedTo(i,theProject.getRoot()):
											 raise e
							 checked[i]=1



def wfrAlgorithm2(changes):
		theProject.getRoot().isWellFormedRecursive()
														
								
						
		
