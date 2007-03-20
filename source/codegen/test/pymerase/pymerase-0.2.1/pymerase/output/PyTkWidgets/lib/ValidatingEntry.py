from Tkinter import *

class ValidatingEntry(Entry):
  """
  ValidatingEntry Class in full or in part from
  http://effbot.org/zone/tkinter-entry-validate.htm
  """
  # base class for validating entry widgets

  def __init__(self, master, value="", **kw):
    apply(Entry.__init__, (self, master), kw)
    self.__value = value
    self.__variable = StringVar()
    self.__variable.set(value)
    self.__variable.trace("w", self.__callback)
    self.config(textvariable=self.__variable)

  def __callback(self, *dummy):
    value = self.__variable.get()
    newvalue = self.validate(value)
    if newvalue is None:
      self.__variable.set(self.__value)
    elif newvalue != value:
      self.__value = newvalue
      self.__variable.set(newvalue)
    else:
      self.__value = value

  def validate(self, value):
    # override: return value, new value, or None if invalid
    return value

class IntegerEntry(ValidatingEntry):
  """
  IntergerEntry in full or in part from http://effbot.org/zone/tkinter-entry-validate.htm
  """
  def validate(self, value):
    try:
      if value == '':
        return value
      elif value:
        v = int(value)
        return value
    except ValueError:
      return None


class FloatEntry(ValidatingEntry):
  """
  FloatEntry in full or in part from http://effbot.org/zone/tkinter-entry-validate.htm
  """
  def validate(self, value):
    try:
      if value == '':
        return value
      elif value:
        v = float(value)
        return value
    except ValueError:
      return None

class MaxLengthEntry(ValidatingEntry):
  """
  MaxLengthEntry in full or in part from http://effbot.org/zone/tkinter-entry-validate.htm
  """
  def __init__(self, master, value="", maxlength=None, **kw):
    self.maxlength = maxlength
    apply(ValidatingEntry.__init__, (self, master), kw)

  def validate(self, value):
    if self.maxlength:
      value = value[:self.maxlength]
      return value
    else:
      return value

