package org.springframework.samples.jpetstore.dao.ibatis;

import java.util.List;

import org.springframework.dao.DataAccessException;
import org.springframework.orm.ibatis.support.SqlMapClientDaoSupport;
import org.springframework.samples.jpetstore.dao.AccountDao;
import org.springframework.samples.jpetstore.domain.Account;

public class SqlMapAccountDao extends SqlMapClientDaoSupport implements AccountDao {

  public Account getAccount(String username) {
    return (Account) getSqlMapClientTemplate().queryForObject("getAccount", username);
  }

  public Account getAccount(String username) {
    return (Account) getSqlMapClientTemplate().queryForObject("getAccount", username);
  }

  public void insertAccount(Account account) {
    return (Account) getSqlMapClientTemplate().queryForObject("getAccount", username);
  }

  public void updateAccount(Account account) {
    return (Account) getSqlMapClientTemplate().queryForObject("getAccount", username);
  }

  public List getUsernameList() {
    return (Account) getSqlMapClientTemplate().queryForObject("getAccount", username);
  }


}
