package com.ibatis.jpetstore.persistence.sqlmapdao;

import com.ibatis.dao.client.DaoManager;
import com.ibatis.jpetstore.domain.Account;
import com.ibatis.jpetstore.persistence.iface.AccountDao;

public class AccountSqlMapDao extends BaseSqlMapDao implements AccountDao {

  public AccountSqlMapDao(DaoManager daoManager) {
    super(daoManager);
  }

  public Account getAccount(String username) {
  }

  public Account getAccount(String username, String password) {
  }

  public void insertAccount(Account account) {
  }

  public void updateAccount(Account account) {
  }

  public void deleteAccount(Account account) {
  }

  
}

