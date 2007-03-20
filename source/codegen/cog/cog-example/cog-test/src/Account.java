package com.ibatis.jpetstore.domain;

import java.io.Serializable;


public class Account implements Serializable {
  //[[[cog import dyno_cog; dyno_cog.writeProperty2('Account', cog.inFile) ]]]
  private String id;
  private Integer revNum;
  private String subject;
  private Date modDate;

  public String getId() {
    return id;
  }
  public void setId(String id) {
    this.id = id;
  }


  public Integer getRevnum() {
    return revNum;
  }
  public void setRevnum(String revNum) {
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
  public void setModdate(String modDate) {
    this.modDate = modDate;
  }

  //[[[end]]]
  
  
  
  public String getUsername() {
    return username;
  }

  public void setUsername(String username) {
    this.username = username;
  }

  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }

}
