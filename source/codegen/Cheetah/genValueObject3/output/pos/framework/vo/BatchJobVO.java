package lfis.framework.vo;

import java.io.UnsupportedEncodingException;
import java.util.Date;
import java.util.StringTokenizer;

import laf.support.collection.LData;

//java.util ��Ű�� �Ǵ� java.sql ��Ű���� ������ ����ϴ� ��� ����ϴ� Class�� ���� import�ϼ���

public class BatchJobVO extends lfis.framework.vo.BaseVO {

	/****************************************************
	 ������ TABLE �� : [ TFE_SYST06 ] 
	 ****************************************************/

	/*****************************************************
	 Attributes 
	 *****************************************************/

	private long batchWorkSno;

	private String workSchdDate; // �۾������Ͻ� 

	private String menuCd; // �޴��ڵ� 

	private String fulfilParam; // �����Ķ���� 

	private Date workDate; // �۾��Ͻ� 

	private String workRsltFg; // ó��������� 

	private String errTypeFg; // ������������ 

	private String workLog; // �۾��α� 

	private String regiUserId; // �����ID 

	private Date regiDate; // ����Ͻ� 

	private String finalModiUserId; // ����������ID 

	private Date finalModiDate; // ���������Ͻ� 

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
	 * �۾������Ͻ� ������ �����ϴ� �޼ҵ�
	 * @param Date  workSchdDate  :  �۾������Ͻ�
	 */

	public void setWorkSchdDate(String workSchdDate) {
		this.workSchdDate = workSchdDate;
	}

	/** 
	 *  �۾������Ͻ� ������ ���� ��ȯ�ϴ� �޼ҵ� 
	 * @return  Date   workSchdDate  :  �۾������Ͻ� 
	 */

	public String getWorkSchdDate() {
		return this.workSchdDate;
	}

	/** 
	 * �޴��ڵ� ������ �����ϴ� �޼ҵ�
	 * @param String  menuCd  :  �޴��ڵ�
	 */

	public void setMenuCd(String menuCd) {
		this.menuCd = menuCd;
	}

	/** 
	 *  �޴��ڵ� ������ ���� ��ȯ�ϴ� �޼ҵ� 
	 * @return  String   menuCd  :  �޴��ڵ� 
	 */

	public String getMenuCd() {
		return this.menuCd;
	}

	/** 
	 * �����Ķ���� ������ �����ϴ� �޼ҵ�
	 * @param String  fulfilParam  :  �����Ķ����
	 */

	public void setFulfilParam(String fulfilParam) {
		this.fulfilParam = fulfilParam;
	}

	/** 
	 *  �����Ķ���� ������ ���� ��ȯ�ϴ� �޼ҵ� 
	 * @return  String   fulfilParam  :  �����Ķ���� 
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
	 * �۾��Ͻ� ������ �����ϴ� �޼ҵ�
	 * @param Date  workDate  :  �۾��Ͻ�
	 */

	public void setWorkDate(Date workDate) {
		this.workDate = workDate;
	}

	/** 
	 *  �۾��Ͻ� ������ ���� ��ȯ�ϴ� �޼ҵ� 
	 * @return  Date   workDate  :  �۾��Ͻ� 
	 */

	public Date getWorkDate() {
		return this.workDate;
	}

	/** 
	 * ó��������� ������ �����ϴ� �޼ҵ�
	 * @param String  workRsltFg  :  ó���������
	 */

	public void setWorkRsltFg(String workRsltFg) {
		this.workRsltFg = workRsltFg;
	}

	/** 
	 *  ó��������� ������ ���� ��ȯ�ϴ� �޼ҵ� 
	 * @return  String   workRsltFg  :  ó��������� 
	 */

	public String getWorkRsltFg() {
		return this.workRsltFg;
	}

	/** 
	 * ������������ ������ �����ϴ� �޼ҵ�
	 * @param String  errTypeFg  :  ������������
	 */

	public void setErrTypeFg(String errTypeFg) {
		this.errTypeFg = errTypeFg;
	}

	/** 
	 *  ������������ ������ ���� ��ȯ�ϴ� �޼ҵ� 
	 * @return  String   errTypeFg  :  ������������ 
	 */

	public String getErrTypeFg() {
		return this.errTypeFg;
	}

	/** 
	 * �۾��α� ������ �����ϴ� �޼ҵ�
	 * @param String  workLog  :  �۾��α�
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
	 *  �۾��α� ������ ���� ��ȯ�ϴ� �޼ҵ� 
	 * @return  String   workLog  :  �۾��α� 
	 */

	public String getWorkLog() {
		return this.workLog;
	}

	/** 
	 * �����ID ������ �����ϴ� �޼ҵ�
	 * @param String  regiUserId  :  �����ID
	 */

	public void setRegiUserId(String regiUserId) {
		this.regiUserId = regiUserId;
	}

	/** 
	 *  �����ID ������ ���� ��ȯ�ϴ� �޼ҵ� 
	 * @return  String   regiUserId  :  �����ID 
	 */

	public String getRegiUserId() {
		return this.regiUserId;
	}

	/** 
	 * ����Ͻ� ������ �����ϴ� �޼ҵ�
	 * @param Date  regiDate  :  ����Ͻ�
	 */

	public void setRegiDate(Date regiDate) {
		this.regiDate = regiDate;
	}

	/** 
	 *  ����Ͻ� ������ ���� ��ȯ�ϴ� �޼ҵ� 
	 * @return  Date   regiDate  :  ����Ͻ� 
	 */

	public Date getRegiDate() {
		return this.regiDate;
	}

	/** 
	 * ����������ID ������ �����ϴ� �޼ҵ�
	 * @param String  finalModiUserId  :  ����������ID
	 */

	public void setFinalModiUserId(String finalModiUserId) {
		this.finalModiUserId = finalModiUserId;
	}

	/** 
	 *  ����������ID ������ ���� ��ȯ�ϴ� �޼ҵ� 
	 * @return  String   finalModiUserId  :  ����������ID 
	 */

	public String getFinalModiUserId() {
		return this.finalModiUserId;
	}

	/** 
	 * ���������Ͻ� ������ �����ϴ� �޼ҵ�
	 * @param Date  finalModiDate  :  ���������Ͻ�
	 */

	public void setFinalModiDate(Date finalModiDate) {
		this.finalModiDate = finalModiDate;
	}

	/** 
	 *  ���������Ͻ� ������ ���� ��ȯ�ϴ� �޼ҵ� 
	 * @return  Date   finalModiDate  :  ���������Ͻ� 
	 */

	public Date getFinalModiDate() {
		return this.finalModiDate;
	}

	/**
	 * @return url�� �����մϴ�.
	 */
	public String getUrl() {
		return url;
	}

	/**
	 * @param url �����Ϸ��� url.
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