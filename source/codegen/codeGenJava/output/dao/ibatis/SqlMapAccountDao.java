package org.springframework.samples.jpetstore.dao.ibatis;

import java.util.List;

import org.springframework.dao.DataAccessException;
import org.springframework.orm.ibatis.support.SqlMapClientDaoSupport;
import org.springframework.samples.jpetstore.dao.AccountDao;
import org.springframework.samples.jpetstore.domain.Account;

public class SqlMapAccountDao extends SqlMapClientDaoSupport implements AccountDao {

  public Account getAccount(String username) throws DataAccessException {
    return (Account) getSqlMapClientTemplate().queryForObject("getAccount", username);
  }

  public Account getAccount(String username, String password) throws DataAccessException {
    Account account = new Account();
    account.setUsername(username);
    account.setPassword(password);
    return (Account) getSqlMapClientTemplate().queryForObject("getAccount", account);
  }

  public void insertAccount(Account account) throws DataAccessException {
    getSqlMapClientTemplate().insert("insertAccount", account);
    getSqlMapClientTemplate().insert("insertProfile", account);
    getSqlMapClientTemplate().insert("insertSignon", account);
  }

  public void updateAccount(Account account) throws DataAccessException {
    getSqlMapClientTemplate().update("updateAccount", account, 1);
    getSqlMapClientTemplate().update("updateProfile", account, 1);
    getSqlMapClientTemplate().update("updateSignon", account, 1);
  }

  public List getUsernameList() throws DataAccessException {
    return getSqlMapClientTemplate().queryForList("getUsernameList", null);
  }


}
