# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start

"""
일단 해야 하는 것은 뭐냐면?
crud를 주면 c를 반환한다.
rud를 주면 D
"""
def getKeyCrud(crudGubun):
	if crudGubun.find('C')>=0:
		return 'C'
	if crudGubun.find('D')>=0:
		return 'D'
	if crudGubun.find('U')>=0:
		return 'U'
	if crudGubun.find('R')>=0:
		return 'R'

	return crudGubun #에러 상황이다.

yy = getKeyCrud('CR')
yy = getKeyCrud('CR')
yy = getKeyCrud('CRUD')
yy = getKeyCrud('RUD')
yy = getKeyCrud('C')
yy = getKeyCrud('CD')
yy = getKeyCrud('DC')
yy = getKeyCrud('UD')