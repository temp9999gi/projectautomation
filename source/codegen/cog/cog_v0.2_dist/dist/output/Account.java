package com.ibatis.jpetstore.domain;

import java.io.Serializable;

public class Account implements Serializable {
  //[[[cog from posCogApp import posCog; posCog.writeProperty2('Account', cog.inFile) ]]]
    private String id;
    private Integer revNum;
    private String subject;
    private Date modDate;
  111
    public String getId() {
      return id;
    }
    public void setId(String id) {
      this.id = id;
    }

    public Integer getRevnum() {
      return revNum;
    }
    public void setRevnum(Integer revNum) {
      this.revNum = revNum;
    }

    public String getSubject() {
      return subject;
    }
    public void setSubject(String subject) {
      this.subject = subject;
    }

    public Date getModdate() {
      return modDate;
    }
    public void setModdate(Date modDate) {
      this.modDate = modDate;
    }

  //[[[end]]]  

}