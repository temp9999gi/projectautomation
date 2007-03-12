# -*- coding: utf-8 -*-
from win32com.client import Dispatch
import pythoncom

from CommonUtil import CommonUtil
#from Constants import *

ComUtil = CommonUtil()

#import win32com.client
#a=win32com.client.Dispatch("access.application.8")
#self.xl = Dispatch("Excel.Application")
try:
	aces=Dispatch("Access.Application")
except pythoncom.com_error, (hr, msg, exc, arg):
	ComUtil.printPythonComError(hr, msg, exc, arg)


aces.Visible=1
aces.OpenCurrentDatabase("C://_projectautomation/source/test/Access/MyDB.mdb")

aDoCmd = aces.DoCmd

QueryName='010_1'
View = 0
"""
View   선택 요소로서 AcView 형식입니다.

AcView는 다음 AcView 상수 중 하나를 사용할 수 있습니다.

acViewDesign 1
acViewNormal  0 기본값입니다.
acViewPivotChart 4
acViewPivotTable 3
acViewPreview 2
"""

x = aDoCmd.OpenQuery(QueryName, View)

QueryName='010_2'
x = aDoCmd.OpenQuery(QueryName, View)

print 11
