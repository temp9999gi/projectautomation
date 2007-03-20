package lfis.framework.vo;

import laf.core.config.LConfiguration;
import laf.core.config.LConfigurationException;

import lfis.framework.env.KeyStore;
import lfis.framework.env.Path;

/**
 * <pre>
 *  
 *  
 * </pre>
 * 
 * @author LG CNS
 * 
 * @see PageVO
 */
public class PageIndexVO extends BaseVO {

	private int numOfRowPerPage;

	private int numOfIndexPerPage;

	private int currentPage;

	private int totalPage;

	private int totalRecords;

	private int prevPageIndex;

	private int currentPageIndex;

	private int nextPageIndex;

	private int totalPageIndex;

	private String pageNavigation;
	
	private int rowCntPerPage;

	private static final String scriptCode = 
		    "<script>" + KeyStore.LINE_SEP 
		  + "function fncGoPage(page){" + KeyStore.LINE_SEP
			+ "       var pageForm = null;" + KeyStore.LINE_SEP 
			+ "       pageForm = document.all['_currentPage'].form;" + KeyStore.LINE_SEP
			+ "       pageForm._currentPage.value = page;" + KeyStore.LINE_SEP 
			+ "       pageForm.fireSubmit();" 
			+ KeyStore.LINE_SEP + "}" 
			+ KeyStore.LINE_SEP 
			
			+ "function fncGetRowPerPage(){" + KeyStore.LINE_SEP
			+ "       var pageForm = null;" + KeyStore.LINE_SEP 
			+ "       pageForm = document.all['_rowCntPerPage'].form;" + KeyStore.LINE_SEP
			//+ "       alert('vvv - '+pageForm._rowCntPerPage.value);" + KeyStore.LINE_SEP 
			+ "       pageForm.fireSubmit();" 
			+ KeyStore.LINE_SEP + "}" 
			+ KeyStore.LINE_SEP 
			
			
			+ "</script>" + KeyStore.LINE_SEP;
	private static final String TABLE_START =
			 "<table width='100%' border='0' cellspacing='0' cellpadding='0'><tr><td width='25%' valign='middle' class='temp-text-small'>"+ KeyStore.LINE_SEP;

	private static final String TABLE_MIDDLE = "</td><td width='70%' class='temp-pagenav'>"+ KeyStore.LINE_SEP;;

	private static final String TABLE_END =
		 "</td><td width='5%' class='temp-pagenav'>&nbsp;</td></tr></table>"+ KeyStore.LINE_SEP;

	private static final String noResult = "데이터가 존재하지 않습니다." + KeyStore.LINE_SEP + "<input type='hidden' name='_currentPage' value='1'";


	/**
	 * Creates a new PageIndexVO object.
	 * 
	 * @param pageSpec
	 *          DOCUMENT ME!
	 *  
	 */
	public PageIndexVO(String pageSpec) {
		try {
			LConfiguration conf = LConfiguration.getInstance();
			this.numOfRowPerPage =  conf.getInt("/configuration/laf/page/spec<" + pageSpec + ">/row-size", KeyStore.DEFAULT_NUM_OF_ROW_PER_PAGE);
			this.numOfIndexPerPage =  conf.getInt("/configuration/laf/page/spec<" + pageSpec + ">/page-size", KeyStore.DEFAULT_NUM_OF_INDEX_PER_PAGE);
		} catch (LConfigurationException e) {
			this.numOfRowPerPage = KeyStore.DEFAULT_NUM_OF_ROW_PER_PAGE;
			this.numOfIndexPerPage = KeyStore.DEFAULT_NUM_OF_INDEX_PER_PAGE;
			e.printStackTrace();
		}
	}
	public PageIndexVO(String pageSpec, int pageRow) {
		try {
			LConfiguration conf = LConfiguration.getInstance();
			if (pageRow>0){
				this.numOfRowPerPage = pageRow;
			} else {
				this.numOfRowPerPage =  conf.getInt("/configuration/laf/page/spec<" + pageSpec + ">/row-size", KeyStore.DEFAULT_NUM_OF_ROW_PER_PAGE);				
			}						
			this.numOfIndexPerPage =  conf.getInt("/configuration/laf/page/spec<" + pageSpec + ">/page-size", KeyStore.DEFAULT_NUM_OF_INDEX_PER_PAGE);
		} catch (LConfigurationException e) {
			this.numOfRowPerPage = KeyStore.DEFAULT_NUM_OF_ROW_PER_PAGE;
			this.numOfIndexPerPage = KeyStore.DEFAULT_NUM_OF_INDEX_PER_PAGE;
			e.printStackTrace();
		}
	}
	
	public PageIndexVO(int numOfRowPerPage, int numOfIndexPerPage) {
		this.numOfRowPerPage = numOfRowPerPage;
		this.numOfIndexPerPage = numOfIndexPerPage;
	}
	/**
	 *
	 * 
	 * @return Returns the currentPage.
	 */
	public int getCurrentPage() {
		return currentPage;
	}

	/**
	 *
	 * 
	 * @param currentPage
	 *          The currentPage to set.
	 */
	public void setCurrentPage(int currentPage) {
		this.currentPage = currentPage;
	}

	/**
	 *
	 * 
	 * @return Returns the numOfIndexPerPage.
	 */
	public int getNumOfIndexPerPage() {
		return numOfIndexPerPage;
	}

	/**
	 *
	 * @param numOfIndexPerPage
	 *          The numOfIndexPerPage to set.
	 */
	public void setNumOfIndexPerPage(int numOfIndexPerPage) {
		this.numOfIndexPerPage = numOfIndexPerPage;
	}

	/**
	 * 
	 * @return Returns the numOfRowPerPage.
	 */
	public int getNumOfRowPerPage() {
		return numOfRowPerPage;
	}

	/**
	 * 
	 * @param numOfRowPerPage
	 *          The numOfRowPerPage to set.
	 */
	public void setNumOfRowPerPage(int numOfRowPerPage) {
		this.numOfRowPerPage = numOfRowPerPage;
	}

	/**
	 * 
	 * @return Returns the totalPage.
	 */
	public int getTotalPage() {
		return totalPage;
	}

	/**
	 * 
	 * @param totalPage
	 *          The totalPage to set.
	 */
	public void setTotalPage(int totalPage) {
		this.totalPage = totalPage;
	}

	/**
	 * 
	 * @return Returns the totalRecords.
	 */
	public int getTotalRecords() {
		return totalRecords;
	}

	/**
	 * 
	 * @param totalRecords
	 *          The totalRecords to set.
	 */
	public void setTotalRecords(int totalRecords) {
		this.totalRecords = totalRecords;
	}

	/**
	 * @return nextPageIndex
	 */
	public int getNextPageIndex() {
		return nextPageIndex;
	}

	public void setNextPageIndex(int nextPageIndex) {
		this.nextPageIndex = nextPageIndex;
	}

	public int getPrevPageIndex() {
		return prevPageIndex;
	}

	public void setPrevPageIndex(int prevPageIndex) {
		this.prevPageIndex = prevPageIndex;
	}

	public int getCurrentPageIndex() {
		return currentPageIndex;
	}

	public void setCurrentPageIndex(int currentPageIndex) {
		this.currentPageIndex = currentPageIndex;
	}

	public int getTotalPageIndex() {
		return totalPageIndex;
	}

	public void setTotalPageIndex(int totalPageIndex) {
		this.totalPageIndex = totalPageIndex;
	}
	
	public String getTotalPageNavigation(){
		return " <font size='2'>(총 " + this.getTotalRecords() +"건)</font>";
	}	
	public String getSetRowCnt(){
		if (this.getRowCntPerPage()==0){
			this.setRowCntPerPage(this.numOfRowPerPage);
		}
		String tmp = "<select size=1 class='temp-text-small' name='_rowCntPerPage' OnChange='fncGetRowPerPage()'>"
			         + "<option value='15' "+(this.getRowCntPerPage()==15?"selected":"")+" >15</option>"
			         + "<option value='20' "+(this.getRowCntPerPage()==20?"selected":"")+" >20</option>"
			         + "<option value='25' "+(this.getRowCntPerPage()==25?"selected":"")+" >25</option>"
			         + "<option value='30' "+(this.getRowCntPerPage()==30?"selected":"")+" >30</option>"
			         + "<option value='40' "+(this.getRowCntPerPage()==40?"selected":"")+" >40</option>"
			         + "</select>건/페이지";
		return tmp;
	}
	/**
	 * @return rowCntPerPage을 리턴합니다.
	 */
	public int getRowCntPerPage() {
		return rowCntPerPage;
	}
	/**
	 * @param rowCntPerPage 설정하려는 rowCntPerPage.
	 */
	public void setRowCntPerPage(int rowCntPerPage) {
		this.rowCntPerPage = rowCntPerPage;
	}
	
	
	public String getPageNavigation() {
		if (totalRecords == 0)
			return PageIndexVO.noResult;

		StringBuffer buf = new StringBuffer(PageIndexVO.scriptCode)
		.append("<input type='hidden' name='_currentPage' value='").append(currentPage).append("'>" + KeyStore.LINE_SEP)
		.append(PageIndexVO.TABLE_START)
		.append(this.getSetRowCnt())
		.append(this.getTotalPageNavigation())
		.append(PageIndexVO.TABLE_MIDDLE);
		
		if (currentPage != 1) {
			buf.append("<a href='javascript:fncGoPage(1)'><img src='").append(Path.IMG)
			     .append("/temp_pre2icon.gif' alt='맨앞으로' width='13' height='13' border='0' align='absmiddle'></a> " + KeyStore.LINE_SEP);
		}
		if (currentPage > numOfIndexPerPage) {
			buf.append("&nbsp;<a href='javascript:fncGoPage(").append(prevPageIndex).append(")'>").append("<img src='")
					.append(Path.IMG).append("/temp_previcon.gif' border='0' align='absmiddle'></a> " + KeyStore.LINE_SEP);
		}

		int pageEnd = 0;
		if (currentPageIndex >= totalPageIndex)
			pageEnd = totalPage + 1;
		else
			pageEnd = nextPageIndex;

		for (int i = currentPageIndex; i < pageEnd; i++) {
			if (i == currentPage) {
				buf.append("<font color = red><strong>").append(i).append("</strong></Font> ");
			} else {
				buf.append("<a href='javascript:fncGoPage(").append(i).append(")'>").append(i).append("</a>  ");
			}

		}
		buf.append("\n");
		if (currentPageIndex < totalPageIndex) {
			buf.append("<a href='javascript:fncGoPage(").append(nextPageIndex).append(")'>").append("<img src=\'")
					.append(Path.IMG).append("/temp_nexticon.gif' border='0' align='absmiddle'></a> " + KeyStore.LINE_SEP);
		}
		if (currentPage != totalPage) {
			buf.append("<a href='javascript:fncGoPage(").append(totalPage).append(")'>").append("<img src=\'")
			    .append(Path.IMG).append("/temp_next2icon.gif' width='13' height='13' border='0' align='absmiddle'></a>" + KeyStore.LINE_SEP);
		}
		buf.append(PageIndexVO.TABLE_END);
		pageNavigation = buf.toString();
		return pageNavigation;
	}

	/**
	 * <pre>
	 *  
	 *  
	 * </pre>
	 */
	public void calcIndex() {

		if ((this.totalRecords == 0) || (this.numOfRowPerPage < 0)) {

			this.totalPage = 0;
			this.currentPage = 1;
		} else {
			this.totalPage = (int) Math.ceil((double) (totalRecords) / numOfRowPerPage);

			if (this.currentPage > this.totalPage) {
				this.currentPage = this.totalPage;
			}
			this.totalPageIndex = totalPage
					- (totalPage % numOfIndexPerPage == 0 ? numOfIndexPerPage : totalPage % numOfIndexPerPage) + 1;
			this.currentPageIndex = currentPage
					- (currentPage % numOfIndexPerPage == 0 ? numOfIndexPerPage : currentPage % numOfIndexPerPage) + 1;
			//this.nextPageIndex = ((int) Math.ceil((double) currentPage / numOfRowPerPage)) * numOfIndexPerPage + 1;
			this.nextPageIndex = ((int) Math.ceil((double) currentPage / numOfIndexPerPage)) * numOfIndexPerPage + 1;
			nextPageIndex = (nextPageIndex > totalPage) ? totalPageIndex : nextPageIndex;
			//this.prevPageIndex = ((int) Math.ceil((double) currentPage / numOfRowPerPage) - 2) * numOfIndexPerPage + 1;
			this.prevPageIndex = ((int) Math.ceil((double) currentPage / numOfIndexPerPage) - 2) * numOfIndexPerPage + 1;
			prevPageIndex = (prevPageIndex < 0) ? 1 : prevPageIndex;
			//+ 1 )*numOfIndexPerPage + 1;

		}
	}

	public static void main(String[] args) {
		PageIndexVO page = new PageIndexVO(20, 20);
		page.setTotalRecords(19994);
		page.setCurrentPage(32);
		page.calcIndex();
		System.out.println("total cnt:"+page.getTotalPage());
		System.out.println("next:"+page.getNextPageIndex());
		System.out.println("current:"+page.getCurrentPageIndex());
		System.out.println("pre:"+page.getPrevPageIndex());
		System.out.println("total:"+page.getTotalPageIndex());
		int next = (int) Math.ceil((double) (32) / 10);
//		int next1 = (int) Math.ceil((double) (2) / 10);
		System.out.println(next);
//		System.out.println(2000 % 10);
	}

}