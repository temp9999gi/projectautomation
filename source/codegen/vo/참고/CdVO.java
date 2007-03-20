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
	 * @return cdId�� �����մϴ�.
	 */
	public String getCdId() {
		return cdId;
	}
	/**
	 * @param cdId �����Ϸ��� cdId.
	 */
	public void setCdId(String cdId) {
		this.cdId = cdId;
	}
	/**
	 * @return cdNm�� �����մϴ�.
	 */
	public String getCdNm() {
		return cdNm;
	}
	/**
	 * @param cdNm �����Ϸ��� cdNm.
	 */
	public void setCdNm(String cdNm) {
		this.cdNm = cdNm;
	}
	/**
	 * @return cdTpId�� �����մϴ�.
	 */
	public String getCdTpId() {
		return cdTpId;
	}
	/**
	 * @param cdTpId �����Ϸ��� cdTpId.
	 */
	public void setCdTpId(String cdTpId) {
		this.cdTpId = cdTpId;
	}
	
	/**
	 * @return cdTpNm�� �����մϴ�.
	 */
	public String getCdTpNm() {
		return cdTpNm;
	}
	/**
	 * @param cdTpNm �����Ϸ��� cdTpNm.
	 */
	public void setCdTpNm(String cdTpNm) {
		this.cdTpNm = cdTpNm;
	}
	/**
	 * @return delFg�� �����մϴ�.
	 */
	public String getDelFg() {
		return delFg;
	}
	/**
	 * @param delFg �����Ϸ��� delFg.
	 */
	public void setDelFg(String delFg) {
		this.delFg = delFg;
	}
	/**
	 * @return updateDate�� �����մϴ�.
	 */
	public String getUpdateDate() {
		return updateDate;
	}
	/**
	 * @param updateDate �����Ϸ��� updateDate.
	 */
	public void setUpdateDate(String updateDate) {
		this.updateDate = updateDate;
	}
	/**
	 * @return rowStatus�� �����մϴ�.
	 */
	public String getRowStatus() {
		return rowStatus;
	}
	/**
	 * @param rowStatus �����Ϸ��� rowStatus.
	 */
	public void setRowStatus(String rowStatus) {
		this.rowStatus = rowStatus;
	}
	/**
	 * @return currentPage�� �����մϴ�.
	 */
	public int getCurrentPage() {
		return currentPage;
	}
	/**
	 * @param currentPage �����Ϸ��� currentPage.
	 */
	public void setCurrentPage(int currentPage) {
		this.currentPage = currentPage;
	}
}
