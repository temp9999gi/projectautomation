from smw.metamodel import MetaMM
from smw.metamodel.MetaMM import MMClass
from smw.metamodel.MMAtom import MMAtom
from smw.exceptions import *
import copy
from myers_diff import *
from myers_patch import *
from diff_commands import *
import types
from smw.metamodel.Reflection import getMetamodelByName
from smw import log
logger=log.getLogger("repository diff routines")

def create_unordered_editscript(uuids1, uuids2):
		"""Creates an editscript for unordered connections."""

		len_i = len(uuids1)
		len_j = len(uuids2)

		uuids1.sort()
		uuids2.sort()

		# The -999 are just silly not-valid values
		# A -1 is bad since it's also the last element in a python sequence...
		# (note, this doesn't mean we're limited to 999 elements,
		#	it's just a high enough value to catch bugs)
		
		j = 0
		editscript = []
		i = 0
		while i < len_i:
				if j >= len_j:
						break
				if uuids1[i] < uuids2[j]:
						editscript.append(ElementChange(delete_command, uuids1[i], -999))
						i += 1
				elif uuids1[i] > uuids2[j]:
						editscript.append(ElementChange(insert_command, uuids2[j], -999))
						j += 1
				else:
						assert(uuids1[i] == uuids2[j])
						i += 1
						j += 1

		while i < len_i:
				editscript.append(ElementChange(delete_command, uuids1[i], -999))
				i += 1

		while j < len_j:
				editscript.append(ElementChange(insert_command, uuids2[j], -999))
				j += 1

				
		
		return editscript
		
# Two different compares
# ErrorOnly is when you only want to know if there is a difference,
# and FullResults for wanting two know exactly what differences
# there are.

cmpkind__ErrorOnly = 0
cmpkind__FullResults = 1

def compare_two_elements (element1, element2, cmp__kind, model1_elems = None, model2_elems = None):
		"""Compares two elements, and returns either
		a boolean saying if they differ, or a complete structure of
		the differences.
		Note that this is a shallow comparison, an element's keys
		should point to objects with the same __XMIid__() to be
		considered equal (even though the objects pointed are of
		different revisions).
		"""

		if element1 == None and element2 == None:
				if cmp__kind == cmpkind__ErrorOnly:
						return 0
				return (None, None, {}, {})
		
		change_xmiid = None
		change_type = None

		if element1.__XMIid__() != element2.__XMIid__():
				if cmp__kind == cmpkind__ErrorOnly:
						return -1
				change_xmiid = ( change_xmiid_command, element1.__XMIid__(), element2.__XMIid__())
				
		if element1.__name__ != element2.__name__:
				if cmp__kind == cmpkind__ErrorOnly:
						return -1
				change_type = ( change_type_command, element1.__name__, element2.__name__ )
				
		# These are 'association: editscript' hashes that
		# describe what's inserted/deleted in the elements
		edit_associations = {}
				
		all_keys = {}
		for a in element1.__mm__.keys():
				all_keys[a] = 1
		for a in element2.__mm__.keys():
				all_keys[a] = 1

		for key in all_keys.keys():
				if element1.__mm__.has_key(key):
						kind = element1.__mm__[key][0]
				else:
						kind = element2.__mm__[key][0]

				value1 = MetaMM.getValue(element1, key)
				value2 = MetaMM.getValue(element2, key)
						
				if kind == MetaMM.MMClass.kind__Attribute:
						# There could be a weird case here where
						# element1.key contains an attribute
						# and element2.key contains a list of children
						# anyway, it will fail the test and report
						# an edit
						if value1 != value2:
								if cmp__kind == cmpkind__ErrorOnly:
										return -1

								# HACK between different types
								# We can't use pointers, we need to have the XMI id strings!
								if element1.__mm__.has_key(key) and element1.__mm__[key][0] != MetaMM.MMClass.kind__Attribute:
										value1 = map(lambda x: x.__XMIid__(), value1)
										
								if element2.__mm__.has_key(key) and element2.__mm__[key][0] != MetaMM.MMClass.kind__Attribute:
										value2 = map(lambda x: x.__XMIid__(), value2)
										
								edit_associations[key] = [ ElementAttributeChange(change_attribute_command, value1, value2) ]

				elif kind == MetaMM.MMClass.kind__Association or kind == MetaMM.MMClass.kind__Composition:
						children1 = value1
						children2 = value2

						# HACK between different types
						# We need a list, so if we have missing keys or _attributes_ create a list of no children
						if not element1.__mm__.has_key(key) or element1.__mm__[key][0] == MetaMM.MMClass.kind__Attribute:
								children1 = []
						if not element2.__mm__.has_key(key) or element2.__mm__[key][0] == MetaMM.MMClass.kind__Attribute:
								children2 = []
										
						#
						# Make a list of uuids we have in each element.
						#
						uuids1 = map(lambda x: x.__XMIid__(), children1)
						uuids2 = map(lambda x: x.__XMIid__(), children2)

						if cmp__kind == cmpkind__ErrorOnly:
								if not MetaMM.isOrdered(element1.__mm__, key):
										# Sort according to XMIid and compare.
										uuids1.sort()
										uuids2.sort()
										
								if len(uuids1) != len(uuids2):
										return -1
								for i in range(len(uuids1)):
										if uuids1[i] != uuids2[i]:
												return -1
										
								continue



						editscript = None

						#
						#
						# DO WE NEED AN INORDER EDITSCRIPT?
						#
						#
						if MetaMM.isOrdered(element1.__mm__, key):
								
								# Compare using Myers' difference algorithm
								# The comparison is done relative to uuids1
								e = myers(uuids1, uuids2)
								editscript = []
								for (cmd, val, idx) in e:
										editscript.append(ElementChange(cmd, val, idx))

						#
						#
						# UNORDERED EDITSCRIPT CREATION
						#
						#
						else:
								# Special case when multiplicity == 1
								if element1.__mm__[key][2] == 1:
										assert(len(uuids1) <= 1)
										assert(len(uuids2) <= 1)
										
										if len(uuids1) == len(uuids2) == 0:
												editscript = None
												
										elif len(uuids1) != len(uuids2) or uuids1[0] != uuids2[0]:
												if len(uuids1) == 0:
														uuids1 = [ None ]
												if len(uuids2) == 0:
														uuids2 = [ None ]
														
												editscript = [ ElementSingleAssociationChange(change_one_association, uuids1[0], uuids2[0]) ]
												
								else:
										editscript = create_unordered_editscript(uuids1, uuids2)
								
						if editscript:
								edit_associations[key] = editscript
								print "editscript", element1.__XMIid__(), key, editscript
						
				else:
						assert(0)
						
		if cmp__kind == cmpkind__ErrorOnly:
				return 0
		
		return (change_xmiid, change_type, edit_associations)


def __special_mof_patch_func__(private_data, result, command, editscript):
		print "__special_mof_patch_func__"
		children = private_data["children"]
		index = editscript[2]
		value = editscript[1]
		if command == delete_command:
				element = private_data["element"]
				assoc	 = private_data["assoc"]
				#print children
				#print index
				#print editscript
				#print element, element.__XMIid__(), assoc

				assert(element.__mm__[assoc][2] == 0)

				otherelem = private_data["model_uuids"][value]

				# ORDERED
				if MetaMM.isOrdered(element.__mm__, assoc):
						print "REMOVE ORDERED ASSOCIATION"
						print "REMOVING", element, element.__XMIid__(), assoc
						print getattr(element, assoc)
						assert(getattr(element, assoc)[index] == otherelem)
						
				# UNORDERED
				else:
						print "REMOVE UNORDERED ASSOCIATION"
						print getattr(element, assoc)
						index = getattr(element, assoc).index(otherelem)

				# we could use "children" as well
				print "mm_this ", getattr(element, assoc)
				print index
				getattr(element, assoc).__pop__(index)
				print "mm_this ", getattr(element, assoc)
				print "*"
				print vars(otherelem)

		elif command == insert_command:
				value = editscript[1]
				element = private_data["element"]
				assoc	 = private_data["assoc"]
				model_uuids = private_data["model_uuids"]

				if MetaMM.isOrdered(element.__mm__, assoc):
						assert(index >= 0)
				else:
						# unordered, so we insert at the end
						
						assert(index == -999)
						
						index = -1

				#print "NOW"
				#print element, assoc, element.__dict__[assoc]
				#print assoc, model_uuids[value], index
				element.__insert__(assoc, model_uuids[value], index)
				#print element, assoc, element.__dict__[assoc]
				#print "---"

		elif command == change_one_association:
				assert(0)
				
		else:
				assert(0)

#class EOffsets:
#		"""Basically, contains maps (uuid,key) = [[start_index, length]...].
#		Used for modifying the otherindex entries... non-trivial. Error-prone.
#		To my knowledge, never done before either...
#		"""
#		def __init__(self):
#				self.offsets = {}
#
#		def addOffset(self, uuid, key, length, otherindex):
#				if not self.offsets.has_key((uuid, key)):
#						self.offsets[(uuid, key)] = []
#
#				print "ADDOFFSET"
#				print uuid, key, length, otherindex
#				work = self.offsets[(uuid, key)]
#				for i in range(len(work)):
#						if work[i][0] <= otherindex < work[i][0] + work[i][1]:
#								# Exactly at new place
#								if otherindex == work[i][0]:
#										# Don't create a new offset
#										pass
#								else:
#										work.insert(i, [work[i][0], otherindex - work[i][0]])
#										otherindex = work[i][0]
#										i += 1
#
#								self.__fixOffsets__(uuid, key, i)
#
#								print "OFFSET WORK", work
#								return otherindex
#
#				# If we come here, we are either before all the offsets,
#				# or after all of them
#				# The == case doesn't need any work, hence > instead of >=
#				if otherindex > length:
#						work.append([length, otherindex - length])
#						otherindex = length
#
#				print "OFFSET WORK2", work
#				return otherindex
#
#		def delOffset(self, uuid, key, otherindex):
#				"""We have deleted an item, so decrease all stuff
#				in our offset."""
#				if not self.offsets.has_key((uuid, key)):
#						self.offsets[(uuid, key)] = []
#				work = self.offsets[(uuid, key)]
#				for i in work:
#						# if not, then something is really weird
#						assert(work[i][0] > otherindex)
#						# Decrease by one
#						work[i][0] -= 1
#				
#		def __fixOffsets__(self, uuid, key, from_which_index_onward):
#				pop_these = []
#				work = self.offsets[(uuid, key)]
#				for i in range(from_which_index_onward, len(work)):
#						
#						work[i][0] = work[i][0] + 1
#						work[i][1] = work[i][1] - 1
#						
#						assert(work[i][1] >= 0)
#						# Is this offset unnecessary, is it at the correct place?
#						if work[i][1] == 0:
#								pop_these.append(i)
#
#				# So they are popped in a nice order
#				pop_these.reverse()
#
#				for i in pop_these:
#						work.pop(i)

				
class EChange:
		def __init__(self):
				self.mergeconflict = []
				self.modeldifference = None

		def attachMergeConflict(self, mc):
				assert(self.mergeconflict.count(mc) == 0)
				self.mergeconflict.append(mc)
				
		def removeMergeConflict(self, mc):
				i = len(self.mergeconflict)
				self.mergeconflict.remove(mc)
				assert(len(self.mergeconflict) == i - 1)
				mc.elemchange = None
				# Update the ModelDifference also
				if self.modeldifference:
						self.modeldifference.dropMergeConflict(mc)

		def hasMergeConflicts(self):
				return len(self.mergeconflict) > 0

		def isSimilarTo(self, ec):
				assert(0)

class ElementAttributeChange (EChange):
		def __init__(self, command, frm, to):
				self.command = command
				self.frm = frm
				self.to = to
				EChange.__init__(self)

		def isSimilarTo(self, ec):
				return isinstance(ec, ElementAttributeChange) and self.command == ec.command and self.frm == ec.frm and self.to == ec.to

		def __str__(self):
				t = "<<%s, %s, %s" % (self.command, self.frm, self.to)
				if self.mergeconflict:
						t += ", %s" % str(self.mergeconflict)
				t += ">>"
				return t

class ElementSingleAssociationChange (EChange):
		def __init__(self, command, frm, to):
				assert(command == change_one_association)
				self.command = command

				# due to marshalling
				if frm == 0:
						frm = None
				if to == 0:
						to = None

				# Doesn't make sense otherwise
				assert(frm != to)
				
				self.frm = frm
				self.to = to
				EChange.__init__(self)

		def isSimilarTo(self, ec):
				return isinstance(ec, ElementSingleAssociationChange) and self.command == ec.command and self.frm == ec.frm and self.to == ec.to
		
		def thisEndUnordered(self):
				# Always considered unordered, since we have only one
				# element
				return 1
		
		def __str__(self):
				t = "<<%s, %s, %s" % (self.command, self.frm, self.to)
				if self.mergeconflict:
						t += ", %s" % str(self.mergeconflict)
				t += ">>"
				return t


class ElementChange (EChange):
		def __init__(self, command, value, index = -999):
				assert(command == insert_command or command == delete_command)
				self.command = command
				self.value = value
				self.index = index
				assert(type(self.index) == int)
				EChange.__init__(self)

		def isSimilarTo(self, ec):
				"""Returns true if self is similar to ec."""
				return isinstance(ec, ElementChange) and self.command == ec.command and self.value == ec.value and self.index == ec.index

		def thisEndUnordered(self):
				return self.index == -999

		def __str__(self):
				assert(type(self.index) == int)

				if self.index == -999:
						i = "-"
				else:
						i = str(self.index)

				t = "<<%s, %s, %s" % (self.command, self.value, i)
				if self.mergeconflict:
						t += ", %s" % str(self.mergeconflict)
				t += ">>"
				return t

def EC2list(list_of_ecs):
		e = []
		for i in list_of_ecs:
				# If this fails, TODO
				# Will fail when trying to apply a ModelDifference
				# with MergeConflicts
				assert(i.mergeconflict == [])

				if isinstance(i, ElementSingleAssociationChange):
						e.append((i.command, i.frm or 0, i.to or 0))

				elif isinstance(i, ElementChange):
						e.append((i.command, i.value, i.index))

				elif isinstance(i, ElementAttributeChange):
						#assert(i.frm != None)
						#assert(i.to != None)
						if i.frm == None:
								i.frm = 0
						if i.to == None:
								i.to = 0
						e.append((i.command, i.frm, i.to))

		return e

class ElementDifference:
		"""ElementDifference descibes the difference between two elements.
		You can take the difference and apply it later to an element, even
		in reverse."""
		def __init__(self, element1, element2 = None, model1_elems = None, model2_elems = None):
				if element2:
						assert(isinstance(element1, MetaMM.MMClass))
						assert(isinstance(element2, MetaMM.MMClass))
						self.element_type = element1.__name__
						change_xmiid, change_type, element_editscripts = compare_two_elements(element1, element2, cmpkind__FullResults, model1_elems, model2_elems)
						self.change_xmiid = change_xmiid
						self.change_type = change_type
						self.element_editscripts = element_editscripts
				else:
						self.decanonify(element1)

		def __str__(self):
				t = "Element type: " + str(self.element_type) + "\n" + \
						"Change type:	" + str(self.change_type)	+ "\n" + \
						"Change ID:		" + str(self.change_xmiid) + "\n"

				t += "Editscripts:\n"
				for i in self.element_editscripts.keys():
						t += "\t" + i + ":\n"
						for e in self.element_editscripts[i]:
								t += "\t\t" + str(e) + "\n"
				return t

		def canonify(self):
				t1 = map(lambda x: (x, EC2list(self.element_editscripts[x])), self.element_editscripts)
				return (self.element_type, self.change_xmiid or 0, self.change_type or 0, t1)

		def decanonify(self, canonified):
				self.element_type, self.change_xmiid, self.change_type, t1 = canonified
				# Stupid marshalling
				if not self.change_xmiid:
						self.change_xmiid = None
				if not self.change_type:
						self.change_type = None
				
				self.element_editscripts = {}

				for (key, value) in t1:
						print "VAL", value
						e = []
						for v in value:
								if v[0] == change_one_association:
										e.append(apply(ElementSingleAssociationChange, v))
								elif v[0] == change_attribute_command:
										e.append(apply(ElementAttributeChange, v))
								else:
										e.append(apply(ElementChange, v))
						self.element_editscripts[key] = e

		def isEmpty(self):
				"""Returns true if there is no change in this ElementDifference."""
				return self.change_xmiid == None and self.change_type == None and self.element_editscripts == {}

		def remove(self, ec):
				for key in self.element_editscripts.keys():
						i = self.element_editscripts[key]
						if ec in i:
								i.remove(ec)
								if not self.element_editscripts[key]:
										del self.element_editscripts[key]
								break

		def patch(self, element, model_uuids, reverse = 0):
				"""Patches a new element with the difference created
				previously. If reverse is true, assumes this to be a 'reverse
				patch' and apply it in reverse. model_uuids is the uuid => element
				mapping of a model's elements, which are used to connect our
				patched element to the rest of the world."""
				ins_cmd = insert_command
				del_cmd = delete_command
				if reverse:
						ins_cmd, del_cmd = del_cmd, ins_cmd

				# Change type if necessary. This most certainly has BUGS.
				kept_element = 0
				if self.change_type:
						c1, c2 = self.change_type[1], self.change_type[2]
						if reverse:
								c1,c2 = c2,c1
						assert(c1 == element.__name__)
						new_elem = element.getMetamodel().__dict__[c2]()
						# Must reset
						new_elem.__resetattrs__()
						assert(new_elem.__XMIid__() != element.__XMIid__())
						new_elem.__uniqueID__ = element.__XMIid__()
						# Changing types most likely doesn't work
						assert(0)
				else:
						#new_elem = copy.copy(element)
						new_elem = element
						kept_element = 1

				assert(new_elem.__XMIid__() == element.__XMIid__())
				if not kept_element:
						assert(new_elem != element)

				# Change XMI id if necessary. This has bugs...
				if self.change_xmiid:
						assert(0)
						# BUG what should model_uuids[old_unique] point to???
						frm, to = self.change_xmiid[1], self.change_xmiid[2]
						if reverse:
								frm, to = to, frm
						assert(frm == element.__XMIid__())
						# Extremely important so we always point to the _new_ element
						model_uuids[new_elem.__XMIid__()] = new_elem
						new_elem.__uniqueID__ = to
						assert(kept_element or new_elem.__XMIid__() != element.__XMIid__())
						# Delete the old connection
						if not kept_element:
								del model_uuids[element.__XMIid__()]
						

				####model_uuids[new_elem.__XMIid__()] = new_elem

				# Edit attributes
				for key in self.element_editscripts.keys():
						# Skip all but attributes
						if not element.__mm__[key][0] == MMClass.kind__Attribute:
								continue

						ec = self.element_editscripts[key][0]
						cmd, frm, to = ec.command, ec.frm, ec.to
						print "CHANGE"
						print key,frm,to
						assert(cmd == change_attribute_command)
						if reverse:
								frm, to = to, frm
						print element, element.__XMIid__(), key, self.element_editscripts[key]
						# Note that the other end doesn't update for attributes,
						# so setattr and set_children are ok.

						# Needed when changing types
						if not new_elem.__mm__.has_key(key):
								assert(to == None)
								continue

						if not issubclass(new_elem.__mm__[key][1], MetaMM.MMDataType):
								if to == None:
										setattr(new_elem, key, None)
								else:
										setattr(new_elem, key, model_uuids[to])
						else:
								setattr(new_elem, key, to)
						print "SETATTR"
						print new_elem, key, to

				# Fix so everybody points to new_elem instead of element
				# This is done _before_ myers
				# THIS MAY CONTAIN BUGS, as it is not an exercised
				# code path at the moment
				if not kept_element:
						assert(0)
						for key in element.__mm__.keys():
								# Fix the other ends, they point to the old element
								children = MetaMM.get_children(element, key)
								if children:
										print "********** argh", new_elem, key, children
				
								for child in children:
										for childkey in child.__mm__.keys():
												otherchildren = MetaMM.get_children(child, childkey)
												if otherchildren:
														print "********** otherargh", child, childkey, otherchildren
												if child.__mm__[childkey][2] == 1:
														if child.__dict__[childkey] == element:
																child.__dict__[childkey] = new_elem
												else:
														for i in range(len(otherchildren.items)):
																if otherchildren.items[i] == element:
																		otherchildren.items[i] = new_elem
												otherchildren = MetaMM.get_children(child, childkey)
												if otherchildren:
														print "********** otherargh", child, childkey, otherchildren

				# Edit associations
				print "-------"
				print new_elem
				others = {}
				for key in self.element_editscripts.keys():
						# Skip attributes
						if element.__mm__[key][0] == MMClass.kind__Attribute:
								continue
						
						editscript = self.element_editscripts[key]
						if element.__mm__[key][2] == 1:
								assert(len(editscript) <= 1)
								cmd, frm, to = editscript[0].command, editscript[0].frm, editscript[0].to
								if reverse:
										frm, to = to, frm
								assert(cmd == change_one_association)
								old = getattr(element, key)
								if old:
										old = old.__XMIid__()
								if to:
										to = model_uuids[to]
								assert(old == frm)
								print "SETTING ", element.__XMIid__(), key, to
								element.__dict__[key] = to
								continue
						
						children = MetaMM.get_children(element, key)
						old_uuids = map(lambda x: x.__XMIid__(), children)
						print
						print "myers_patch"
						print "invalidate", element, element.__XMIid__()
						print key
						print "OLD ", old_uuids
						print editscript, reverse, {"children": map(lambda x: x.__XMIid__(), children), "element": new_elem, "assoc": key, "model_uuids": model_uuids }
						myers_patch(EC2list(editscript), old_uuids, reverse, __special_mof_patch_func__, {"children": children, "element": new_elem, "assoc": key, "model_uuids": model_uuids })
						print "NEW ", map(lambda x: x.__XMIid__(), MetaMM.get_children(element, key))
						print
										
				return new_elem

##def asciify_element(element):
##		"""Creates a tuple describing the element and its connections using
##		XMIids, not pointers. Empty children are not listed, for compactness."""
##		result = []
##		for key in element.__mm__.keys():
##				value = MetaMM.getValue(element, key)
##				if not issubclass(element.__mm__[key][1], MetaMM.MMDataType):
##						continue
##				if type(value) == types.InstanceType or type(value) == list:
##						assert(0)
##						value = map(lambda x: x.__XMIid__(), value)
##				if value:
##						result.append((key, value))
##		return (element.__XMIid__(), element.__name__, result)

##def deasciify_element(element, model_elements, listofkeyvals):
##		"""From a list of attributes, recreates the attributes of
##		an empty element."""
##		for (key, value) in listofkeyvals:
##				if not issubclass(element.__mm__[key][1], MetaMM.MMDataType):
##						continue
##				print "deasciify SETATTR"
##				print element, element.__XMIid__(), key, value, type(value)
##				#if issubclass(element.__mm__[key][1], MetaMM.MMUnlimitedInteger):
##				#		value = int(value)
##				setattr(element, key, value)

class ModelChange:
		def __init__(self, command, value, type):
				self.command = command
				self.type = type
				self.value = value

		def __str__(self):
				if self.command == insert_command:
						return "\tCreate " + self.type + " with id " + self.value + "\n"
				elif self.command == delete_command:
						return "\tDelete " + self.type + " with id " + self.value + "\n"

		def canonify(self):
				return self.command, self.type, self.value

class ModelDifference:
		"""ModelDifference describes the differences between
		two/three(?) models. Basically it consists of several
		ElementDifferences."""
		def __init__(self, model1, model2 = None):
				self.model_changes = []
				self.element_differences = []
				self.old_root = None
				self.new_root = None
				self.mergeconflicts = []

				self.is_diff3 = 0

				if model2:
						assert(model1.__module__ == model2.__module__)
						self.metamodel_name = model1.__module__
						self.compare_two_models(model1, model2)
				else:
						self.decanonify(model1)

		def __str__(self):
				t = "----------------------------------------------------------------------\n" + \
						"Metamodel:		" + str(self.metamodel_name) + "\n" + \
						"Old Root element: " + str(self.old_root) + "\n" + \
						"New Root element: " + str(self.new_root) + "\n" + \
						"Changes:\n"
				for i in self.model_changes:
						t += str(i)
				t += "Differences:\n\n"
				for (uuid, ed) in self.element_differences:
						t += "[" + uuid + "]" + "\n" + str(ed) + "\n"
				t += "----------------------------------------------------------------------\n"
				return t

		def canonify(self):
				"""Returns the canonical form of a model difference, for
				XML-RPC operations."""
				t2 = map(lambda x: x.canonify(), self.model_changes)
				t3 = map(lambda x: (x[0], x[1].canonify()), self.element_differences)
				return [ self.old_root, self.new_root, self.metamodel_name, self.is_diff3, t2, t3 ]

		def decanonify(self, canonified):
				self.old_root, self.new_root, self.metamodel_name, self.is_diff3, t2, t3 = canonified

				for (command, type, value) in t2:
						self.model_changes.append(ModelChange(command, value, type))

				for (key, value) in t3:
						self.element_differences.append((key, ElementDifference(value)))

		def cleanup(self, MD_B):
				"""Delete empty hashes and array elements.
				Removes deletions from self which MD_B already deletes,
				if there are no changes for the element."""
		
				del_ediffs = []

				for (d_uuid, d_elemdiff) in self.element_differences:
						for d_key in d_elemdiff.element_editscripts.keys():
								if len(d_elemdiff.element_editscripts[d_key]) == 0:
										del d_elemdiff.element_editscripts[d_key]
						if len(d_elemdiff.element_editscripts) == 0:
								print "DEL", d_uuid
								del_ediffs.append((d_uuid, d_elemdiff))

				del_modelchanges = []
				
				for i in del_ediffs:
						self.element_differences.remove(i)
						for modelchange in self.model_changes:
								if modelchange.value == i[0]:
										for modelchange_B in MD_B.model_changes:
												if modelchange_B.value == i[0]:
														# Both must be deletions, how else
														# could they have the same uuid???!
														# Oh bugger, some luser could play with
														# modules.
														if (modelchange.command != delete_command or modelchange_B.command != delete_command):
																logger.warning("Both modelchanges add the same element! Continuing anyway, let's hope it is OK.")
														del_modelchanges.append(modelchange)
														break
										break

				for i in del_modelchanges:
						self.model_changes.remove(i)

		def isEmpty(self):
				return self.model_changes == [] and self.element_differences == []

		def dropMergeConflict(self, mc):
				"""Drops the given MergeConflict."""
				self.mergeconflicts.remove(mc)

		def updateMergeConflicts(self):
				mcs = []
				for (d_uuid, d_elemdiff) in self.element_differences:
						for d_key in d_elemdiff.element_editscripts.keys():
								for ec in d_elemdiff.element_editscripts[d_key]:
										if ec.hasMergeConflicts():
												mcs.extend(ec.mergeconflict)

				self.mergeconflicts = mcs
		
		def compare_two_models(self, model1, model2):
				"""Compares all elements in two models, returning a structure
				of the differences."""
				model_changes = []
				element_differences = []

				model1_elements = MetaMM.getElementsOfModel(model1)
				model2_elements = MetaMM.getElementsOfModel(model2)

				#
				# * First we add or delete any elements not in both models
				# * Then we compare the common elements
				#

				for i in model2_elements.keys():
						if model1_elements.has_key(i):
								assert(model2_elements[i] != model1_elements[i])
				for i in model1_elements.keys():
						if model2_elements.has_key(i):
								assert(model1_elements[i] != model2_elements[i])

				
				# New in model 2, removed in model 1?
				for i in model2_elements.keys():
						if not model1_elements.has_key(i):
								# Element i is new in 2, or removed in 1
								# Insert the whole element
								model_changes.append(ModelChange(insert_command, i, model2_elements[i].__name__))
								# Create empty element
								new_elem = model2_elements[i].__class__()
								# Must reset
								new_elem.__resetattrs__()
								#assert(i == model2_elements[i].__uniqueID__)
								new_elem.__uniqueID__ = i

								assert(not model1_elements.has_key(i))
								print "CREATED", i
								model1_elements[i] = new_elem

				# New in model 1, removed in model 2?
				for i in model1_elements.keys():
						if not model2_elements.has_key(i):
								# Create an empty element here
								# The created ElementDifference will "drop" the element later
								new_elem =	model1_elements[i].__class__()
								# Must reset, otherwise Knuth^WGod only knows what elements
								# actually are created
								new_elem.__resetattrs__()
								new_elem.__uniqueID__ = i
								assert(not model2_elements.has_key(i))
								print "CREATED", i
								model2_elements[i] = new_elem
								# We need to notify this however, for reverse patches.
								model_changes.append(ModelChange(delete_command, i, model1_elements[i].__name__))
								
				print
				print "MODEL CHANGES:"
				for i in model_changes:
						print i
				print
				print map(lambda x: x.__XMIid__(), model1_elements.values())
				print
				print map(lambda x: x.__XMIid__(), model2_elements.values())
				print

				for i in model1_elements.keys():
						assert(model2_elements.has_key(i))
						elem_diff = ElementDifference(model1_elements[i], model2_elements[i], model1_elements, model2_elements)

						assert(not elem_diff.change_xmiid)

						# Don't include empty differences
						if not elem_diff.isEmpty():
								print "ELEM_DIFF"
								print vars(elem_diff)
								print
								element_differences.append((i, elem_diff))

				print "DONE ELEM_DIFF"
				self.model_changes = model_changes
				self.element_differences = element_differences
				self.old_root = model1.__XMIid__()
				self.new_root = model2.__XMIid__()

				print "model changes"
				for i in model_changes:
						print vars(i)
				print "element differences"
				#
				# Fix so elementchanges now which ModelDifference they are in
				#
				for (uuid, ediff) in element_differences:
						for ec in ediff.element_editscripts.values():
								for echange in ec:
										echange.modeldifference = self

						print uuid, ediff
				print

		def getOldRoot(self):
				return self.old_root

		def getNewRoot(self):
				return self.new_root

		def patch3(self, model, reverse = 0):
				"""Patches a model according to the diff3-modified ModelDifference.
				Set reverse if you want to undo a previous patch3."""
				# Trivial, since all the work has been done by diff3.
				assert(self.is_diff3 == 1)
				return self.__patch__(model, reverse)

		def patch(self, model, reverse = 0):
				assert(self.is_diff3 == 0)
				return self.__patch__(model, reverse)
		
		def __patch__(self, model, reverse):
				"""Patches the model with the difference created previously.
				If reverse is true, assume this to be a 'reverse patch' and
				apply it in reverse."""
				if self.mergeconflicts:
						raise CantPatchWithMergeConflicts

				model_elements = MetaMM.getElementsOfModel(model)

				ins_cmd, del_cmd = insert_command, delete_command
				if reverse:
						ins_cmd, del_cmd = del_cmd, ins_cmd
						#assert(0)

				# Model changes, i.e. addition/removal of elements

				# First, create all the elements but don't do anything about
				# their attributes and associations
				print self.model_changes
				model_changes = copy.copy(self.model_changes)
				if reverse:
						model_changes.reverse()
				for mc in self.model_changes:
						cmd, uuid, elemname = mc.command, mc.value, mc.type
						if cmd == ins_cmd:
								new_elem = model.getMetamodel().__dict__[elemname]()
								# Must reset
								new_elem.__resetattrs__()
								new_elem.__uniqueID__ = uuid

								assert(not model_elements.has_key(uuid))
								model_elements[uuid] = new_elem

								print "NEW", new_elem, new_elem.__uniqueID__
								print vars(new_elem)
								
				# Do the editscripts
				element_differences = copy.copy(self.element_differences)

				if reverse:
						element_differences.reverse()

				for (uuid, ed) in element_differences:
						new_elem = ed.patch(model_elements[uuid], model_elements, reverse)

				# Delete unwanted elements
				for mc in self.model_changes:
						cmd, uuid, elemname = mc.command, mc.value, mc.type
						if cmd == del_cmd:
								## Unnecessary
								# resetattrs(model1_elements[value[0]])
								del model_elements[uuid]


				if reverse:
						root = self.old_root
				else:
						root = self.new_root

				assert(root)
				assert(model_elements.has_key(root))
				return model_elements[root]


#
#
#
#
#
#
#
# EVERYTHING BELOW THIS LINE IS B0RKEN!
#
#
#
#
#
#
#
#

		
#### MERGE ALGORITHM
#
#def remove_uuid(elements, uuid):
#		"""Removes uuid from the elements"""
#		pass
#
#def remove_connection(elements, uuid_from, key, uuid_to):
#		"""Removes a connection from uuid_from to uuid_to, in the
#		key association/composition. NOTE: the element uuid_to
#		is not removed, since it may be referenced otherwise.
#		This will hopefully not lead to any trouble, as e.g. saving the
#		model is done recursively trough the top-level model later."""
#		children = MetaMM.get_children(elements[uuid_from], key)
#		for i in children:
#				if i.__XMIid__() == uuid_to:
#						children.remove(i)
#
#		MetaMM.set_children(elements[uuid_from], key, children)
#
#def __create__(elements, elem):
#		"""Create a copy of elem if not found in elements, and
#		recursively do this for all the associations."""
#		uuid = elem.__XMIid__()
#		if elements.has_key(uuid):
#				return elements[uuid]
#		# Create a new copy of elem
#		# Note that the only real usage is the copying
#		# of simple primitive keys...
#		e = copy.copy(elem)
#		elements[uuid] = e
#		for key in e.__mm__.keys():
#				assocs = MetaMM.get_children(e, key)
#				children = []
#				for child in assocs:
#						newchild = __create__(elements, child)
#						children.append(newchild)
#				if assocs:
#						# Note that the above check nicely skips
#						# the simple primitive keys like name etc.
#						MetaMM.set_children(e, key, children)
#
#		return e
#
#def add_connection(elements, uuid_from, key, elem_to):
#		"""Adds a connection between uuid_from to a copy of elem,
#		and recursively adds new things."""
#		uuid_to = elem_to.__XMIid__()
#		print "Add %s - %s - %s" % (uuid_from, key, uuid_to)
#		assert(elements.has_key(uuid_from))
#		elem_to = __create__(elements, elem_to)
#		# Now add elemto
#		children = MetaMM.get_children(elements[uuid_from], key)
#		children.append(elem_to)
#		MetaMM.set_children(elements[uuid_from], key, children)
#
#def compare_and_fix(only_in_element1, only_in_element2, different_attributes, new1, new2, elements1, elements2, commonelements, joinelems):
#		print "COMPARE AND FIX"
#		print "only 1"
#		print only_in_element1
#		print "only 2"
#		print only_in_element2
#		print "diff attrs"
#		print different_attributes
#		print
#		print "New 1"
#		print new1
#		print "New 2"
#		print new2
#		print "Elements 1"
#		print elements1
#		print "Elements 2"
#		print elements2
#		print "The common model is"
#		print commonelements
#		# Add new elements
#		print "THE FIX IS"
#		# These really shouldn't matter
#		# Everything comes up in only_in_element[12]
#		# And the routine later on (N/A)
#
#		print "BEFORE"
#		print joinelems
#
#		del_this = []
#		for uuid in new1:
#				if commonelements.has_key(uuid):
#						# This was removed in the elem2 branch,
#						# lets' keep it that way in the join
#						print "1. Do not keep %s" % uuid
#						# Remove it from the join
#						remove_uuid(joinelems, uuid)
#				else:
#						# This was added in elem1 branch
#						# Let's add it in the join
#						print "1. Keep %s" % uuid
#						# Do nothing, already in join
#				del_this.append(uuid)
#		for uuid in del_this:
#				del new1[uuid]
#
#		del_this = []
#		for uuid in new2:
#				if commonelements.has_key(uuid):
#						# This was removed in the elem1 branch,
#						# lets' keep it that way in the join
#						print "2. Do not keep %s" % uuid
#						# Do nothing, already removed in join
#				else:
#						# This was added in elem2 branch
#						# Let's add it in the join
#						print "2. Keep %s" % uuid
#						# Do nothing, it will be added later on
#				del_this.append(uuid)
#		for uuid in del_this:
#				del new2[uuid]
#
#		del_this = []
#		# Compare associations
#		for uuid in only_in_element1.keys():
#				assert(elements2[uuid])
#				assert(commonelements[uuid])
#				# These associations are in elem1 only
#				associations = only_in_element1[uuid]
#				for key in associations.keys():
#						add_links = associations[key]
#						other_ass = MetaMM.get_children(elements2[uuid], key)
#						common_ass = MetaMM.get_children(commonelements[uuid], key)
#						for child in add_links:
#								if child in other_ass:
#										# Already in the other element, ok
#										print "1. Already, keep %s - %s - %s" % (uuid, key, child)
#								elif child in common_ass:
#										# Was removed in other element
#										print "1. Remove %s - %s - %s" % (uuid, key, child)
#										remove_connection(joinelems, uuid, key, child)
#								else:
#										print "1. New, keep %s - %s - %s" % (uuid, key, child)
#										add_connection(joinelems, uuid, key, elements1[child])
#				del_this.append(uuid)
#		for uuid in del_this:
#				del only_in_element1[uuid]
#				
#		del_this = []
#		for uuid in only_in_element2.keys():
#				assert(elements1[uuid])
#				assert(commonelements[uuid])
#				# These associations are in elem1 only
#				associations = only_in_element2[uuid]
#				for key in associations.keys():
#						add_links = associations[key]
#						other_ass = MetaMM.get_children(elements1[uuid], key)
#						common_ass = MetaMM.get_children(commonelements[uuid], key)
#						for child in add_links:
#								if child in other_ass:
#										# Already in the other element, ok
#										print "2. Already, keep %s - %s - %s" % (uuid, key, child)
#								elif child in common_ass:
#										# Was removed in other element
#										print "2. Remove %s - %s - %s" % (uuid, key, child)
#										remove_connection(joinelems, uuid, key, child)
#								else:
#										print "2. New, keep %s - %s - %s" % (uuid, key, child)
#										add_connection(joinelems, uuid, key, elements2[child])
#				del_this.append(uuid)
#		for uuid in del_this:
#				del only_in_element2[uuid]
#
#		print "ATTRIBS"
#		del_this = []
#		for uuid in different_attributes.keys():
#				assert(elements1[uuid])
#				assert(elements2[uuid])
#				# This uuid isn't in the common tag?
#				if not uuid in commonelements:
#						continue
#				if not uuid in joinelems:
#						assert(0)
#						continue
#				for key in different_attributes[uuid]:
#						if issubclass(elements1[uuid].__mm__[key][1], MetaMM.MMDataType):
#								if getattr(elements1[uuid], key) == getattr(commonelements[uuid], key):
#										# Take it from elements2
#										joinelems[uuid].__setattr__(key, getattr(elements2[uuid], key))
#										del_this.append((uuid, key))
#										print "Change %s - %s from %s to %s" % (uuid, key, getattr(elements1[uuid], key), getattr(elements2[uuid], key))
#								elif getattr(elements2[uuid], key) == getattr(commonelements[uuid], key):
#										# Take it from elements1
#										joinelems[uuid].__setattr__(key, getattr(elements1[uuid], key))
#										del_this.append((uuid, key))
#										print "Change %s - %s from %s to %s" % (uuid, key, getattr(elements2[uuid], key), getattr(elements1[uuid], key))
#								else:
#										# Both different to the common element, CONFLICT
#										print "CONFLICT at uuid %s, attribute %s" % (uuid, key)
#						else:
#								if getattr(elements1[uuid], key).__XMIid__() == getattr(commonelements[uuid], key).__XMIid__():
#										# Take it from elements2
#										o = getattr(elements2[uuid], key).__XMIid__()
#										for i in joinelems.keys():
#												if i.__XMIid__() == o:
#														joinelems[uuid].__setattr__(key, i)
#														break
#										del_this.append((uuid, key))
#										print "Change %s - %s from %s to %s" % (uuid, key, getattr(elements1[uuid], key).__XMIid__(), getattr(elements2[uuid], key).__XMIid__())
#								elif getattr(elements2[uuid], key).__XMIid__() == getattr(commonelements[uuid], key).__XMIid__():
#										# Take it from elements1
#										o = getattr(elements1[uuid], key).__XMIid__()
#										for i in joinelems.keys():
#												if i.__XMIid__() == o:
#														joinelems[uuid].__setattr__(key, i)
#														break
#										del_this.append((uuid, key))
#										print "Change %s - %s from %s to %s" % (uuid, key, getattr(elements2[uuid].__XMIid__(), key), getattr(elements1[uuid], key).__XMIid__())
#								else:
#										# Both different to the common element, CONFLICT
#										print "CONFLICT at uuid %s, attribute %s" % (uuid, key)
#		for (uuid, key) in del_this:
#				del different_attributes[uuid][key]
#		for uuid in different_attributes.keys():
#				if len(different_attributes[uuid]) == 0:
#						del different_attributes[uuid]
#								
#		print "AFTER"
#		print joinelems
#		print "WHAT IS LEFT"
#		print only_in_element1
#		print only_in_element2
#		print different_attributes
#		print "READY FIXING"
#		for i in elements1.values():
#				print i
#		for i in elements2.values():
#				print i
#				
#		for i in joinelems:
#				print
#				print i
#				print joinelems[i]
#				print joinelems[i].__dict__
#		print
#		print
#		print
#		
#
