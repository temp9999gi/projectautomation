###########################################################################
#																																				 #
# C O P Y R I G H T	 N O T I C E																				 #
#	Copyright (c) 2001 by:																								 #
#		* California Institute of Technology																 #
#																																				 #
#		All Rights Reserved.																								 #
#																																				 #
# Permission is hereby granted, free of charge, to any person						 #
# obtaining a copy of this software and associated documentation files		#
# (the "Software"), to deal in the Software without restriction,					#
# including without limitation the rights to use, copy, modify, merge,		#
# publish, distribute, sublicense, and/or sell copies of the Software,		#
# and to permit persons to whom the Software is furnished to do so,			 #
# subject to the following conditions:																		#
#																																				 #
# The above copyright notice and this permission notice shall be					#
# included in all copies or substantial portions of the Software.				 #
#																																				 #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,				 #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF			#
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND									 #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS		 #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN			#
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN			 #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE				#
# SOFTWARE.																															 #
###########################################################################
#
#			 Authors: Diane Trout
# Last Modified: $Date: 2007/01/01 13:36:53 $
# $Revision: 1.1 $
#
from __future__ import nested_scopes

import imp
import os
import pprint
import re
import string
import sys
import types
import traceback

import psycopg as db_api
#import pgdb as db_api

import fkeyTypes
from bool import Bool

from mx import DateTime
from mx.DateTime.Parser import DateTimeFromString

import warnings
from warnings import warn

class DebugWarning(Warning):
	pass
warnings.filterwarnings('ignore', category=DebugWarning, append=1)

class Functor:
	"""Predefine some arguments for a function.

	e.g.
	def Foo(a,b,c):
		print a
		print b
		print c

	Bar = Functor(Foo, "alpha", "beta")

	Bar("delta")
	alpha
	beta
	delta
	"""
	def __init__(self, function, *args, **kargs):
		assert callable(function), "function should be a callable obj"
		self._function = function
		self._args = args
		self._kargs = kargs
		
	def __call__(self, *args, **kargs):
		"""call function"""
		_args = list(self._args)
		_args.extend(args)
		_kargs = self._kargs.copy()
		_kargs.update(kargs)
		return apply(self._function,_args,_kargs)			

def reloadModuleList(module_list):
	"""Reload all modules in provided list

	This support function is used to create moduleReload
	which is needed to reimport an API so the test code can create
	different versions of the same API.

	it would also be useful if you modified some modules within an
	interpreter session.
	"""
	# if we're being reinitialized reload all of our modules
	for module in module_list:
		if sys.modules.has_key(module.__name__):
			#print "reloading module %s" % (module.__name__)
			reload(module)
				
def sqlEscapeString(s):
	"""Given a string escape any double quote marks \"
	"""
	if type(s) == types.StringType or type(s) == types.UnicodeType:
		s = re.sub('"', '\\\"', s)
		s = re.sub("'", "\\\'", s)
		return s
	else:
		return s

class DBSessionImpl:
	"""Implementation code for managing a database session.

	For this to be useful you should derive from it and make sure that
	loadClasses is called with a list if classes to be attached to this
	session.

	e.g.
	class DBsession(DBSsessionImpl):
		def __init__(self, dsn=None, database=None, user=None, password=None):
			classes_to_load = [('class', package.module.class)]
	
			DBSessionImpl.__init__(self, dsn, database, user, password)
			self.loadClasses(classes_to_load)
			self.connect()
	"""

	default_host = "localhost"
	try:
		default_user = os.getlogin()
	except:
		default_user = None
	default_database = ""
	default_password=None
	
	def __init__(self, host=None, database=None, user=None, password=None):
		if host is None:
			self.host = os.environ.get('DBHOST', DBSessionImpl.default_dsn)
		else:
			self.host = host
		if database is None:
			self.database = os.environ.get('DBDATABASE', DBSessionImpl.default_database)
		else:
			self.database = database
		if user is None:
			self.user = os.environ.get('DBUSER', DBSessionImpl.default_user)
		else:
			self.user = user
		if password is None:
			self.password = os.environ.get('DBPASSWORD', DBSessionImpl.default_password)
		else:
			self.password = password

		# object pointing to the low level database api
		self.db = None

		# class references is used to lookup the table class variable information
		# in getObjects and getAllObjects
		self.class_references = {}
		

	def __del__(self):
		if self.db is not None:
			self.db.close()

	#############################
	# Database session management
	def connect(self):
		if self.db is None:
			dsn = []
			if self.host is not None: dsn += ["host=%s" % (self.host)]
			if self.database is not None: dsn += ["dbname=%s" % (self.database)]
			if self.user is not None: dsn += ["user=%s" % (self.user)]
			if self.password is not None: dsn += ["password=%s" % (self.password)]
			dsn=string.join(dsn)
			self.db = db_api.connect(dsn=dsn, serialize=0)
			
	def cursor(self):
		#if self.db is None:
		#	self.connect()
		return self.db.cursor()

	def rollback(self):
		if self.db is not None:
			self.db.rollback()

	def commit(self):
		if self.db is not None:
			self.db.commit()

	def close(self):
		if self.db is not None:
			self.db.close()


	############################
	# attribute access
	def loadClasses(self, module_list):
		for className, classRef in module_list:
			# construct arguments for functor
			_args = [classRef]
			kargs = {'db_session': self}

			# create class factory application function
			functor = apply(Functor, _args, kargs)

			# store reference to class reference, so we can
			# get access to the class variables when doing
			# certain types of lookups. (Yes this seems icky)
			self.class_references[functor] = classRef
			
			# add constructor to our class object
			setattr(self, className, functor)

		return
		for m in module_list:
			self.__loadClass(m)
			

	def __getClassRef(self, class_functor):
		"""Given a class or class factory reference return a class reference
		"""
		
		if type(class_functor) == types.ClassType:
			class_ref = class_functor
		elif isinstance(class_functor, Functor):
			class_ref = self.class_references[class_functor]
		else:
			raise ValueError("unrecognized class type")

		return class_ref


	def createTransactionManager(self):
		return TransactionManager(self)
	
	
	def getObjects(self, class_functor, keys):
		"""Returns a list of objects from a list of primary keys.
		"""
		if keys is None or len(keys) == 0:
			# FIXME: Should this raise an error instead?
			return None
		
		class_ref = self.__getClassRef(class_functor)
		class_inst = class_ref()
		
		sql = "SELECT * FROM \"%s\" where \"%s\" in (" % (
			class_ref.table_name,
			class_inst.getPrimaryKeyName())
		sql += keys[0]
		for k in keys[1:]:
			sql += ", %s" % (k)
		sql += ")"
	
		return self.loadRecords(class_ref, sql)
	
	def getAllObjects(self, class_functor):
		"""Return all records of type class_ref as a list.
		"""
		class_ref = self.__getClassRef(class_functor)
		
		sql = "SELECT * FROM \"%s\"" % (class_ref.table_name)
		return self.loadRecords(class_ref, sql)

	def getObjectsWhere(self, class_functor, where_clause):
		"""Returns all records of type class ref that matches the sql where expr.
		"""
		class_ref = self.__getClassRef(class_functor)
		
		sql = "SELECT * FROM \"%s\" where %s" % (class_ref.table_name, where_clause)
		return self.loadRecords(class_ref, sql)

	def getObjectsBySearch(self, class_functor, search, attribute=None):
		"""Returns all records of type class ref that contains a subset of ANY of the attributes
		of a class, if attribute=None, or it only searchs the attribute specified by the user.
		IF attribute is a list, it only searchs the attribute from the list.
		"""
		class_ref = self.__getClassRef(class_functor)

		class_inst = class_ref()

		if attribute is None:
			#Construct search ALL attribute where clause
			where_clause = ''
			for key in class_inst.fields.keys():
				where_clause += 'upper(%s) LIKE \'%%%s%%\' OR ' % (key, search.upper())
			#Remove last OR
			where_clause = where_clause[:-4]
		elif type(attribute) is types.StringType and class_inst.fields.has_key(attribute):
			#Construct search for single attribute
			where_clause = 'upper(%s) LIKE \'%%%s%%\'' % (attribute, search.upper())
		elif type(attribute) is types.ListType and len(attribute) > 0:
			#Construct search ALL attribute where clause
			where_clause = ''
			for key in attribute:
				where_clause += 'upper(%s) LIKE \'%%%s%%\' OR ' % (key, search.upper())
			#Remove last OR
			where_clause = where_clause[:-4]
		else:
			#Provide instructive error if wrong attribute was choosen.
			msg = 'Attribute of \'%s\' not valid, try one of the following:\n' % (attribute)
			for key in class_inst.fields.keys():
				msg += '%s, ' % (key)
			msg = msg[:-2]
			raise ValueError, msg

		#sql statement
		sql = "SELECT * FROM \"%s\" WHERE %s" % (class_ref.table_name, where_clause)
		return self.loadRecords(class_ref, sql)
	

	def getObjectCount(self, class_functor):
		"""
		Returns the number of objects which exist for a given class
		"""
		class_ref = self.__getClassRef(class_functor)
		
		sql = "SELECT count(*) FROM \"%s\"" % (class_ref.table_name)
		 
		try:
			cursor = self.db.cursor()
			try:
				cursor.execute(sql)
				record = cursor.fetchone()
			finally:
				cursor.close()
		except Exception, e:
			# pgdb isn't too informative about exception
			sys.stderr.write(str(e))
			sys.stderr.write(os.linesep)
		
		return record[0]
		 
	def getObjectCountWhere(self, class_functor, where_clause):
		"""
		Returns the number of objects which exist for a given class,
		given a where clause.
		"""
		class_ref = self.__getClassRef(class_functor)
		
		sql = "SELECT count(*) FROM \"%s\" where %s" % (class_ref.table_name,
																												 where_clause)
		 
		try:
			cursor = self.db.cursor()
			try:
				cursor.execute(sql)
				record = cursor.fetchone()
			finally:
				cursor.close()
		except Exception, e:
			# pgdb isn't too informative about exception
			sys.stderr.write(str(e))
			sys.stderr.write(os.linesep)
		
		return record[0]

	def getObjectCountBySearch(self, class_functor, search, attribute=None):
		"""Returns all records of type class ref that contains a subset of ANY of the attributes
		of a class, if attribute=None, or it only searchs the attribute specified by the user.
		IF attribute is a list, it only searchs the attribute from the list.
		"""
		class_ref = self.__getClassRef(class_functor)

		class_inst = class_ref()

		if attribute is None:
			#Construct search ALL attribute where clause
			where_clause = ''
			for key in class_inst.fields.keys():
				where_clause += 'upper(%s) LIKE \'%%%s%%\' OR ' % (key, search.upper())
			#Remove last OR
			where_clause = where_clause[:-4]
		elif type(attribute) is types.StringType and class_inst.fields.has_key(attribute):
			#Construct search for single attribute
			where_clause = 'upper(%s) LIKE \'%%%s%%\'' % (attribute, search.upper())
		elif type(attribute) is types.ListType and len(attribute) > 0:
			#Construct search ALL attribute where clause
			where_clause = ''
			for key in attribute:
				where_clause += 'upper(%s) LIKE \'%%%s%%\' OR ' % (key, search.upper())
			#Remove last OR
			where_clause = where_clause[:-4]
		else:
			#Provide instructive error if wrong attribute was choosen.
			msg = 'Attribute of \'%s\' not valid, try one of the following:\n' (attribute)
			for key in class_inst.fields.keys():
				msg += '%s, ' % (key)
			msg = msg[:-2]
			raise ValueError, msg

		#sql statement
		sql = "SELECT count(*) FROM \"%s\" WHERE %s" % (class_ref.table_name, where_clause)
		try:
			cursor = self.db.cursor()
			try:
				cursor.execute(sql)
				record = cursor.fetchone()
			finally:
				cursor.close()
		except Exception, e:
			# pgdb isn't too informative about exception
			sys.stderr.write(str(e))
			sys.stderr.write(os.linesep)

		return record[0]

		
	def loadRecords(self, class_ref, sql):
		"""Returns a list of objects selected by an sql statement.
		
		Given a class_reference and an sql statement for each record returned
		bind the values to an object instantiated from the class_ref.
		"""
		objects = []
		try:
			cursor = self.db.cursor()
			try:
				cursor.execute(sql)
				
				record = cursor.fetchone()
				while record is not None:
					o = class_ref(db_session=self)
					# tag this object as having been loaded from the database
					o.loaded = 1
					o.bindFields(cursor.description, record)
					objects.append(o)
					record = cursor.fetchone()
			finally:
				cursor.close()
		except Exception, e:
			# pgdb isn't too informative about exception
			sys.stderr.write(str(e))
			sys.stderr.write(os.linesep)
		# DELETE CODE:
		#	self.rollback()
		#else:
		#	self.commit()
			
		return objects

class Field:
	"""Stores information about database fields.

	Including name, type, null, and a cached copy of the value.
	"""
	def __init__(self, name, type=None, friendlyName=None):
		self.name = name
		self.friendlyName = friendlyName
		self.type = type
		self.null_allowed = 1
		self.modified = 0
		self.value = None
		self.loaded_value = None

	def setValue(self, value, loading = 0):
		"""
		Sets the value of the field after checking to make sure the types
		are compatible.
		"""
		# FIXME: type checking needs work
		# FIXME: if self.type isn't none we can type check
		# FIXME: if value is none, 
		# FIXME:	 can we be null?
		# FIXME:	 if yes: skip remainder of type checking
		# FIXME:	 if no: throw error
		# FIXME: does values type match our 
		# FIXME:
		if self.type is not None:
			# check for null
			if value is None:
				if not self.null_allowed:
					error_msg = "Field %s must not be null" % ( self.name )
					raise ValueError(error_msg)
			# try to typecast datetime types
			elif self.type == DateTime.DateTimeType and (type(value) == types.StringType or type(value) == types.UnicodeType):
				value = DateTimeFromString(value)
			# FIXME: postgresql returns bigints for sequences
			# FIXME:	which breaks this type checking code
			# FIXME: I'm not sure this coercion is a good idea since
			# FIXME: it might cause size problems
			elif self.type == types.IntType and type(value) == types.LongType:
				pass
			# FIXME: the following code fragment was added 'cause it
			# FIXME: it seems that you can't add subclassed objects to
			# FIXME: things expecting their base classes.
			# FIXME: also changed advisor link from faculty to employee to try
			# FIXME: and create some inheritance.
			#elif self.type == types.ClassType and issubclass(value, self.type):
			#		pass
			elif type(self.type) == types.ClassType:
				# NOTE: if the class can't parse the passed in value it should
				# NOTE: throw the value error
				value = self.type(value)
			elif self.type != type(value):
				error_msg = "Incompatible type for field %s, expecting %s, got %s"
				error_msg = error_msg % (self.name,
																 str(self.type),
																 str(type(value)))
				raise ValueError(error_msg)
			# NOTE: this allows a class to be listed as a type
			
		if not loading:
			warn("modified %s to %s" % (self.name , str(value)), DebugWarning)
			self.modified = 1

		self.value = value

	def isModified(self):
		if self.modified:
			return 1
		else:
			return 0

	def isNotNull(self):
		return not self.null_allowed

	def __str__(self):
		return pprint.pformat(self.__dict__)

class DBAssociation:
	def __init__(self, thisObject, otherEndModule, otherEndHasFKey, otherEndMultiplicity):
		self.thisObject = thisObject
		self.otherEndMultiplicity = otherEndMultiplicity
		self.otherEndHasForeignKey = otherEndHasFKey
		self.otherEndModule = otherEndModule

		# FIXME: This probably needs to be converted to a weak reference
		self.loaded_objects = None
		self.appended_objects = []

	def __len__(self):
		count = 0
		if self.loaded_objects is not None:
			count += len(self.loaded_objects)
		count += len(self.appended_objects)
		return count

	def __loadObjects(self):
		sql = "SELECT * FROM \"%s\" WHERE \"%s\" = %s"

		if self.isLocalAssociation():
			m = '1'
			keyName = self.otherEndModule.getPrimaryKeyName()
			keyValue = self.thisObject.fields[self.otherEndModule.getForeignKeyName()].value
		else:
			m = '*'
			keyName = self.thisObject.getForeignKeyName()
			keyValue = self.thisObject.fields[self.thisObject.getPrimaryKeyName()].value

		tableName = sqlEscapeString(self.otherEndModule.getTableName())
		keyName = sqlEscapeString(keyName)
		keyValue = sqlEscapeString(keyValue)
		sql %= (tableName, keyName, keyValue)
		warn("__loadObjects{%s}: %s -> %s" % (m, sql, self.otherEndModule.getClassName()), DebugWarning)
		return self.thisObject.db_session.loadRecords(self.otherEndModule.getClass(), sql)
		
	def getObjects(self):
		if self.loaded_objects is None:
			self.loaded_objects = self.__loadObjects()
			
		return self.loaded_objects + self.appended_objects

	def setObjects(self, objects):
		"""Replace the current contents of this association with the provided set.
		"""
		if self.otherEndMultiplicity == fkeyTypes.OneToOne:
			# we want a singleton item
			if type(object) == types.ListType:
				raise ValueError("One to one links cannot be lists")
			self.appended_objects = [objects]
		else:
			# we want a list
			if type(object) != types.ListType:
				raise ValueError("Many to one links must be lists")
			self.appended_objects = objects

		# erase any loaded objects
		self.loaded_objects = []
		
	def appendObjects(self, object):
		if self.otherEndMultiplicity == fkeyTypes.OneToOne:
			if len(self) >= 1:
				msg = "One to one links cannot have more than one linked object"
				raise ValueError(msg)
		#if not isinstance(object, self.class_reference):
		elif type(object) != types.InstanceType:
			msg = "Requires class instance"
			raise ValueError(msg)
#		# FIXME: type checking is not working for subclasses
#		elif not issubclass(object.__class__, self.class_reference):
#			msg = "Got object [%s], was expecting [%s]"
#			msg %= (str(object.__class__), str(self.class_reference))
#							
#			raise ValueError(msg)
#		
		self.appended_objects.append(object)

	def commit(self, transactionManager, visited):
		"""Commits changes made to linked objects
		"""
		# FIXME: this probably isn't thread safe
		appended_objects = self.appended_objects
		self.appended_objects = []

		if self.loaded_objects is None:
			self.loaded_objects = appended_objects
		else:
			self.loaded_objects.extend(appended_objects)
			
		for object in self.loaded_objects:
			object.commit(transactionManager, visited)

	def getPrimaryKeys(self):
		keys = []
		if self.loaded_objects is None:
			return keys
		
		for object in self.loaded_objects:
			keys.append(object.id())
		return keys

	def isLocalAssociation(self):
		"""Attempt to determine if this class has the foreign key attribute
		"""
		# we have a self referential object
		return not self.otherEndHasForeignKey
		
	def updateLinks(self):
		if self.isLocalAssociation():
			warn("saving local %s" % (self.thisObject.getTableName()),
					 DebugWarning)
			# We are in the object containing the foreign key

			if len(self) > 1:
				warn("executing one to one code with too many choices", RuntimeWarning)
			elif len(self) == 0:
				warn("executing one to one code with no choices", RuntimeWarning)
				return
			
			m = '1'
			keyName = self.otherEndModule.getPrimaryKeyName()
			keyValue = self.loaded_objects[0].id()
			self.thisObject.fields[self.otherEndModule.getForeignKeyName()].setValue(keyValue)

			msg ='d[%s] = s[%s] = %s' % (self.thisObject.getClassName(), self.loaded_objects[0].getClassName(), str(keyValue))
			warn(msg, DebugWarning)

		else:
			warn("saving remote %s" % (self.thisObject.getTableName()),
					 DebugWarning)
			keyValue = self.thisObject.fields[self.thisObject.getPrimaryKeyName()].value
			# we're in the object that has the foreign key pointing to it.
			keyValue = self.thisObject.id()

			for object in self.appended_objects:
				object.fields[self.thisObject.getForeignKeyName()].setValue(keyValue)
				warn('d[%s] = s[%s] = %s' % (object.table_name, self.thisObject.table_name, str(keyValue)), DebugWarning)
			
			
class ForeignKey:
	"""Provides a method to follow a foreign key link to another DBClass.
	"""
	# FIXME: need to reduce the number of parameters here
	# FIXME: perhaps local table name and column can be determined from
	# FIXME: the link type and table reference.
	def __init__(self, column_id, local_table, foreign_table, pkey, type, table, class_reference):
		# Information about the foreign key
		self.column_id = column_id
		self.local_table = local_table
		self.foreign_table = foreign_table
		self.foreign_table_pkey = pkey
		self.fkey_type = type

		# information about the object we're embedded in
		self.table = table
		self.db_session = table.db_session
		self.class_reference = class_reference
		
		# FIXME: This probably needs to be converted to a weak reference
		self.loaded_objects = None
		self.appended_objects = []

	def __len__(self):
		count = 0
		if self.loaded_objects is not None:
			count += len(self.loaded_objects)
		count += len(self.appended_objects)
		return count
			
	def __loadObjects(self):
		sql = "SELECT * FROM \"%s\" WHERE \"%s\" = %s" 
		warn("load %s %s" % (self.table.table_name, self.local_table), DebugWarning)
		if self.table.table_name == self.local_table:
			# We are in the object 
			# select * from foreign_table where foreign_table_pkey = current.key
			from_table = self.foreign_table
			key_name = self.foreign_table_pkey
			key_value = self.table.fields[self.column_id].value
			
		else:
			# we're in the object that has the foreign key pointing to it.
			# select * from local_table where column_id = local_table.pkey
			from_table = self.local_table
			key_name = self.column_id
			key_value = self.table.id()
			
		if key_value is None:
			# can't lookup something that doesn't exist.
			# FIXME: how should I handle adding new objects to an object?
			return None

		from_table = sqlEscapeString(from_table)
		key_name = sqlEscapeString(key_name)
		
		sql = sql % (from_table, key_name, key_value)
		warn(sql, DebugWarning)

		return self.db_session.loadRecords(self.class_reference, sql)

	def getObjects(self):
		if self.loaded_objects is None:
			self.loaded_objects = self.__loadObjects()
			
		return self.loaded_objects + self.appended_objects

	def appendObjects(self, object):
		if self.fkey_type == fkeyTypes.OneToOne:
			if len(self) >= 1:
				msg = "One to one links cannot have more than one linked object"
				raise ValueError(msg)
		#if not isinstance(object, self.class_reference):
		elif type(object) != types.InstanceType:
			msg = "Requires class instance"
			raise ValueError(msg)
#		# FIXME: type checking is not working for subclasses
#		elif not issubclass(object.__class__, self.class_reference):
#			msg = "Got object [%s], was expecting [%s]"
#			msg %= (str(object.__class__), str(self.class_reference))
#							
#			raise ValueError(msg)
#		
		self.appended_objects.append(object)

	def commit(self, transactionManager, visited):
		"""Commits changes made to linked objects
		"""
		raise ValueError("foreign key commit was never called")
		
		# FIXME: this probably isn't thread safe
		appended_objects = self.appended_objects
		self.appended_objects = []

		if self.loaded_objects is None:
			self.loaded_objects = appended_objects
		else:
			self.loaded_objects.extend(appended_objects)
			
		for object in self.loaded_objects:
			object.commit(transactionManager, visited)

	def getPrimaryKeys(self):
		keys = []
		if self.loaded_objects is None:
			return keys
		
		for object in self.loaded_objects:
			keys.append(object.id())
		return keys

	def isLocalAssociation(self):
		"""Attempt to determine which class the key to update is in.
		"""
		# we have a self referential object
		if self.local_table == self.foreign_table:
			# this code is getting ugly
			if self.fkey_type == fkeyTypes.OneToOne:
				return 1
			else:
				return 0
		# the containing class is the local class
		elif self.table.table_name == self.local_table:
			return 1
		else:
			return 0
		
	def updateLinks(self):
		if self.isLocalAssociation():
		#if self.fkey_type == fkeyTypes.OneToOne:
			warn("saving local %s %s" % (self.table.table_name, self.local_table),
					 DebugWarning)
			# We are in the object containing the foreign key

			if len(self) > 1:
				warn("executing one to one code with too many choices", RuntimeWarning)
			elif len(self) == 0:
				warn("executing one to one code with no choices", RuntimeWarning)
				return

			key_value = self.loaded_objects[0].id()
			self.table.fields[self.column_id].setValue(key_value)
			warn('d[%s] = s[%s] = %s' % (self.table.table_name, self.loaded_objects[0].table_name, str(key_value)), DebugWarning)

		else:
			warn("saving remote %s %s" % (self.table.table_name, self.local_table),
					 DebugWarning)
			# we're in the object that has the foreign key pointing to it.
			key_value = self.table.id()

			for object in self.appended_objects:
				object.fields[self.column_id].setValue(key_value)
				warn('d[%s] = s[%s] = %s' % (object.table_name, self.table.table_name, str(key_value)), DebugWarning)
			
class DBClass:
	"""Base class for all the classes that are database backed.
	"""
	def __init__(self, db_session=None):
		self.loaded = 0

		# FIXME: I don't like this code, but it prevents a base class from
		# FIXME: reinitializing the list of fields & links back to null
		# FIXME: perhaps we should seperate the class information
		# FIXME: from the writer interface?
		if not hasattr(self, 'fields'):
			self.fields = {}
		if not hasattr(self, 'links'):
			self.associations = {}

		self.db_session = db_session

	def setDefaultSession(self, db_session):
		"""Set the default database session 
		for anything derived from DBClass.
		"""
		DBClass.db_session = db_session

	def connect(self):
		self.db_session.connect()
		
	def id(self):
		"""Return's the primary key value
		"""
		return self.fields[self.getPrimaryKeyName()].value
	
	def loadSelf(self, primary_key):
		"""Given a primary key populate our fields from the database.
		"""
		try:
			cursor = self.db_session.cursor()
			select_sql = "SELECT * FROM \"%s\" WHERE \"%s\" = %s"

			table_name = sqlEscapeString(self.table_name)
			primary_key_name = sqlEscapeString(self.getPrimaryKeyName())
			select_sql %= (table_name, primary_key_name, primary_key)
			cursor.execute(select_sql)
			# FIXME: what to do if this loads more than one record?
			record = cursor.fetchone()
			if record is None:
				warn("no item found", DebugWarning)
				raise KeyError("%s" % (str(primary_key)))
			else:
				self.loaded = 1
				self.bindFields(cursor.description, record)
		finally:
			# Tag this object as having been loaded from the database
			cursor.close()
		# Yes the difference between commiting and rolling back on a select
		# statement is kind of irrelevant, but it does fit the database model
		# better
	 
		# DELETE CODE
		# What was the point of calling rollback on a read-only connection?
		#except Exception, e:
		#	self.db_session.rollback()
		#	# once we've cleaned up the transaction pass the error on to the
		#	# rest of the code
		#	raise e
		#else:
		#	self.db_session.commit()

	def bindFields(self, descriptions, record):
		"""Given the PyDB 2.0 description dictionary of the fields and the
		fields themselves bind the field values to the corresponding Field
		objects in our class.
		"""
		for i in xrange(len(descriptions)):
			field_name = descriptions[i][0]
			try:
				self.fields[field_name].setValue(record[i], loading=self.loaded)
			except KeyError, e:
				err = "Query returned unrecognized field %s for table %s" % (
					field_name,
					self.table_name)
				warn(err, RuntimeWarning)
				#raise KeyError(err)
			except TypeError, e:
				warn("FATAL: field %s is not type %s " % ( field_name, self.fields[field_name]), RuntimeWarning)
				raise e

	def getNextKey(self):
		"""Get the next key value from a primary key sequence
		"""
		record = [None]
		try:
			cursor = self.db_session.cursor()
			# FIXME: this is a postgresql specific statement
			sql = "SELECT nextval('\"%s\"')" % (sqlEscapeString(self.getPrimaryKeyName()+"_seq"))
			warn("getNextKey: %s" % (sql), DebugWarning)
			cursor.execute(sql)
			record = cursor.fetchone()
			if record is None:
				raise KeyError("%s" % (str(self.id())))
		finally:
			# Tag this object as having been loaded from the database
			cursor.close()
			
		return record[0]

	def insertSelf(self, transactionManager=None):
		"""Inserts just the changes for this object

		if transactionManager is non-null append the updates to it instead
		of commiting to the database.
		
		Note: If you want to actually update an object hierarchy, look at commit
		"""
		warn("Saving self[%s: %s]" % (self.table_name, self.id()), DebugWarning)
		
		# where are we saving?
		if transactionManager is not None:
			cursor = transactionManager.cursor()
		else:
			cursor = self.db_session.cursor()
		
		try:
			# iterate over all fields and determine which have changed
			# construct an update for them
			update_names_list = []
			update_values_list = []

			warn("%d, %s, %d" % (self.loaded,
													 self.getPrimaryKeyName(),
													 self.isAutoSequence()),
					 DebugWarning)
			
			# try and get a primary key
			# what should we do if there is no sequence?
			if not self.loaded and \
						 self.getPrimaryKeyName() is not None and \
						 self.isAutoSequence():
				nextkey = self.getNextKey()
				self.fields[self.getPrimaryKeyName()].setValue(nextkey)
		
			# determine which fields have changed
			updated_fields = []
			for field in self.fields.values():
				warn("%s %d %d" % (field.name, field.isModified(), field.modified),
						 DebugWarning)
				if field.isModified():
					# save list of fields that we're committing.
					updated_fields.append(field)
					# append to list to update
					update_names_list.append('"'+field.name+'"')
					if field.type == types.StringType or field.type == types.UnicodeType:
						update_values_list.append("'%s'" % (sqlEscapeString(field.value)))
					elif field.type == DateTime.DateTimeType:
						update_values_list.append("'%s'" % (str(field.value)))
					elif field.type == Bool:
						update_values_list.append("'%s'" % (str(field.value)))
					else:
						update_values_list.append(str(field.value))
		
			if len(update_values_list) > 0:
				# construct the query needed to update the database
				if self.loaded:
					update_tuples = zip(update_names_list, update_values_list)
					update_pairs_list = map(lambda (x,y): '%s=%s' % (x,y), update_tuples)
					update_pairs = string.join(update_pairs_list, ', ')
					sql = "UPDATE \"%s\" SET %s WHERE \"%s\" = %s"
					sql %=(sqlEscapeString(self.table_name),
								 update_pairs,
								 sqlEscapeString(self.getPrimaryKeyName()),
								 self.id())
				else:
					update_names = string.join(update_names_list, ", ")
					update_values = string.join(update_values_list, ", ")
					sql = "INSERT INTO \"%s\" (%s) VALUES (%s);"
					sql %= (sqlEscapeString(self.table_name), update_names, update_values)
		
				#execute the query
				warn(sql, DebugWarning)
				cursor.execute(sql)
				# once we've either saved ourselves or committed updates
				# we are in the "loaded" state.
				self.loaded = 1
				
		except Exception, e:
			cursor.rollback()
			traceback.print_exc()
			raise e
		else:
			cursor.commit()
			for field in updated_fields:
				field.modified = 0
	
	def commit(self, transactionManager=None, visited=None):
		"""Attempt to write object hierarchy back to the database
		"""
		# Begin transaction
		if visited == None:
			visited = {}

		if visited.has_key(self):
			return
		
		warn("DBClass.commit %s" % (self.table_name), DebugWarning)
		#cursor = self.db_session.cursor()
		try:
			# save all linked objects whose primary keys are
			# stored in this table (one to one links)
			#local_test = lambda x: x.local_table == x.table.table_name
			local_links = filter(DBAssociation.isLocalAssociation, self.associations.values())

			if local_links is not None:
				for link in local_links:
					# update the one-to-one objects
					link.commit(transactionManager, visited)
					# update the local keys with values from the linked to objects
					link.updateLinks()

			visited[self] = 1
			self.insertSelf(transactionManager=transactionManager)
			
			# store all links whose needs the current objects primary key
			# many-to-one
			#remote_test = lambda x: x.local_table != x.table.table_name
			remote_test = lambda x: not x.isLocalAssociation()
			remote_links = filter(remote_test, self.associations.values())
			
			if remote_links is not None:
				for link in remote_links:
					# update the remote keys with the values from the local object
					link.updateLinks()
					# commit the many-to-one objects
					link.commit(transactionManager, visited)
		# DELETE CODE		
		except Exception, e:
		#	self.db_session.rollback()
			traceback.print_exc()
			raise e
		else:
		#	self.db_session.commit()
			pass

		warn("DBClass.commit %s done" % (self.table_name), DebugWarning)

	def rollback(self):
		"""Return object back to the state loaded from the database
		"""
		# FIXME: perhaps we should be caching the original values instead
		self.refresh()
	
	def refresh(self):
		"""Retrieve data out of the database again
		"""
		self.loadSelf(self.id())

	def safeDelete(self):
		"""Only deletes the object if it has no associations with other objects
		"""
		for key in self.associations.keys():
			assoc = self.associations[key]
			objList = assoc.getObjects()
			if len(objList) > 0:
				msg = 'CANNOT DELETE %s SAFELY, ABORTING DELETETION' % (self.getTableName())
				raise ValueError, msg

		self.delete()

	def delete(self, transactionManager=None):
		"""Delete the current object from the database.
		"""
		# FIXME: Should this actually even be an option?
		delete_sql = "DELETE FROM \"%s\" WHERE \"%s\" = %s"
		delete_sql %= (sqlEscapeString(self.table_name),
									 sqlEscapeString(self.getPrimaryKeyName()),
									 self.id())

		try:
			if transactionManager is not None:
				cursor = transactionManager.cursor()
			else:
				cursor = self.db_session.cursor()
			cursor.execute(delete_sql)
			cursor.commit()
		except Exception, e:
			cursor.rollback()
			raise e
		cursor.close()


	def __str__(self):
		return pprint.pformat(self.__dict__)

class TransactionManager:
	"""Provides a way of collecting updates and inserts into a single transaction

	An instance of this class can be used to collect multiple inserts and 
	updates into a single transaction which can be sent to the database in a
	single step.

	This provides a performance advantage as the index wont be rebuilt until 
	the transaction finishes.

	One downside to doing this is that objects will <em>think</em> that they 
	have been saved without actually being commited to disk.

	This could be problematic if one changes the object and comits it before 
	committing the transaction. This update will be overwritten when the 
	transaction is comitted.

	Also since commit recursively searchs for objects attached to the comited
	object that are dirty this problem of overwriting changes might even
	happen when touching an object that is merely associated with an object
	hierarchy.
	
	To be safe, finish comitting the transaction before changing other objects.

	The last issue is that since the commits require that the objects to have
	their keys set, the objects will have to hit their sequences to construct
	their unique IDs. If you then throw away the transaction those IDs will
	be lost.

	Usage:
		transaction = TransactionManager( db_session_object )

		for object in all_objects_to_commit:
			object.commit(transaction)

		transaction.commit()
	"""
	def __init__(self, session):
		if not isinstance(session, DBSessionImpl):
			raise ValueError("session parameter must be a DBSession")
		self.db_session = session
		self.sql_statements = []
		
	def commit(self):
		"""Send all of the collected changes to the database.
		"""
		cursor = self.db_session.cursor()
		for statement in self.sql_statements:
			cursor.execute(statement)
		cursor.commit()
		self.sql_statements = []

	def rollback(self):
		"""Throw the current changes away.
		"""
		self.sql_statements = []

	def _addSql(self, statement):
		"""Internal function

		Adds an sql statement to the transaction
		"""
		if type(statement) in types.StringTypes:
			self.sql_statements.append(statement)
		else:
			raise ValueError("SQL Statement must be a string")

	def cursor(self):
		"""Return a fake cursor object.

		Provides a python db-api 2.0 tyle cursor which is tied to the 
		transaction object.

		(Rather useful for minimizing the code changes necessary to support
		writing to the transaction manager.
		"""
		class TransactionCursor:
			"""Provide a cursor like interface to 
			"""
			def __init__(self, transactionManager):
				self.transactionManager = transactionManager
	
			def execute(self, sql):
				self.transactionManager._addSql(sql)

			def commit(self):
				pass

			def close(self):
				pass

			def rollback(self):
	raise NotImplementedError("What should a rollback on a TransactionManager cursor do?")

		return TransactionCursor(self)
