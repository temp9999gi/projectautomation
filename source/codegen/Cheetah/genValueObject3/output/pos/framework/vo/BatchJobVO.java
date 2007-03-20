package lfis.framework.vo;

import java.io.UnsupportedEncodingException;
import java.util.Date;
import java.util.StringTokenizer;

import laf.support.collection.LData;

//java.util 패키지 또는 java.sql 패키지의 변수를 사용하는 경우 사용하는 Class만 직접 import하세요

public class BatchJobVO extends lfis.framework.vo.BaseVO {

	/****************************************************
	 연관된 TABLE 명 : [ TFE_SYST06 ] 
	 ****************************************************/

	/*****************************************************
	 Attributes 
	 *****************************************************/

	private long batchWorkSno;

	private String workSchdDate; // 작업예정일시 

	private String menuCd; // 메뉴코드 

	private String fulfilParam; // 실행파라미터 

	private Date workDate; // 작업일시 

	private String workRsltFg; // 처리결과구분 

	private String errTypeFg; // 에러유형구분 

	private String workLog; // 작업로그 

	private String regiUserId; // 등록자ID 

	private Date regiDate; // 등록일시 

	private String finalModiUserId; // 최종수정자ID 

	private Date finalModiDate; // 최종수정일시 

	private String url; // url

	public static final String WORK_FG_NOT_RUN = "10";

	public static final String WORK_FG_SUCCESS = "20";

	public static final String WORK_FG_FAIL = "30";

	public static final String ERR_TYPE_USER = "10";

	public static final String ERR_TYPE_SYS = "20";

	/******************************************************
	 Set & Get Method List 
	 ******************************************************/

	public void setBatchWorkSno(long batchWorkSno) {
		this.batchWorkSno = batchWorkSno;
	}

	public long getBatchWorkSno() {
		return this.batchWorkSno;
	}

	/** 
	 * 작업예정일시 정보를 설정하는 메소드
	 * @param Date  workSchdDate  :  작업예정일시
	 */

	public void setWorkSchdDate(String workSchdDate) {
		this.workSchdDate = workSchdDate;
	}

	/** 
	 *  작업예정일시 정보의 값을 반환하는 메소드 
	 * @return  Date   workSchdDate  :  작업예정일시 
	 */

	public String getWorkSchdDate() {
		return this.workSchdDate;
	}

	/** 
	 * 메뉴코드 정보를 설정하는 메소드
	 * @param String  menuCd  :  메뉴코드
	 */

	public void setMenuCd(String menuCd) {
		this.menuCd = menuCd;
	}

	/** 
	 *  메뉴코드 정보의 값을 반환하는 메소드 
	 * @return  String   menuCd  :  메뉴코드 
	 */

	public String getMenuCd() {
		return this.menuCd;
	}

	/** 
	 * 실행파라미터 정보를 설정하는 메소드
	 * @param String  fulfilParam  :  실행파라미터
	 */

	public void setFulfilParam(String fulfilParam) {
		this.fulfilParam = fulfilParam;
	}

	/** 
	 *  실행파라미터 정보의 값을 반환하는 메소드 
	 * @return  String   fulfilParam  :  실행파라미터 
	 */

	public String getFulfilParam() {
		return this.fulfilParam;
	}

	public LData getFulfilParamMap() {
		LData data = new LData();
		StringTokenizer st = new StringTokenizer(this.fulfilParam, "&");
		while (st.hasMoreTokens()) {
			String[] keyVal = st.nextToken().split("=");
			if (keyVal.length == 2)
				data.put(keyVal[0].trim(), keyVal[1].trim());
			else
				data.put(keyVal[0].trim(), "");
		}
		return data;
	}

	/** 
	 * 작업일시 정보를 설정하는 메소드
	 * @param Date  workDate  :  작업일시
	 */

	public void setWorkDate(Date workDate) {
		this.workDate = workDate;
	}

	/** 
	 *  작업일시 정보의 값을 반환하는 메소드 
	 * @return  Date   workDate  :  작업일시 
	 */

	public Date getWorkDate() {
		return this.workDate;
	}

	/** 
	 * 처리결과구분 정보를 설정하는 메소드
	 * @param String  workRsltFg  :  처리결과구분
	 */

	public void setWorkRsltFg(String workRsltFg) {
		this.workRsltFg = workRsltFg;
	}

	/** 
	 *  처리결과구분 정보의 값을 반환하는 메소드 
	 * @return  String   workRsltFg  :  처리결과구분 
	 */

	public String getWorkRsltFg() {
		return this.workRsltFg;
	}

	/** 
	 * 에러유형구분 정보를 설정하는 메소드
	 * @param String  errTypeFg  :  에러유형구분
	 */

	public void setErrTypeFg(String errTypeFg) {
		this.errTypeFg = errTypeFg;
	}

	/** 
	 *  에러유형구분 정보의 값을 반환하는 메소드 
	 * @return  String   errTypeFg  :  에러유형구분 
	 */

	public String getErrTypeFg() {
		return this.errTypeFg;
	}

	/** 
	 * 작업로그 정보를 설정하는 메소드
	 * @param String  workLog  :  작업로그
	 */

	public void setWorkLog(String workLog) {
		byte[] logs = workLog.getBytes();
		if (logs.length > 200) {
			try {
				this.workLog = new String(logs, 0, 200, "EUC-KR");
			} catch (UnsupportedEncodingException e) {
				e.printStackTrace();
				this.workLog = new String(logs, 0, 200);
			}
		} else {
			this.workLog = workLog;
		}
	}

	/** 
	 *  작업로그 정보의 값을 반환하는 메소드 
	 * @return  String   workLog  :  작업로그 
	 */

	public String getWorkLog() {
		return this.workLog;
	}

	/** 
	 * 등록자ID 정보를 설정하는 메소드
	 * @param String  regiUserId  :  등록자ID
	 */

	public void setRegiUserId(String regiUserId) {
		this.regiUserId = regiUserId;
	}

	/** 
	 *  등록자ID 정보의 값을 반환하는 메소드 
	 * @return  String   regiUserId  :  등록자ID 
	 */

	public String getRegiUserId() {
		return this.regiUserId;
	}

	/** 
	 * 등록일시 정보를 설정하는 메소드
	 * @param Date  regiDate  :  등록일시
	 */

	public void setRegiDate(Date regiDate) {
		this.regiDate = regiDate;
	}

	/** 
	 *  등록일시 정보의 값을 반환하는 메소드 
	 * @return  Date   regiDate  :  등록일시 
	 */

	public Date getRegiDate() {
		return this.regiDate;
	}

	/** 
	 * 최종수정자ID 정보를 설정하는 메소드
	 * @param String  finalModiUserId  :  최종수정자ID
	 */

	public void setFinalModiUserId(String finalModiUserId) {
		this.finalModiUserId = finalModiUserId;
	}

	/** 
	 *  최종수정자ID 정보의 값을 반환하는 메소드 
	 * @return  String   finalModiUserId  :  최종수정자ID 
	 */

	public String getFinalModiUserId() {
		return this.finalModiUserId;
	}

	/** 
	 * 최종수정일시 정보를 설정하는 메소드
	 * @param Date  finalModiDate  :  최종수정일시
	 */

	public void setFinalModiDate(Date finalModiDate) {
		this.finalModiDate = finalModiDate;
	}

	/** 
	 *  최종수정일시 정보의 값을 반환하는 메소드 
	 * @return  Date   finalModiDate  :  최종수정일시 
	 */

	public Date getFinalModiDate() {
		return this.finalModiDate;
	}

	/**
	 * @return url을 리턴합니다.
	 */
	public String getUrl() {
		return url;
	}

	/**
	 * @param url 설정하려는 url.
	 */
	public void setUrl(String url) {
		this.url = url;
	}

	/******************************************************
	 Constructors
	 ******************************************************/

	/** 
	 *   Default Constructor 
	 */

	public BatchJobVO() {

	}

}