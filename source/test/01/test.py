# -*- coding: utf-8 -*-
import sys
#sys.path.insert(0, "C://_projectautomation/source/lib")
sys.path.append("C://_projectautomation/source/lib")

print sys.path
#\lib\libTest\subLib
import libTest.subLib.libTest2 as tt

x = tt.splitT('aa_bb')


