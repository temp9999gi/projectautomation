# -*- coding: utf-8 -*-
from win32com.client import Dispatch
import pythoncom

from CommonUtil import *
#from Constants import *

ComUtil = CommonUtil()

#import win32com.client
#a=win32com.client.Dispatch("access.application.8")
#self.xl = Dispatch("Excel.Application")
try:
	a=Dispatch("Access.Application")
except pythoncom.com_error, (hr, msg, exc, arg):
	ComUtil.printPythonComError(hr, msg, exc, arg)


a.Visible=1
#C:\_projectautomation\source\dbAutomation\checkDbDictionary\db
a.OpenCurrentDatabase("C://_projectautomation/source/test/Access/MyDB.mdb")

aDoCmd = a.DoCmd
aDoCmd.OpenForm('test',3)

#a.DoCmd.OpenReport("ber",2)
#a.DoCmd.OpenForm "Employees", acNormal

##p = PRTMIP()
##p.read(a, 0)
##p.display()

