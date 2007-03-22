###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) 2003 by:                                                 #
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
#
#       Authors: Brandon King
# Last Modified: $Date: 2006/12/18 15:54:02 $
#

class Templates:
  def __init__(self):
    pass

  def getBasicTemplate(self):
    template = """#!/usr/bin/env python
###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) 2002 by:                                                 #
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
#
#  Generated By: Pymerase (CreatePyTkWidgets Output Module)
#           URL: http://pymerase.sourceforge.net
# Last Modified: $Date: 2006/12/18 15:54:02 $
#

import Tkinter
import ValidatingEntry
import modes

from ExtendedOptionMenu import ExtendedOptionMenu

class %CLASSNAME%Widget(Tkinter.Frame):

  def __init__(self, master=None, mode=modes.DEFAULT, **kw):
    Tkinter.Frame.__init__(self, master, kw)
    self.parent = master
    self.mode = mode

%VAR_ELEMENT%

  def getParent(self):
    return self.parent

  def save(self):
    \"\"\"
    Override save function.
    \"\"\"
    print 'Save Not Implemented'

  def load(self):
    \"\"\"
    Override lost function.
    \"\"\"
    print 'Load Not Implemented'
    
%GET_FUNCTION%


%SET_FUNCTION%

if __name__ == '__main__':
  root = Tkinter.Tk()
  root.title(\"%CLASSNAME%\")
  %CLASSNAME%gui = %CLASSNAME%Widget(root, modes.DEFAULT)
  root.mainloop()
"""
    return template


  def getDbTemplate(self):
    template = """#!/usr/bin/env python
###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) 2003 by:                                                 #
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
#
#  Generated By: Pymerase (CreatePyTkWidgets Output Module)
#           URL: http://pymerase.sourceforge.net
# Last Modified: $Date: 2006/12/18 15:54:02 $
#

import Tkinter
from %CLASSNAME%Widget import %CLASSNAME%Widget
from SaveWidget import SaveWidget
from NavBar import NavBar
from dbSession import sessionObj

import modes

class %CLASSNAME%DbWidget(%CLASSNAME%Widget):

  def __init__(self, master, mode=modes.DEFAULT, session=None):

    self.master = master
    self.bodyFrame = Tkinter.Frame(self.master)
    self.footerFrame = Tkinter.Frame(self.master)
    self.bodyFrame.grid(row=0)
    self.footerFrame.grid(row=1)

    %CLASSNAME%Widget.__init__(self, self.bodyFrame, mode)

    if session is None:
      self.session = sessionObj(self.master)
    else:
      self.session = session
    self.dbs = self.session.getDbs()

    self.curDBObj = None

%OPTION_MENU_DICT%
    
    self.navBar = NavBar(self.footerFrame, self, self.dbs.%CLASSNAME%, self.session)
    self.navBar.pack()
    
    self.SaveWidget = SaveWidget(self.footerFrame, self)
    self.SaveWidget.pack()

    
%UPDATE_FUNCTIONS%

  def setCurrentDBObj(self, obj):
    self.curDBObj = obj

  def getCurrentDBObj(self):
    return self.curDBObj

  def save(self):
    obj = self.getCurrentDBObj()

    if obj is not None:
%SAVE_FUNCTION%

      obj.commit()
    else:
      print \"Create new object before saving.\"

  def load(self, obj):
%LOAD_FUNCTION%

    self.setCurrentDBObj(obj)

if __name__ == '__main__':
  root = Tkinter.Tk()
  root.title('%CLASSNAME%DbWidget')
  gui = %CLASSNAME%DbWidget(root, modes.OPTION_MENU)
  root.mainloop()
"""
    return template