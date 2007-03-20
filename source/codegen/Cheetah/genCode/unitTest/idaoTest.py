#*- coding: utf-8 -*-

import unittest
import string

#import sys
#sys.path.append('C://_python/Cheetah-2.0rc6/_genValueObject2')
from commonUtil import *


#-----------------------------------------------------------------------------
# CONSTANTS & GLOBALS
TRUE, FALSE = (1==1),(1==0)
#-----------------------------------------------------------------------------
class IDaoTestCase(unittest.TestCase):
    def setUp(self):
        self.fileName = '.' + IDAO_OUT_DIR +'AccountDao.java'
        self.outFile1 = open(self.fileName,'r')
        self.outFile =  self.outFile1.read()
        self.isTrue = FALSE
        
    def tearDown(self):
        self.sorurce =''
        self.isTrue = FALSE

    #-----------------------------------------------------------------------------
    def testRun(self):
		self.sorurce = \
"""package com.ibatis.jpetstore.persistence.iface;

import com.ibatis.jpetstore.domain.Account;

public interface AccountDao {

  Account getAccount(String username);

  Account getAccount(String username, String password);

  void insertAccount(Account account);

  void updateAccount(Account account);

  void deleteAccount(Account account);

}"""    	
		#find( sub[, start[, end]]) 
		#  Return the lowest index in the string where substring sub is found, 
		#  such that sub is contained in the range [start, end]. 
		#  Optional arguments start and end are interpreted as in slice notation. 
		#  Return -1 if sub is not found. 
		 
		if self.outFile.find(self.sorurce) >= 0 : self.isTrue = TRUE
		assert TRUE == self.isTrue, '생성된 파일이 원하는데로 생성되었는가 체크'


    #-----------------------------------------------------------------------------	
    def suite(self):    	
		suite = unittest.TestSuite()
		suite.addTest(IDaoTestCase("testRun"))		
		return suite
	
                                          

#-----------------------------------------------------------------------------	
if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(IDaoTestCase("testRun"))
	runner = unittest.TextTestRunner()
	runner.run(suite)       
