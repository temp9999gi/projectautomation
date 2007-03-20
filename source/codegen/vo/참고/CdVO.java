package lfis.sample.cd.vo;

import lfis.framework.vo.BaseVO;

public class CdVO extends BaseVO {

	private String cdId;

	private String cdNm;

	private String cdTpId;
	
	private String cdTpNm;

	private String delFg;

	private String updateDate;

	private String rowStatus;
	
	private int currentPage;
	

	public CdVO() {
	}
	
	/**
	 * @return cdId을 리턴합니다.
	 */
	public String getCdId() {
		return cdId;
	}
	/**
	 * @param cdId 설정하려는 cdId.
	 */
	public void setCdId(String cdId) {
		this.cdId = cdId;
	}
	/**
	 * @return cdNm을 리턴합니다.
	 */
	public String getCdNm() {
		return cdNm;
	}
	/**
	 * @param cdNm 설정하려는 cdNm.
	 */
	public void setCdNm(String cdNm) {
		this.cdNm = cdNm;
	}
	/**
	 * @return cdTpId을 리턴합니다.
	 */
	public String getCdTpId() {
		return cdTpId;
	}
	/**
	 * @param cdTpId 설정하려는 cdTpId.
	 */
	public void setCdTpId(String cdTpId) {
		this.cdTpId = cdTpId;
	}
	
	/**
	 * @return cdTpNm을 리턴합니다.
	 */
	public String getCdTpNm() {
		return cdTpNm;
	}
	/**
	 * @param cdTpNm 설정하려는 cdTpNm.
	 */
	public void setCdTpNm(String cdTpNm) {
		this.cdTpNm = cdTpNm;
	}
	/**
	 * @return delFg을 리턴합니다.
	 */
	public String getDelFg() {
		return delFg;
	}
	/**
	 * @param delFg 설정하려는 delFg.
	 */
	public void setDelFg(String delFg) {
		this.delFg = delFg;
	}
	/**
	 * @return updateDate을 리턴합니다.
	 */
	public String getUpdateDate() {
		return updateDate;
	}
	/**
	 * @param updateDate 설정하려는 updateDate.
	 */
	public void setUpdateDate(String updateDate) {
		this.updateDate = updateDate;
	}
	/**
	 * @return rowStatus을 리턴합니다.
	 */
	public String getRowStatus() {
		return rowStatus;
	}
	/**
	 * @param rowStatus 설정하려는 rowStatus.
	 */
	public void setRowStatus(String rowStatus) {
		this.rowStatus = rowStatus;
	}
	/**
	 * @return currentPage을 리턴합니다.
	 */
	public int getCurrentPage() {
		return currentPage;
	}
	/**
	 * @param currentPage 설정하려는 currentPage.
	 */
	public void setCurrentPage(int currentPage) {
		this.currentPage = currentPage;
	}
}
