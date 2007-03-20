# These are the basic datatypes used in a metamodel
#

import string

class MMDataType:
		pass

class MMString(MMDataType):
		__name__="String"
		default=""
		def fromString(self,s):
				return s
		def toString(self,s):
				return str(s)
		
class MMUnlimitedInteger(MMDataType):
		__name__="UnlimitedInteger"
		default=0
		def fromString(self,s):
				return int(s)
		def toString(self,s):
				return str(s)
		
class MMInteger(MMUnlimitedInteger):

		__name__="Integer"
		default=0

class MMUnlimitedRealNumber(MMDataType):
		__name__="UnlimitedRealNumber"
		default=0.0
		def fromString(self,s):
				return float(s)
		def toString(self,s):
				return str(s)

class MMEnumeration(MMDataType):
		default=0

		def fromString(self,s):
				for i in range(len(self.description)):
						sl=string.split(self.description[i],"_")
						if s==self.description[i] or (len(sl)==2 and s==sl[1]):
								return i
				# We cannot find s so we return the default value
				return self.default

		def toString(self,s):
				# remove prefix 
				r=self.description[s]
				if len(r)>3 and r[2]=="_":
						return r[3:]
				else:
						return r

class MMBoolean(MMEnumeration):
		description=["false","true"]

MMBoolean.__name__="Boolean"

class MMGeometry(MMString):
		pass
MMGeometry.__name__="Geometry"

class MMName(MMString):
		pass
MMName.__name__="Name"

class Name(MMName):
		pass

class Geometry(MMGeometry):
		pass

class String(MMString):
		pass

class Boolean(MMBoolean):
		pass

class Integer(MMInteger):
		pass

class UnlimitedInteger(MMUnlimitedInteger):
		pass

class Float(MMUnlimitedRealNumber):
		pass

class Double(MMUnlimitedRealNumber):
		pass

