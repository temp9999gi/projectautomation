# -*- coding: utf-8 -*-
#SMW System Modeling Workbench
#Copyright 2001,2002 by Ivan Porres iporres@abo.fi
#
#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.
# 
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
#GNU General Public License for more details.


import copy
import inspect
import types
import string
import time
import os
from smw.exceptions import *

from smw.metamodel.TransactionManager import TransactionManager
from smw.metamodel.MMAtom import MMAtom
from smw.metamodel.OCLforPython import * 
from smw.metamodel.MetamodelDataTypes import *
from smw.metamodel.UniqueID import getUniqueID

from smw import release
from smw.ipmanager import IPManager
IPManager().registerIPModule(release)

class MMClass(MMAtom):
		kind__Attribute=1
		kind__Association=2
		kind__Composition=3
		One=1
		Many=0
		
		def __init__(self,**args):
				self.__registercreation__()
				self.__initattrs__(**args)

				# This defines if the given element is the topmost element
				# of a module
				self.modulestring = None

				# Defines extra opaque XMI.extension stuff that
				# other tools use
				self.xmiextension = None

				MMAtom.__init__(self)

		def setModule(self, string):
				self.modulestring = string

		def getModule(self):
				assert(self.isModule())
				return self.modulestring

		def isModule(self):
				return self.modulestring and len(self.modulestring) > 0
		
		def __initattrs__(self,**args):
			for name in self.__mm__.keys():
				if not self.__dict__.has_key(name):
					(kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=self.__mm__[name]
					if kind==self.kind__Attribute:
						# is an attribute
						if issubclass(mmtype,MMDataType):
								MMAtom.__setattr__(self,name,mmtype.default)
						else:
								 MMAtom.__setattr__(self,name,mmtype())
					else:
						# is an association
						if multiplicity==1:
								MMAtom.__setattr__(self,name,None)
						else:
								MMAtom.__setattr__(self,name,MMAssociationEnd([],self,name,self.__mm__[name]))

			for k in args.keys():
				self.__setattr__(k,args[k])


		def __isDead__(self):
				return self.__dict__.has_key("__dead__")
		
		def __resetattrs__(self):
				"""sets the attributes to a model element to default values.
				This method should be used to delete a model element from the model.

				5.8.02 Now it also resets the parts.
				"""
				self.__dead__=1
				for name in self.__mm__.keys():
						(kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=self.__mm__[name]
						a=getattr(self,name)
						if kind==self.kind__Attribute:
								# is an attribute
								if issubclass(mmtype,MMDataType):
										self.__setattr__(name,mmtype.default)
								else:
										#if a:
										#		a.__resetattrs__()
										self.__setattr__(name, None)
						elif kind==self.kind__Composition:
								if multiplicity==1:
										if a:
												a.__resetattrs__()
								else:
										for x in copy.copy(a):
												x.__resetattrs__()
										self.__setattr__(name,MMAssociationEnd([],self,name,self.__mm__[name]))
						else:
								# is an association
								if multiplicity==1:
										self.__setattr__(name,None)
								else:
										self.__setattr__(name,MMAssociationEnd([],self,name,self.__mm__[name]))

		def __whereIsAttrDefined__(self,a,candidate=None):
				if not candidate:
						candidate=self.__class__
				bases=list(candidate.__bases__)
				if MMClass in bases:
						bases.remove(MMClass)
				for b in bases:
						if b.__mm__.has_key(a):
								candidate=b.__whereIsAttrDefined__(self,a,b)
				return candidate
		
		def __getstate__(self):
				# returns a dictionary with the state of the object
				# the dictionary does not contain empty attributes or association ends
				# since they are created by init
				dict=copy.copy(self.__dict__)
				for name in self.__mm__.keys():
						(kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=self.__mm__[name]
						if multiplicity==0 and getattr(self,name).size()==0:
							 del dict[name]
						else:
								if getattr(self,name)==None:
										del dict[name]
				return dict
								
		def __setstate__(self,newstate):
				self.__initattrs__()
				for k in newstate.keys():
						self.__dict__[k]=newstate[k]
						
		def __setclass__(self,newclass):
				self.__class__=newclass
				self.__mm___=newclass.__mm__
				self.__initattrs__()

		def __insert__(self, name, val, index):
				"""Insert val at self.name at index 'index', but NOT
				at the opposite end. Yes, this is
				needed in the metamodel to keep stuff in _order_!

				The index can be <0 meaning plain append.

				Yes, this is very similar to __setattr__. Yes, it's a kludge."""

				assert(self.__mm__.has_key(name))
				(kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=self.__mm__[name]

				# Always an association/composition
				assert(kind != self.kind__Attribute)
				# Always for sets, we have other commands for multiplicity == 1
				assert(multiplicity == 0)

				# BUG comment this after testing
				assert(index != -999)

				if index < 0:
						index = len(self.__dict__[name]) + index + 1

				self.__dict__[name].insert(val, index)
		
		def __setattr__(self,name,val):
				if self.__mm__.has_key(name):
						(kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=self.__mm__[name]
						if kind==self.kind__Attribute:
								# is an attribute
								if type(val)==types.InstanceType and not isinstance(val,mmtype):
										raise WFRException("Type error in attribute "+name+". Expected "+str(mmtype)+" instance. Found "+str(val.__class__))
								MMAtom.__setattr__(self,name,val)
						else:
								# is an association
								if multiplicity==1:
										if self.__dict__[name]:
												if otherMultiplicity==0:
														self.__dict__[name].__dict__[otherRole].remove(self)
												else:
														MMAtom.__setattr__(self.__dict__[name],otherRole,None)
										if val!=None and type(val)!=type(mmtype) and	not (type(val)==types.InstanceType and isinstance(val,mmtype)):
											 raise WFRException("Type error in attribute "+name+". Expected "+str(mmtype)+" Found",val)
										MMAtom.__setattr__(self,name,val)

										if self.__dict__[name]:
												if otherMultiplicity==0:
														self.__dict__[name].__dict__[otherRole].append(self)
												else:
														MMAtom.__setattr__(self.__dict__[name],otherRole,self)
										
								else:
										if self.__dict__[name]:
												if otherMultiplicity==0:
														for x in	copy.copy(self.__dict__[name].items):
																x.__dict__[otherRole].remove(self)
												else:
														for x in self.__dict__[name]:
																MMAtom.__setattr__(x,otherRole,None)
										if type(val)==types.ListType:												
												MMAtom.__setattr__(self,name,MMAssociationEnd(val,self,name,self.__mm__[name]))
										elif	type(val)==types.InstanceType and isinstance(val,MMAssociationEnd):
												if val.__mm__[1]!=mmtype:
														raise WFRException("TypeError: AssociationEnd has different mmtype")
												else:
														# should it be a copy?
														MMAtom.__setattr__(self,name,val)
										else:
												raise WFRException("TypeError: it should be list or MMAssociationEnd")
																																														
				else:
						# attribute or association not found
						#raise "TypeError: Attribute or association not found"
						MMAtom.__setattr__(self,name,val)

		def __gatherCL__(self,cl,c):
						for b in c.__bases__:
								if b not in cl:
										cl.append(b)
										self.__gatherCL__(cl,b)
						return cl

		def __deepcopy__(self,dict=None):
				"""Use MetaMM.modelcopy instead."""
				assert(0)

		def getAllParts(self):
				"""Returns a MMSet with all the elements transitively owned by this object"""
				r=MMSet()
				for a in self.__mm__.keys():
						(kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=self.__mm__[a]						
						if a!="presentation" and kind == self.kind__Composition:
								attr = get_children(self, a)
								for o in attr:
										if isinstance(o, MMClass):
												r.append(o)
												r=r+o.getAllParts()
				return r

		##def isPart(self,obj):
##				"""Returns true if obj is a part self"""
##				if obj==self:
##						return 1
				
##				for a in self.__mm__.keys():
##						(kind,mmtype,multiplicity,otherRole,otherMultiplicity)=self.__mm__[a]						
##						if a!="presentation" and kind == self.kind__Composition:
##								attr = get_children(self, a)
##								for o in attr:
##										if o==obj:
##												return 1
##										if isinstance(o, MMClass):
##												if o.isPart(obj):
##														return 1
##				return 0

		def isPart(self,obj,recurse=1):
				if obj==self:
						return 1
				for a in obj.__mm__.keys():
						(kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=obj.__mm__[a]
						if kind!= self.kind__Association:
								continue
						otherKind=mmtype.__mm__[otherRole][0]
						if a!="subject" and otherKind == obj.kind__Composition:
								attr = get_children(obj, a)
								for o in attr:
										if o==self:
												return 1
										if isinstance(o, MMClass) and recurse:
												if self.isPart(o):
														return 1
				return 0
		
		def __modelcopy1__(self,dict):
				# Pass 1, we just create the objects

				if self in dict:
						return dict[self]

				new=self.__class__()
				dict[self]=new

				# we create new objects for attributes and compositions
				# but not for associations

				for a in self.__mm__.keys():
						(kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=self.__mm__[a]
						if a == "presentation":
								continue
						# Remember, we must let trough Compositions and
						# "element attributes"
						if kind == self.kind__Association:
								continue
						attr = get_children(self, a)
						for o in attr:
								if isinstance(o, MMClass):
										o.__modelcopy1__(dict)

				return dict[self]

		def __modelcopy2__(self,dict,dict2, dict3, keep_associations_outside_subtree):

				if self in dict2:
						return dict[self]

				dict2[self]=1
				
				# Right, now everybody [under composition] is copied
				# time to solve those references
				new=dict[self]
				
				for a in self.__dict__.keys():
						if not self.__mm__.has_key(a):
								#normal variables are deepcopied as usual
								setattr(new,a,copy.deepcopy(getattr(self,a)))
						else:
								(kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=self.__mm__[a]
								if a == "presentation":
										continue
								
								if kind == self.kind__Association:
										# it is an association, shallowcopy it, but remember
										# that it can point to old or new deepcopied elements
										if multiplicity==1:
												other=getattr(self,a)
												# The keep_association_outside subtree is for
												# module support
												if (otherMultiplicity == 1 or not keep_associations_outside_subtree) and not dict.has_key(other):
														# Outside our deepcopy scope, and
														# target can only have one element =>
														# we must skip this
														new.__dict__[a] = None
														pass
												else:
														# Can't use setattr - other end would update!
														new.__dict__[a] = dict.get(other, other)
														### IPP: why not?
														###setattr(new,a,dict.get(other,other))
														# Because it could scramble order.
														#
														# Example:
														#
														# m = Model()
														# c1 = Class()
														# c2 = Class()
														# c1.namespace = m
														# c2.namespace = m
														#
														# m.ownedElement == [c1, c2]
														#
														# Copy model:
														# * m2.ownedElement is set to [c1, c2]
														# * c1.namespace is set to m2, _but_
														#	 now the order is different,
														#	 m2.ownedElement == [c2, c1]
														#	 => not a perfect copy
														# Needless to say, this is hard to reproduce
														# but I know the problem still is there
														# if you use setattr, but __dict__
														# solves this.
														# --msa
														#

														# Association outside?
														if other and not dict.has_key(other):
																#dict3[(other, otherRole)] = 1
																other.__dict__[otherRole].items.append(new)
																
										else:
												l=getattr(new,a)
												# Now go trough it again, and properly add in order
												for o in getattr(self, a):
														if (otherMultiplicity == 1 or not keep_associations_outside_subtree) and not dict.has_key(o):
																# We must skip this, since target can't keep
																# both connections
																pass
														else:
																###l.append(dict.get(o, o))
																# Same thing here,
																# we don't want to update the
																# other end
																l.items.append(dict.get(o, o))

																# Association outside?
																if o and not dict.has_key(o):
																		#dict3[(o, otherRole)] = 1
																		o.__dict__[otherRole].items.append(new)
																		
								else:															 
										# deepcopy!
										if multiplicity==1:
												attr = getattr(self, a)
												if isinstance(attr, MMClass):
														new.__dict__[a] = attr.__modelcopy2__(dict,dict2, dict3, keep_associations_outside_subtree)
												else:
														new.__dict__[a] = copy.deepcopy(attr)
										else:
												l=getattr(new,a)
												for o in getattr(self,a):
														if isinstance(o, MMClass):
																# Don't update other end
																l.items.append(o.__modelcopy2__(dict,dict2, dict3, keep_associations_outside_subtree))
														else:
																# Don't update other end
																l.items.append(copy.deepcopy(o))
														
				# voila! perfect copy
														
				return dict[self]

##		def __modelcopy3__(self, dict, key):
##				children = get_children(self, key)
##				going_to_append = []
##				for c in children:
##						if dict.has_key(c):
##								going_to_append.append(c)

##				for c in going_to_append:
##						self.__dict__[key].items.append(dict[c])

		
		def asSet(self):
				return MMSet([self])

				
		def isWellFormed(self,toIgnore=[]):
				cl=self.__gatherCL__([self.__class__],self.__class__)
				for c in cl:
						for m in c.__dict__.values():
								if type(m)==types.FunctionType:
										if m.__name__[:3]=="wfr" and m.__name__ not in toIgnore:
												if not apply(m,(self,)):
														raise WFRException("Well-formed rule "+m.__name__+" does not hold ",formatWellFormedRuleException(m,self))
				if hasattr(self,"__userWellFormedRule__"):
						for c in self.__userWellFormedRule__:
								if not apply(c,(self,)):
										raise WFRException("User-defined well-formed rule "+m.__name__+" does not hold ",formatWellFormedRuleException(m,self))
						
				return 1

				
		def isWellFormedRecursive(self,toIgnore=[],dict=None):
				if not dict:
						dict={}
				if dict.has_key(self):
						return 1
				
				self.isWellFormed(toIgnore)
				dict[self]=1
				for k in self.__mm__.keys():
						if self.__mm__[k][2]==1:
								val=getattr(self,k)
								if type(val)==types.InstanceType and isinstance(val,MMClass):
										val.isWellFormedRecursive(toIgnore,dict)
						else:
								for val in getattr(self,k):
										if type(val)==types.InstanceType and isinstance(val,MMClass):
												val.isWellFormedRecursive(toIgnore,dict)
				return 1				 

		def getMetamodel(self):
				from smw.metamodel.Reflection import getMetamodelByName
				return getMetamodelByName(self.__module__)
# The simple reflection interface

		def getParent(self):
				"""Returns the parent element, if available."""
				# Note, there are many composition associations, but only
				# one can be valid.
				for key in self.__mm__.keys():
						(kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=self.__mm__[key]
						if kind != MMClass.kind__Association:
								continue
						if mmtype.__mm__[otherRole][0] == MMClass.kind__Composition:
								assert(multiplicity == 1)
								parent = getattr(self, key)
								if parent:
										return parent
				return None
						

def addWellFormedRule(c,name,l):
		# FIX ME: we disscard the name
		c.__userWellFormedRule__.append(l)

def formatWellFormedRuleException(rule,object):
		s=		"\nRule name:"+object.__class__.__name__+"."+rule.__name__+"\n"
		try:
				s=s+"Rule body:\n"+inspect.getsource(rule.func_code)
		except:
				pass
		s=s+"Offender:"+str(object)
		return s
		
def modelcopy(o, create_new_xmis = 0, keep_associations_outside_subtree = 1):
		dict={}	# Contains mapping old_object => new_object
		dict2={} # Contains new_object => 1
		# dict3 is not used
		dict3={} # Contains tuples (old_object, key) => 1
		
		if type(o)==type([]) or \
			 (type(o)==types.InstanceType and isinstance(o,MMSet)):
				if type(o)==type([]):
						result=[]
				else:
						result=MMSet()
				for e in o:
						assert(isinstance(e,MMClass))
						x=e.__modelcopy1__(dict)
						result.append(x)
			 
		else:
				assert(isinstance(o,MMClass))
				result=o.__modelcopy1__(dict)

		for e in dict.keys():
				e.__modelcopy2__(dict,dict2, dict3, keep_associations_outside_subtree)

		# Does the user wish we create new XMI strings?
		if create_new_xmis:
				for new_obj in dict.values():
						new_obj.__uniqueID__ = getUniqueID()

		#for (obj, key) in dict3.keys():
		#		obj.__modelcopy3__(dict, key)
				
		return result

class MMAssociationEnd(MMSet):
		def __init__(self,value,parent,name,mm):
				self.__name__=name
				self.__mm__=mm
				self.parent=parent
				MMSet.__init__(self)

				for v in value:
						self.append(v)

		
		def __setstate__(self,state):
				#print state
				self.parent=state["parent"]
				self.__mm__=state["__mm__"]
				if len(self.__mm__)==5:
						# old version association, we should add a ordered flag
						self.__mm__=(self.__mm__[0],self.__mm__[1],self.__mm__[2],
												 self.__mm__[3],self.__mm__[4],0)
				self.__name__=state["__name__"]
				self.items=state["items"]
				
		def __setitem__(self,key,v):
				assert(len(self.items)>key)
				self.__enforceWFR__(v,self.items[key])
				self.__register__('items',copy.copy(self.items))
				self.items[key]=v

		def __enforceWFR__(self,v,previous):
				assert(v)
				(kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=self.__mm__
				if type(v)!=types.InstanceType and isinstance(v,MMClass):
						raise WFRException("An associationEnd cannot contain",v)
					
				if not isinstance(v,mmtype):
						raise WFRException("TypeError: Expected a "+str(mmtype)+" got a "+str(v.__class__.__name__))

				(kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=self.__mm__
				if previous:
						if otherMultiplicity==1:
								MMAtom.__setattr__(previous,otherRole,None)
						else:
								previous.__dict__[otherRole].__register__('items',copy.copy(previous.__dict__[otherRole].items))
								previous.__dict__[otherRole].items.remove(self.parent)
								 
				if otherMultiplicity==1:
						if v:
								old=getattr(v,otherRole)
								if old:
										getattr(old,self.__name__).remove(v)
						MMAtom.__setattr__(v,otherRole,self.parent)
				else:
						v.__dict__[otherRole].__register__('items',copy.copy(v.__dict__[otherRole].items))
						v.__dict__[otherRole].items.append(self.parent)
						
		def append(self,v):
				if v not in self.items:
						self.__enforceWFR__(v,None)								
						self.__register__('items',copy.copy(self.items))					 
						self.items.append(v)
										
		add=append

		def remove(self,item):
				 if item in self.items:
						 (kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=self.__mm__
						 if otherMultiplicity==1:
								 MMAtom.__setattr__(item,otherRole,None)
						 else:
								 item.__dict__[otherRole].__register__('items',copy.copy(item.__dict__[otherRole].items))
								 item.__dict__[otherRole].items.remove(self.parent)
						 self.__register__('items',copy.copy(self.items))
						 self.items.remove(item)

		def __pop__(self, index):
				"""Removes value at specified index, BUT NOT from the other end."""
				return self.items.pop(index)

		def pop(self, index, otherindex = -1):
				"""Removes the value at specified index, and at otherindex if specified."""
				self.__register__('items',copy.copy(self.items))
				item = self.items.pop(index)
				(kind,mmtype,multiplicity,otherRole,otherMultiplicity,ordered)=self.__mm__
				if otherMultiplicity==1:
						MMAtom.__setattr__(item,otherRole,None)
				else:
						item.__dict__[otherRole].__register__('items',copy.copy(item.__dict__[otherRole].items))
						if otherindex == -1:
								item.__dict__[otherRole].items.remove(self.parent)
						else:
								assert(item.__dict__[otherRole].items[otherindex] == self.parent)
								item.__dict__[otherRole].items.pop(otherindex)


		def __getstate__(self):
				state={}
				toSave=[]
				for p in self.items:
						if not isinstance(p,PresentationElement) or \
							 isinstance(p,MMPickablePresentation):
								toSave.append(p)
				state['__mm__']=self.__mm__
				state['__name__']=self.__name__
				state['parent']=self.parent
				state['items']=toSave
				return state

def set_children(element, key, children, oneway = 0):
		"""Sets the children of an element. This function is
		useful since we have to check for various conditions
		when setting the children of an element."""

		multiplicity = element.__mm__[key][2]

		out = children

		if multiplicity == 1:
				assert(len(children) < 2)
				if len(children) == 0:
						out = None
				else:
						out = children[0]
		else:
				# This whole block for assertion purposes only
				assert(type(out) == list or isinstance(out, MMCollection))
				if oneway:
						assert(isinstance(out, MMCollection))
				test1 = {}
				test2 = {}
				for i in out:
						if test1.has_key(i):
								print "Already have key",i
								print out
								assert(0)
						if test2.has_key(i.__XMIid__()):
								print "Already have key",i.__XMIid__()
								print out
								assert(0)
						test1[i] = 1
						test2[i.__XMIid__()] = 1

		if not oneway:
				setattr(element, key, out)
		else:
				element.__dict__[key] = out

def get_children(element, key):
		"""Returns a list of element's children in the key
		association/composition/'object attributes'. Any other
		kind, and it returns the empty list.
		
		An 'object attribute' is basically an attribute that points
		to metamodel classes instead of python primitives. Have a look
		at e.g. ClassifierRole.multiplicity. Kinda freaky. """

		children = []

		kind = element.__mm__[key][0]
		multiplicity = element.__mm__[key][2]

		if kind == MMClass.kind__Association:
				children = getattr(element, key)
		elif kind == MMClass.kind__Composition:
				children = getattr(element, key)
		elif not issubclass(element.__mm__[key][1], MMDataType):
				children = getattr(element, key)

		if multiplicity == 1:
				if children == None or children == []:
						children = MMSet()
				else:
						children = MMSet([ children ])
		else:
				pass

		# This whole block for assertion purposes only
		assert(isinstance(children, MMCollection))

##		test1 = {}
##		test2 = {}
##		for i in children:
##				if test1.has_key(i):
##						print "Already have key",i
##						print children
##						#assert(0)
##				if test2.has_key(i.__XMIid__()):
##						print "Already have key",i.__XMIid__()
##						print children
##						#assert(0)
##				test1[i] = 1
##				test2[i.__XMIid__()] = 1
						
		return children


def getElementsOfModel(model):
		"""Returns all elements of a model as an uuid->object hash.
		It does this by DFS-traversing through the compositions."""
		all_elements = {}
		if not model:
				return all_elements
		
		# Elements on the queue
		to_do = [ model ]
		while len(to_do):
				element = to_do.pop()
				all_elements[element.__XMIid__()] = element

				for key in element.__mm__.keys():

						kind = element.__mm__[key][0]

						if kind != MMClass.kind__Composition and not (kind == MMClass.kind__Attribute and not issubclass(element.__mm__[key][1], MMDataType)):
								# ASSUME all elements are connected to root model
								# via Compositions.
								continue

						# Skip presentations
						if key == "presentation":
								continue

						children = get_children(element, key)
						for c in children:
								# Due to assumption
								assert(not all_elements.has_key(c))
								assert(c not in to_do)
								to_do.append(c)

		return all_elements


def isConnectedTo(e1,e2):
		"""Returns true is element e1 is transitevely connected to e2
		It returns false if e1 or e2 are dead, even if they are connected.
		
		isConnectedTo2 fails if e1 is an attribute of an object.
		This function provides a fix to this bug, but it is slow.
		"""
		if e1.__isDead__() or e2.__isDead__():
				# dead objects are not *semantically* connected to anything
				return 0
		if not isConnectedTo2(e1,e2):
				return isConnectedTo2(e2,e1)
		else:
				return 1
		
def isConnectedTo2(e1,e2,dict=None):
		"Returns true is element e1 is transitevely connected to e2"

		if e1==e2:
				return 1
		
		if dict==None:
				dict={}

		if dict.has_key(e1):
				return 0
		
		dict[e1]=1

		for key in e1.__mm__.keys():
				kind = e1.__mm__[key][0]
				mmtype= e1.__mm__[key][1]
				multiplicity= e1.__mm__[key][2]
				children = get_children(e1, key)
				if e2 in	children:
								return 1
				else:
						for e in children:
								if isinstance(e,MMClass):
										if isConnectedTo2(e,e2,dict):
												return 1															 

		return 0

def getValue(element, key):
		"""This isn't used so much, I'll have to double-check and perhaps
		delete it.. msa"""
		if not element.__mm__.has_key(key):
				return None

		kind = element.__mm__[key][0]
		if kind == MMClass.kind__Attribute:
				if issubclass(element.__mm__[key][1], MMDataType):
						return getattr(element, key)
				else:
						obj = getattr(element, key)
						if obj:
								return obj.__XMIid__()
						else:
								return None
		else:
				return get_children(element, key)

		assert(0)


def __sort_by_XMI_id__(e1, e2):
		i1 = e1.__XMIid__()
		i2 = e2.__XMIid__()
		if i1 < i2:
				return -1
		if i1 > i2:
				return 1
		return 0

def isOrdered(mm, key):
		"""Returns true if the key in the __mm__ given is
		ordered. This trivial helper function is here so we
		can easily enable/disable the ordered/unordered stuff."""

		# Default
		return mm[key][5] == 1

		# Disable unordered relations
		#return 1

def isSameModel(m1, m2, STRICT = 0):
		"""Checks whether two models are the same, i.e., all connections,
		XMIid strings etc are the same, the actual Element pointers are of course
		different. Set STRICT to false if you wan't to assume
		that two _unordered_ associations are same if they contain the same
		elements (but possible in a different order)"""
		uuids1 = getElementsOfModel(m1)
		uuids2 = getElementsOfModel(m2)

		if len(uuids1) != len(uuids2):
				print uuids1
				for i in uuids1.values():
						print i.name
				print
				print uuids2
				for i in uuids2.values():
						print i.name
				print
				assert(0)
		print
		for i in uuids1.keys():
				print i, uuids1[i]
		print
		for i in uuids2.keys():
				print i, uuids2[i]
		print

		for o in uuids1:
				assert(uuids1[o].__XMIid__() == uuids2[o].__XMIid__())
				assert(uuids1[o].__name__ == uuids2[o].__name__)
				for key in uuids1[o].__mm__.keys():
						kind = uuids1[o].__mm__[key][0]
						if kind != MMClass.kind__Attribute or not issubclass(uuids1[o].__mm__[key][1], MMDataType):
								val1 = get_children(uuids1[o], key)
								val2 = get_children(uuids2[o], key)								

								if not STRICT and not isOrdered(uuids1[o].__mm__, key):
										val1.sort( __sort_by_XMI_id__ )
										val2.sort( __sort_by_XMI_id__ )
								
								if len(val1) != len(val2):
										print uuids1[o], o,key
										print
										for v1 in val1:
												print v1, v1.__XMIid__()
										print
										for v2 in val2:
												print v2, v2.__XMIid__()
										assert(0)
								for i in range(len(val1)):
										if (not uuids1.has_key(val1[i].__XMIid__()) or
												not uuids2.has_key(val1[i].__XMIid__()) or
												val1[i].__XMIid__() != val2[i].__XMIid__()):
												print o, key,i
												print
												print getattr(uuids1[o], key)
												print
												print getattr(uuids2[o], key)
												print
												print val1[i], vars(val1[i])
												print
												print val2[i], vars(val2[i])
												assert(0)
										# BUG could check otherkind too...
						else:
								val1 = getattr(uuids1[o], key)
								val2 = getattr(uuids2[o], key)
								if val1 != val2:
										print o, key
										print val1, val2
										print type(val1), type(val2)
										assert(0)
		return 1



# Minimun Metamodel

class Element(MMClass):
		__name__='Element'
		

class PresentationElement(MMClass):
		__name__='PresentationElement'

		def update(self):
				pass

class DiagramPresentationElement(PresentationElement):
		__name__='DiagramPresentationElement'
		def canDropPresentation(self,p):
				return 1
		def onPresentationDroped(self,p):
				pass
		
class MMPickablePresentation:
		"""MMPickablePresentation marks a Presentation as pickable, i.e. it is
		a permanent presentation that should be saved and restored on a file,
		copied/cut/pasted etc...	"""

class Diagram(PresentationElement,MMPickablePresentation):
		__name__='Diagram'
		def canDropPresentation(self,p):
				return 1
		def onPresentationDroped(self,p):
				pass

Element.__mm__={
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0)
		}



PresentationElement.__mm__={
		'subject': (MMClass.kind__Association,Element,0,'presentation',0,0)
		}

DiagramPresentationElement.__mm__={
		'subject': (MMClass.kind__Association,Element,0,'presentation',0,0),
		'diagram': (MMClass.kind__Association,Diagram,1,'content',0,0),
		'connector': (MMClass.kind__Association,PresentationElement,0,'place',0,0),
		'place': (MMClass.kind__Association,PresentationElement,0,'connector',0,0),
		'master': (MMClass.kind__Association,PresentationElement,1,'part',0,0),
		'part': (MMClass.kind__Association,PresentationElement,0,'master',1,0),
		}

Diagram.__mm__={
		'subject': (MMClass.kind__Association,Element,0,'presentation',0,0),
		'content': (MMClass.kind__Association,PresentationElement,0,'diagram',1,0)
		}

# we import reflection for compatibility

from smw.metamodel.Reflection import *
