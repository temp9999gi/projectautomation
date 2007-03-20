package pos.sysa.biz.account.vo;

import pos.framework.vo.BaseVO;

public class Account extends BaseVO {

	public Account() {
	}

	/*****************************************************
	  Attributes
	 *****************************************************/
 	private String id;
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}

 	private String name;
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}

 	private String description;
	public String getDescription() {
		return description;
	}
	public void setDescription(String description) {
		this.description = description;
	}

 	private Date modDate;
	public Date getModDate() {
		return modDate;
	}
	public void setModDate(String modDate) {
		this.modDate = modDate;
	}

}
