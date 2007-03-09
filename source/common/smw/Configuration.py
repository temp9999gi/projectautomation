"""Keeps a database with different user and runtime options.
"""

__author__="Ivan Porres iporres@abo.fi"
__date__="13.02.02"

import inspect
import os.path
import sys
import string

class ConfigParameter:
		def __init__(self,name,description,defaultValue,permanent=1):
				self.name=name
				self.description=description
				self.defaultVaue=defaultValue
				self.currentValue=defaultValue
				self.permanent=permanent
				
		def set(self,v):
				self.currentValue=v

		def get(self):
				return self.currentValue

		def __repr__(self):
				return str(self.currentValue)

		def __int__(self):
				return int(self.currentValue)

		def __getitem__(self, index):
				return self.currentValue[index]
		
class BooleanParameter(ConfigParameter):
		def set(self,v):
				if not v or v=="no" or v=="false" or v=="False":
						v=0
				else:
						v=1
				self.currentValue=v

class ChoiceParameter(ConfigParameter):
		def __init__(self,name,description,choices,defaultChoice,permanent=1):
				ConfigParameter.__init__(self,name,description,defaultChoice,permanent)
				self.choices=choices
				self.set(defaultChoice)

		def set(self,v):
				assert(v>=0 and v<len(self.choices))
				self.currentValue=v

		def get(self):
				return self.currentValue

class StringParameter(ConfigParameter):
		pass

class DirectoryParameter(StringParameter):
		pass

class ModelParameter(ConfigParameter):
		def __init__(self,name,description,fileName,output=0):
				ConfigParameter.__init__(self,name,description,fileName)
				self.model=None
				self.output=output

		def setModel(self,v):
			self.model=v

		def getModel(self):
			return self.model

class Configuration:
		"""Configuration keeps the	configuration options of an application.

		The configuration database is shared by all instances of this class.
		"""
		
		parameters=None
		
		def __init__(self):
				if Configuration.parameters!=None:
						# Already intialized
						return
				Configuration.userPreferences={}
				Configuration.parameters={}
				for p in self.defaultPreferences():
						self.registerParameter(p)
				self.loadUserPreferences()
				
		def defaultPreferences(self):
				# Add here only generic options that should be available
				# to all smw applications
				path=os.path.dirname(inspect.getfile(Configuration))
				return [
						DirectoryParameter("install_path",
															 "The path were the smw toolkit is installed",
															 path,
															 permanent=0),
						DirectoryParameter("user_home",
															 "User home directory",
															 string.replace(os.environ.get("HOME",""),"\\","/")
															 )
															 
						]			 
														
		def registerParameter(self,p):
				"""Registers a configuration option in the database.
				Options must be registered in the database before
				they can be set and retrieved.

				name and description are printable strings and defaultValue
				can be of any data type.
				Options are saved in a configuration file only if they are declared
				permanent"""

				if ' ' in p.name or '\n' in p.name:
						raise "Parameter name should not contain spaces or returns",p
				Configuration.parameters[p.name]=p
				if Configuration.userPreferences.has_key(p.name):
						p.set(Configuration.userPreferences[p.name])
						
		def getParameter(self,name):
				"""Returns the current value of the option name.
				Raises an exception if name is not registered."""
				assert(Configuration.parameters.has_key(name))
				return Configuration.parameters[name]

		def saveUserPreferences(self,fileName=''):
				if not fileName:
						if os.environ.has_key("HOME"):
								fileName=os.environ["HOME"] + os.sep + ".smw"+os.sep+"smw.conf"
				assert(fileName)
				fd=open(fileName,'w')
				for p in self.parameters.values():
						if p.permanent:
								v=str(p.currentValue)
								if '\n' in v:
										print "Cannot store user preference "+p.name+" since its value contains a return chatacter"
								else:
										fd.write("# "+p.name+" :"+p.description+"\n")
										fd.write(p.name+" '"+str(p.currentValue)+"'\n")
				fd.close()

		def loadUserPreferences(self,fileName=''):
				if not fileName:
						if os.environ.has_key("HOME"):
								fileName=os.environ["HOME"] + os.sep + ".smw"+os.sep+"smw.conf"
				if fileName:
						Configuration.userPreferences={}
						try:
								fd=open(fileName,"r")
								for line in fd.readlines():
										if line and line[0]=='#':
												continue
										option=line.split()
										if len(option)>=2: 
												name=option[0]
												value=line[len(name)+1:-1]
												if value[0] in ['"',"'"] and \
													 value[-1] in ['"',"'"]:
														value=value[1:-1]
												Configuration.userPreferences[name]=value
												if Configuration.parameters.has_key(name):
														Configuration.parameters[name].set(value)
														
								fd.close()
						except Exception,e:
								print "Cannot load user preferences",e

def parseCmdLine(cmdline,parameterDict):
		i=0

		while (i<len(cmdline)):
				word=cmdline[i]
				if word[:2]=='--':
						word=word[2:]
						if parameterDict.has_key(word):
								p=parameterDict[word]
								i=i+1
								value=cmdline [i]
								
								p.set(value)
				i=i+1								
						
		return 0
		
