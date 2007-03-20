package lfis.framework.vo;

import java.util.Iterator;
import java.util.List;

/**
 * <pre>
 * </pre>
 * 
 * @author LG CNS
 * @see PageIndexVO
 */

public class PageVO extends BaseVO {

	private PageIndexVO pageIndex;

	private List pagedList;

	public PageVO(PageIndexVO pageIndex, List pagedList) {
		this.pageIndex = pageIndex;
		this.pagedList = pagedList;
	}

	/**
	 * <pre>
	 * 
	 *  
	 * </pre>
	 * 
	 * @return Returns the pagedList.
	 */
	public List getPagedList() {
		return pagedList;
	}

	/**
	 * <pre>
	 * 
	 *  
	 * </pre>
	 * 
	 * @param pagedList
	 *          The pagedList to set.
	 */
	public void setPagedList(List pagedList) {
		this.pagedList = pagedList;
	}

	/**
	 * <pre>
	 * 
	 *  
	 * </pre>
	 * 
	 * @return Returns the pageIndex.
	 */
	public PageIndexVO getPageIndex() {
		return pageIndex;
	}

	/**
	 * <pre>
	 * 
	 *  
	 * </pre>
	 * 
	 * @param pageIndex
	 *          The pageIndex to set.
	 */
	public void setPageIndex(PageIndexVO pageIndex) {
		this.pageIndex = pageIndex;
	}

	public String toString() {
		StringBuffer temp = new StringBuffer(super.toString());
		if (pagedList != null) {
			Iterator it = pagedList.iterator();
			Object obj;
			while (it.hasNext()) {
				temp.append(it.next().toString());

			}
		}
		return temp.toString();
	}
}