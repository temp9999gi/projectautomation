# -*- coding: utf-8 -*-
#
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
#이것은 무조건 logging (을)를 메소드에 포함시킨다.

#test.py
import aop.aspect as aspect

class Test(object):
    def test(self, str):
        return str

class Test2:
    def test2(self, str):
        return str
       
aspect.weave()


