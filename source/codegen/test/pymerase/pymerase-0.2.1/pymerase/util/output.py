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
#       Authors: Diane Trout
# Last Modified: $Date: 2006/12/18 15:54:02 $
#
from __future__ import nested_scopes
import types
import os

def addIndentToStrings(indent, list):
  """Given a list of strings, add some indentation.
  """
  
  return map(lambda x: " " * indent + x, list)

  #return string.join(indented_string, os.linesep)

def getOutputStream(destination, source_pathname=None, extention=""):
  """Open file based off of source name, destination, and new extention.
  """
  if type(destination) == types.StringType:
    if os.path.isdir(destination):
      base, ext = os.path.splitext(source_pathname)
      output_filename = os.path.join(destination, base + extention)
    else:
      output_filename = destination
    output_stream = open(output_filename, "w")
  elif type(destination) == types.FileType:
    output_stream = destination
  else:
    output_stream = sys.stdout
    
  return output_stream


