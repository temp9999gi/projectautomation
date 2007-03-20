import os
import string
import types
from Functor import Functor

# FIXME: this templating system doesn't handle code with %s substitutions well
# FIXME: something should be done about this.

class Template(object):
  """Base class for defining python templating objects.

  Derive from this base class and add functions to define the various
  keyword substituions you'd like to provide. 
  """
  def __init__(self, namespace=None):
    """Constructor

    namespace -- Provide a namespace to resolve variables in, defaults to class
    """
    if namespace is None:
      namespace = self.__dict__
      
    self.namespace = {}
    self.namespace.update(namespace)
    
    functionNameList = self.keys()
    for functionName in functionNameList:
      function = self.__class__.__dict__[functionName]
      self.namespace[functionName] = Functor(function, self)

  def keys(self):
    """Return list of template functions
    """
    utilityFunctions = Template.__dict__.keys()
    allFunctions = self.__class__.__dict__.keys()
    templateFunctions = []
    for f in allFunctions:
      if f not in utilityFunctions:
        templateFunctions.append(f)

    return templateFunctions
      
  def __getitem__(self, key):
    """Resolve dictionary lookup as function call, including parameter lookup
    """
    if type(key) not in types.StringTypes:
      raise RuntimeError("Template expression must be a string")
    elif len(key) == 0:
      raise RuntimeError("Template expression must not be the empty string")

    return eval(key, self.namespace)

  def writeFile(self, template, destination):
    """Process template and save result to destination
    """
    if type(template) is types.ListType:
      result = []
      for l in template:
        result += [l % (self)]
      result = string.join(result, os.linesep)
    else:
      result = template % (self)

    destination_file = open(destination, "w+")
    destination_file.write(result)
    destination_file.close()
  
