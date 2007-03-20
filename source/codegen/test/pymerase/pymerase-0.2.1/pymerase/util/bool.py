###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) 2001 by:                                                 #
#    * California Institute of Technology                                 #
#                                                                         #
#    All Rights Reserved.                                                 #
#                                                                         #
# Permission is hereby granted, free of charge, to any person             #
# obtaining a copy of this software and associated documentation files    #
# (the "Software"), to deal in the Software without restriction,          #
# including without limitation the rights to use, copy, modify, merge,    #
# publish, distribute, sublicense, and/or sell copies of the Software,    #
# and to permit persons to whom the Software is furnished to do so,       #
# subject to the following conditions:                                    #
#                                                                         #
# The above copyright notice and this permission notice shall be          #
# included in all copies or substantial portions of the Software.         #
#                                                                         #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,         #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF      #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                   #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS     #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN      #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN       #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE        #
# SOFTWARE.                                                               #
###########################################################################
import types
import string

def parseBoolValue(value):
  """Parse a random value into a boolean equivalent

  For integers:
    not equal 0 -> true
    0 -> false
  For strings:
    strings that start with 'y' or 't' -> true
    strings that convert to integers follows integer rules
    all others -> false
  For Nones:
    None -> False
  For lists:
    length > 0 -> true
    length = 0 -> false
  """
  if type(value) == types.IntType:
    if value != 0:
      return 1
    else:
      return 0
  elif type(value) == types.StringType or type(value) == types.UnicodeType:
    v = string.lower(value)[0]
    if v == "y" or v == "t":
      return 1
    else:
      # try to convert to a number and then convert to bool
      try:
        return parseBoolValue(int(value))
      except ValueError:
        return 0
      return 0
  elif type(value) == types.NoneType:
    return 0
  elif type(value) == types.ListType:
    if len(value) > 0:
      return 1
    else:
      return 0
    
class Bool:
  def __init__(self, value):
    self.bit = parseBoolValue(value)

  def __str__(self):
    if self.bit:
      return '1'
    else:
      return '0'

  # do I actually need these things?
  def __and__(self, other):
    return (self.bit & other)

  def __xor__(self, other):
    return self.bit ^ other
  
  def __or__(self, other):
    return (self.bit | other)


  
