package lfis.sample.cd.vo;

import lfis.framework.vo.BaseVO;

public class Dwarf extends BaseVO {

	public Dwarf() {
	}

	/*****************************************************
	  Attributes
	 *****************************************************/
 	private int   dwarfId;
	public int getDwarfId() {
		return dwarfId;
	}
	public void setDwarfId(String dwarfId) {
		this.dwarfId = dwarfId;
	}

 	private String   dwarfName;
	public String getDwarfName() {
		return dwarfName;
	}
	public void setDwarfName(String dwarfName) {
		this.dwarfName = dwarfName;
	}

 	private int   born;
	public int getBorn() {
		return born;
	}
	public void setBorn(String born) {
		this.born = born;
	}

 	private int   homeId;
	public int getHomeId() {
		return homeId;
	}
	public void setHomeId(String homeId) {
		this.homeId = homeId;
	}

 	private String   homeName;
	public String getHomeName() {
		return homeName;
	}
	public void setHomeName(String homeName) {
		this.homeName = homeName;
	}

 	private int   spouseId;
	public int getSpouseId() {
		return spouseId;
	}
	public void setSpouseId(String spouseId) {
		this.spouseId = spouseId;
	}

 	private String   spouseName;
	public String getSpouseName() {
		return spouseName;
	}
	public void setSpouseName(String spouseName) {
		this.spouseName = spouseName;
	}


}