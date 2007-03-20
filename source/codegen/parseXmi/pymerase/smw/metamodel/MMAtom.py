# -*- coding: utf-8 -*-
from smw.metamodel import TransactionManager
from smw.metamodel.MetamodelDataTypes import *
from smw.metamodel.UniqueID import *
import time
class MMAtom:

		"""All classes in a metamodel module are subclasses of the MMAtom
		class. The main responsibility of an MMAtom instance is to report
		all changes in its state to a transaction manager.	"""

		def __init__(self):
				if not hasattr(self,"__uniqueID__") or not self.__uniqueID__:
						self.__uniqueID__ = getUniqueID()
				if not hasattr(self,"__timestamp__") or not self.__timestamp__:
						self.__timestamp__=time.time()
						
		def __register__(self,name,old):
				if TransactionManager.theTM and TransactionManager.theTM.inModifyCmd:
								TransactionManager.theTM.partialModifyCmd(self,name,old)
								
		def __registercreation__(self):
				if TransactionManager.theTM and TransactionManager.theTM.inModifyCmd:
								TransactionManager.theTM.newObjectModifyCmd(self)
								
		def __setattr__(self,name,value):
			if TransactionManager.theTM and TransactionManager.theTM.inModifyCmd:
					if self.__dict__.has_key(name):
							if value!=self.__dict__[name]:
									TransactionManager.theTM.partialModifyCmd(self,name,self.__dict__[name])
					else:
							TransactionManager.theTM.partialModifyCmd(self,name, value)
			
			#
			# Enforce types a bit.
			# I'm sick of python's
			# holier-than-thou-everything-just-works-until-it-breaks ideology
			#
			if self.__class__.__dict__.has_key("__mm__") and type(self.__mm__) == dict and self.__mm__.has_key(name):
				if issubclass(self.__mm__[name][1], MMUnlimitedInteger):
					if type(value) != int and value != None:
						print "Element %s, key %s: value %s is not an integer" % (self, name, str(value))
						assert(0)
				elif issubclass(self.__mm__[name][1], MMString):
					if type(value) != str and value != None:
						print "Element %s, key %s: value %s is not a string" % (self, name, str(value))
						assert(0)
				elif issubclass(self.__mm__[name][1], MMEnumeration):
					if type(value) != int:
						print "Element %s, key %s: value %s is not an enumeration integer" % (self, name, str(value))
						assert(0)
			self.__dict__[name]=value

		def __XMIid__(self):
				"""Return an XMI id for the atom"""
				return self.__uniqueID__

		def update(self):
				
				"""This method is called by the transaction manager to notify
				that the attributes of the atom have been changed. It used by
				the presentations to update their widgets"""

		def __kill__(self):
				"""This method is called by the transaction manager to notify
				that the atom has been removed from the model.

				This does not mean the atom will be destroyed since it will
				probably reamin in the undo history for a while.

				However, if the atom is a presentation it should hide its
				widget. Normal atoms should do nothing."""
				
				pass


		def __revive__(self):

				"""This method is called by the transaction manager to notify
				that the atom is back into the model (the oposite of __kill__).

				This can happen if the users redoes a command. If the atom is
				a presentation then it should recreate its widget. Normal
				atoms should do nothing.	"""				
				
				pass

	 

		def oclIsKindOf(self,c):
				""" returns true if the object is an instance of c """
				return isinstance(self,c)

		def isTypeOf(self,anotherO):		
				""" returns true if the object is of the same type as anotherO"""
				return type(self)==type(anotherO)
