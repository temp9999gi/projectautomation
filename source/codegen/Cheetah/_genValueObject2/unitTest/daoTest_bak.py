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
class DaoTestCase(unittest.TestCase):
    def setUp(self):
        self.fileName = '.' + DAO_OUT_DIR +'AccountSqlMapDao.java'
        self.outFile1 = open(self.fileName,'r')
        self.outFile =  self.outFile1.read()
        self.isTrue = FALSE
        
    def tearDown(self):
        self.sorurce =''
        self.isTrue = FALSE

    #-----------------------------------------------------------------------------
    def testImportArea(self):
		self.sorurce = \
"""package com.ibatis.jpetstore.persistence.sqlmapdao;

import com.ibatis.dao.client.DaoManager;
import com.ibatis.jpetstore.domain.Account;
import com.ibatis.jpetstore.persistence.iface.AccountDao;
"""    	
		#find( sub[, start[, end]]) 
		#  Return the lowest index in the string where substring sub is found, 
		#  such that sub is contained in the range [start, end]. 
		#  Optional arguments start and end are interpreted as in slice notation. 
		#  Return -1 if sub is not found. 
		 
		if self.outFile.find(self.sorurce) >= 0 : self.isTrue = TRUE
		assert TRUE == self.isTrue, '선언부 체크'


    #-----------------------------------------------------------------------------	
    def testMethodCheck(self):    	
    	
		self.sorurce = \
"""public class AccountSqlMapDao extends BaseSqlMapDao implements AccountDao {

  public AccountSqlMapDao(DaoManager daoManager) {
    super(daoManager);
  }

  public Account getAccount(String username) {
    return (Account) queryForObject("getAccountByUsername", username);
  }

  public Account getAccount(String username, String password) {
    Account account = new Account();
    account.setUsername(username);
    account.setPassword(password);
    return (Account) queryForObject("getAccountByUsernameAndPassword", account);
  }

  public void insertAccount(Account account) {
    update("insertAccount", account);
    update("insertProfile", account);
    update("insertSignon", account);
  }
"""  
		if self.outFile.find(self.sorurce) >= 0 : self.isTrue = TRUE
		assert TRUE == self.isTrue, 'select, insert메소드들이 정확이 생성되었나?'


    #-----------------------------------------------------------------------------	
    def testUpdateMethod(self):    	
    	
		self.sorurce = \
"""
  public void updateAccount(Account account) {
    update("updateAccount", account);
    update("updateProfile", account);
    update("updateSignon", account);
"""
		if self.outFile.find(self.sorurce) >= 0 : self.isTrue = TRUE
		assert TRUE == self.isTrue, 'update메소드들이 정확이 생성되었나?'



    #-----------------------------------------------------------------------------	
    def testDeleteMethod(self):    	
    	
		self.sorurce = \
"""public void deleteAccount(Account account) {
    delete("deleteAccount", account);
  }
"""
		if self.outFile.find(self.sorurce) >= 0 : self.isTrue = TRUE
		assert TRUE == self.isTrue, '메소드들이 정확이 생성되었나?'



#-----------------------------------------------------------------------------	
if __name__ == "__main__":
	daoTestSuite = unittest.TestSuite()
	daoTestSuite.addTest(DaoTestCase("testImportArea"))
	daoTestSuite.addTest(DaoTestCase("testMethodCheck"))
	daoTestSuite.addTest(DaoTestCase("testUpdateMethod"))
	daoTestSuite.addTest(DaoTestCase("testDeleteMethod"))		
	
	runner = unittest.TextTestRunner()
	runner.run(daoTestSuite)       
                                          
