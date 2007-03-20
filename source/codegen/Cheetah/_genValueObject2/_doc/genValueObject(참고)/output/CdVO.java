package lfis.sample.cd.vo;

import lfis.framework.vo.BaseVO;

public class CdVO extends BaseVO {

	public CdVO() {
	}

	/*****************************************************
	  Attributes
	 *****************************************************/
 	private String   cdId;
	public String getCdId() {
		return cdId;
	}
	public void setCdId(String cdId) {
		this.cdId = cdId;
	}

 	private String   cdNm;
	public String getCdNm() {
		return cdNm;
	}
	public void setCdNm(String cdNm) {
		this.cdNm = cdNm;
	}

 	private int   currentPage;
	public int getCurrentPage() {
		return currentPage;
	}
	public void setCurrentPage(String currentPage) {
		this.currentPage = currentPage;
	}


}
