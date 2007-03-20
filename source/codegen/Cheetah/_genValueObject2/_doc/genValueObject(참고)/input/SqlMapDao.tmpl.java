package com.ibatis.jpetstore.persistence.sqlmapdao;

import com.ibatis.dao.client.DaoManager;
import com.ibatis.jpetstore.domain.${className};
import com.ibatis.jpetstore.persistence.iface.${className}Dao;

public class ${className}SqlMapDao extends BaseSqlMapDao implements ${className}Dao {

  public ${className}SqlMapDao(DaoManager daoManager) {
    super(daoManager);
  }

  public ${className} get${className}(String username) {
    return (${className}) queryForObject("getAccountByUsername", username);
  }

  public ${className} get${className}(String username, String password) {
    ${className} ${lowerClassName} = new ${className}();
    ${lowerClassName}.setUsername(username);
    ${lowerClassName}.setPassword(password);
    return (${className}) queryForObject("getAccountByUsernameAndPassword", ${lowerClassName});
  }

  public void insert${className}(${className} ${lowerClassName}) {
    update("insertAccount", ${lowerClassName});
    update("insertProfile", ${lowerClassName});
    update("insertSignon", ${lowerClassName});
  }

  public void update${className}(${className} ${lowerClassName}) {
    update("updateAccount", ${lowerClassName});
    update("updateProfile", ${lowerClassName});

    if (${lowerClassName}.getPassword() != null && ${lowerClassName}.getPassword().length() > 0) {
      update("updateSignon", ${lowerClassName});
    }
  }


}
