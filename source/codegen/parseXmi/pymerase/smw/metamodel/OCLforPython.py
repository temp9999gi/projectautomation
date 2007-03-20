import copy
import inspect
from smw.metamodel.MMAtom import MMAtom

# OCL-like collectiones
def implies(a,b):
		return not a or b

class MMCollection(MMAtom):
		def __init__(self,items=None):
				self.__register__('items',[])
				if not items:
						self.items=[]
				else:
						self.items=copy.copy(items)
						
		def __iter__(self):
				return iter(self.items)
		
		def __str__(self):
				return str(self.items)

		def __nonzero__(self):
				return self.items!=[]
		
		def __reset__(self):
				"""Resets all connections at _this_ end."""
				self.items = []

		def __getitem__(self,key):
				if type(key)==type(slice(0,0)):
						return self.items[key.start:key.stop]
				else:
						return self.items[key]

		def __getattr__(self,attr):
				#if attr[:2]!="__":
				#		print "__getattr__",self,attr
				# shorthand for collect page 6-71
				if attr[:2]=="__" or (self.items and not hasattr(self.items[0],attr)):
						raise AttributeError
				result=MMBag()
				for v in self.items:
						result.append(getattr(v,attr))
				return result
		
		def sort(self,func):
				self.__register__('items',copy.copy(self.items))
				self.items.sort(func)
				
		def __add__(self,other):
				if isinstance(other, MMCollection):
						return self.__class__(self.items + other.items)
				elif isinstance(other, type(self.items)):
						return self.__class__(self.items + other)
				else:
						return self.__class__(self.items + list(other))

						
		def __setitem__(self,key,items):
				self.__register__('items',copy.copy(self.items))
				self.items[key]=items
		
		def remove(self,item):
				"""Removes a specific value."""
				self.__register__('items',copy.copy(self.item))
				# There is something wrong with this routine.
				# It doesn't update the other end
				self.items.remove(item)
				assert(0)

		def pop(self, index):
				"""Removes the value at specified index."""
				self.__register__('items',copy.copy(self.items))
				self.items.pop(index)
				# There is something wrong with this routine.
				# It doesn't update the other end
				assert(0)
				

		def __len__(self):
				return len(self.items)

		def __getstate__(self):
				return {"items":copy.copy(self.items)}

		def __setstate__(self,state):
				self.items=state["items"]

		def __repr__(self):
				return str(self.__dict__.get('items',[]))

		# OCL-like memebers

		def size(self):
				return len(self.items)

		def includes(self,o):
				return o in self.items

		def excludes(self,o):
				return not self.includes(o)

		def count(self,o):
				c=0
				for x in self.items:
						if x==o:
								c=c+1
				return c

		def includesAll(self,c):
				for o in c:
						if o not in self.items:
								return 0
				return 1

		def excludesAll(self,c):
				for o in c:
						if o in self.items:
								return 0
				return 1

		def select(self,f):
				result=MMSet()
				for v in self.items:
						if f(v):
								result.append(v)
				return result

		def reject(self,f):
				result=MMSet()
				for v in self.items:
						if not f(v):
								result.append(v)
				return result

		def collect(self,f):
				result=MMBag()
				for v in self.items:
						result.append(f(v))
				return result

		def isEmpty(self):
				return len(self.items)==0

		def nonEmpty(self):
				return not self.isEmpty()
		
		def sum(self):
				r=0
				for o in self.items:
						r=r+o
				return r
		
		def forAll(self,f):
				if not self.items or not inspect.getargspec(f)[0]:
						return 1

				nargs=len(inspect.getargspec(f)[0])
				if inspect.getargspec(f)[3]:
						nargs=nargs-len(inspect.getargspec(f)[3])
						
				assert(nargs>0)
				nitems=len(self.items)
				index=[0]*nargs
				
				while 1:
						args=[]
						for x in index:
								args.append(self.items[x])
						if not apply(f,args):
								return 0
						c=len(index)-1
						index[c]=index[c]+1
						while index[c]==nitems:
								index[c]=0
								c=c-1
								if c<0:
										return 1
								else:
										index[c]=index[c]+1 
								if index[c]==nitems-1:
										c=c-1

		def exist(self,f):
				return self.exists(f)
		
		def exists(self,f):
				if not self.items or not inspect.getargspec(f)[0]:
						return 0

				nargs=len(inspect.getargspec(f)[0])
				if inspect.getargspec(f)[3]:
						nargs=nargs-len(inspect.getargspec(f)[3])
						
				assert(nargs>0)
				nitems=len(self.items)
				index=[0]*nargs
				while 1:
						args=[]
						for x in index:
								args.append(self.items[x])
						if apply(f,args):
								return 1
						c=len(index)-1
						index[c]=index[c]+1
						while index[c]==nitems:
								index[c]=0
								c=c-1
								if c<0:
										return 0
								else:
										index[c]=index[c]+1 
								if index[c]==nitems-1:
										c=c-1

		def union(self,s):
				for o in s:
						self.append(o)

		def first(self):
				return self.items[0]

		def last(self):
				return self.items[-1]
class MMBag(MMCollection):
		def insert(self,v):
				self.append(v)
				
		def append(self,v):
				self.__register__('items',copy.copy(self.items))
				self.items.append(v)

		def asSet(self):
				result=MMSet()
				for i in self.items:
						result.append(i)
				return result

		def asSequenece(self):
				result=MMSequence()
				for i in self.items:
						result.append(i)
				return result
		
class MMSequence(MMCollection):
		def insert(self,v):
				self.append(v)
				
		def append(self,v):
				self.__register__('items',copy.copy(self.items))
				##for i in range(len(self.items)):
##						if v<self.items[i]:
##								self.items=self.items[:i]+[v]+self.items[i:]
##								return
				self.items.append(v)

		def at(self,i):
				assert(i>=1 and i<=len(self.items))
				return self.items[i-1]
	 
		
class MMSet(MMCollection):
		def append(self,v):
				if v not in self.items:
						self.__register__('items',copy.copy(self.items))
						self.items.append(v)

		def insert(self, value, index = -1):
				self.__register__('items',copy.copy(self.items))
				if index == -1:
						# BUG:
						# There's a bug somewhere
						# This must be "append", it can't be
						# self.items.insert(len(self.items), value)
						return self.append(value)
				#
				# If the below is true, there is something
				# wrong in the diff routines.
				#
				if len(self.items) < index:
						print
						print "ERRROR IN DIFF ROUTINES"
						print "PLEASE REPORT THIS PROBLEM"
						print
						print self.items
						print index
						print value
						assert(0)

				self.__register__('items',copy.copy(self.items))
				self.items.insert(index, value)
		
		def index(self,v):
				"""Returns at what index value v is."""
				return self.items.index(v)
