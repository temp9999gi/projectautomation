from __future__ import nested_scopes
import re
import string
import types

class NameMangler:
	def mangle(self, name):
		"""Convert a name a particular word splitting convention
		"""
		raise NotImplementedError("abstract class")

	def createGetter(self, name):
		"""Given a mangled name construct the appropriate getter function name
		"""
		raise NotImplementedError("abstract class")

	def createSetter(self, name):
		"""Given a mangled name construct the appropriate setter function name
		"""
		raise NotImplementedError("abstract class")

	def createAppend(self, name):
		"""Given a mangled name construct the appropriate append function name
		"""
		raise NotImplementedError("abstract class")
	

class nullMangler(NameMangler):
	"""Given a string leave it alone.
	"""
	def mangle(self, name):
		return name

	def createGetter(self, name):
		return "get%s" % (self.mangle(name))

	def createSetter(self, name):
		return "set%s" % (self.mangle(name))

	def createAppender(self, name):
		return "append%s" % (self.mangle(name))


class CapWord(nullMangler):
	"""Given a string convert it to CapWord convention.
	"""
	def mangle(self, name):
		def uppercaseFirstLetter(s):
			if len(s) > 0:
				return string.upper(s[0]) + s[1:]
			else:
				return s
		if type(name) == types.StringType or type(name) == types.UnicodeType:
			return string.join(map(uppercaseFirstLetter, re.split("[\s_]+",name)),"")
		else:
			return ""
			# FIXME: this is the better solution by the XMI reader returns
			# FIXME: some garbage we need to ignore.
			#raise ValueError("mangle requires a string not a %s" % str(type(name)))


class underscore_word(nullMangler):
	"""Given_a_string_convert_it_to_underscore_convention.
	"""
	def mangle(self, name):
		if type(name) == types.StringType or type(name) == types.UnicodeType:
			return string.lower(re.sub('(\w)([A-Z][^A-Z])', "\\1_\\2", name))
		else:
			return ""
			#raise ValueError("mangle requires a string not a %s" % str(type(name)))

	def createGetter(self, name):
		return "get_%s" % (self.mangle(name))

	def createSetter(self, name):
		return "set_%s" % (self.mangle(name))

	def createAppender(self, name):
		return "append_%s" % (self.mangle(name))

	
class EnglishWord(nullMangler):
	"""Given a string convert it to english sentance conventions

	capitalize first word, put spaces between other elements.
	"""
	def mangle(self, name):
		if type(name) == types.StringType or type(name) == types.UnicodeType:
			if len(name) > 0:
				s = string.lower(re.sub('(\w)([A-Z][^A-Z])', "\\1 \\2", name))
				return string.upper(s[0]) + s[1:]

		return ""
		#raise ValueError("mangle requires a string not a %s" % str(type(name)))

	def createGetter(self, name):
		return "get_%s" % (self.mangle(name))

	def createSetter(self, name):
		return "set_%s" % (self.mangle(name))

	def createAppender(self, name):
		return "append_%s" % (self.mangle(name))


class lowercaseword(nullMangler):
	"""Given a string convert it to lowercase.
	"""
	def mangle(self, name):
		if type(name) == types.StringType or type(name) == types.UnicodeType:
			if len(name) > 0:
				return string.lower(name)

		return ""
	
################
# Name mangling for keys instead of member variables

class RelationalKey:
	"""Given a name, convert it into primary and foreign key names.

	getPrimaryKey('name_pk') -> 'name_pk'
	getPrimaryKey('name_fk') -> 'name_pk'
	getPrimaryKey('name')		-> 'name_pk'
	getForeignKey('name_pk') -> 'name_fk'
	getForeignKey('name_fk') -> 'name_fk'
	getForeignKey('name')		-> 'name_fk'
	"""
	def getPrimaryKey(self, name):
		if re.search("[Pp][Kk]$", name):
			return name
		elif re.search("[Ff][Kk]$", name):
			return re.sub("[Ff][Kk]$", "pk", name)
		else:
			return name + "_pk"

	def getForeignKey(self, name):
		if re.search("[Pp][Kk]$", name):
			mangled_name = re.sub("[Pp][Kk]$", "fk", name)
		elif re.search("[Ff][Kk]$", name):
			mangled_name = name
		else:
			mangled_name = name + "_fk"
		return mangled_name
	
