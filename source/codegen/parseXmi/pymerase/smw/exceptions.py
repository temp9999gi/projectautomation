from xmlrpclib import *

class SMWException(Exception):
		def __init__(self, value = "(SMWException)"):
				self.value = value
				Exception.__init__(self)
				
		def __str__(self):
				return self.value

class RepositoryException(SMWException):
		def __init__(self, value = "(RepositoryException)"):
				SMWException.__init__(self, value)


class CantConnect(RepositoryException):
		def __init__(self, value = "(CantConnect)"):
				RepositoryException.__init__(self, value)

class BadAuthentication(CantConnect):
		def __init__(self, value = "(BadAuthentication)"):
				RepositoryException.__init__(self, value)

class BadClientAuthentication(BadAuthentication):
		def __init__(self, value = "(BadClientAuthentication)"):
				RepositoryException.__init__(self, value)

class BadServerAuthentication(BadAuthentication):
		def __init__(self, value = "(BadServerAuthentication)"):
				RepositoryException.__init__(self, value)



class NoSuchTag(RepositoryException):
		def __init__(self, value = "(NoSuchTag)"):
				RepositoryException.__init__(self, value)

class NoSuchBranch(RepositoryException):
		def __init__(self, value = "(NoSuchBranch)"):
				RepositoryException.__init__(self, value)

class IsNotLatest(RepositoryException):
		def __init__(self, value = "(IsNotLatest)"):
				RepositoryException.__init__(self, value)

class NoElements(RepositoryException):
		def __init__(self, value = "(NoElements)"):
				RepositoryException.__init__(self, value)

class BadTagGiven(RepositoryException):
		def __init__(self, value = "(BadTagGiven)"):
				RepositoryException.__init__(self, value)

class BadObjectIdGiven(RepositoryException):
		def __init__(self, value = "(BadObjectIdGiven)"):
				RepositoryException.__init__(self, value)

class IncompatibleRepositoryRevision(RepositoryException):
		def __init__(self, value = "(IncompatibleRepositoryRevision)"):
				RepositoryException.__init__(self, value)

class CantJoinParentWithChild(RepositoryException):
		"""Can't join parent tag with its own (transitive) child,
		the tags must be on separate branches."""
		def __init__(self, rev1, rev2, value = "(CantJoinParentWithChild)"):
				self.rev1 = rev1
				self.rev2 = rev2
				RepositoryException.__init__(self, value)

class InternalRepositoryError(RepositoryException):
		def __init__(self, value = "(InternalRepositoryError)"):
				RepositoryException.__init__(self, value)

class CantPatchWithMergeConflicts(RepositoryException):
		def __init__(self, value = "(CantPatchWithMergeConflicts)"):
				RepositoryException.__init__(self, value)

class WFRException(SMWException):
		def __init__(self,description= "(WFRException)",offender=None):
				self.description=description
				self.offender=offender
				SMWException.__init__(self)
				
		def __str__(self):
				return self.description+':'+str(self.offender)
