/******************************************************************* 
 * 표준지방재정정보시스템 *  
 * Copyright (c) 2005 ~ 2006 by LG CNS, Inc. 
 * All rights reserved. 
 ******************************************************************* 
 * $Id: ICdDAO.java,v 1.1 2006/10/29 09:13:18 kusung25 Exp $
 *  
 * $Log: ICdDAO.java,v $
 * Revision 1.1  2006/10/29 09:13:18  kusung25
 * *** empty log message ***
 *
 * Revision 1.2  2006/07/10 12:59:05  kusung25
 * *** empty log message ***
 *
/******************************************************************* 
 * 표준지방재정정보시스템 *  
 * Copyright (c) 2005 ~ 2006 by LG CNS, Inc. 
 * All rights reserved. 
 ******************************************************************* 
 * $Id: ICdDAO.java,v 1.1 2006/10/29 09:13:18 kusung25 Exp $
 *  
 * Revision 1.1  2005/09/07 23:01:16  dhychang
/******************************************************************* 
 * 표준지방재정정보시스템 *  
 * Copyright (c) 2005 ~ 2006 by LG CNS, Inc. 
 * All rights reserved. 
 ******************************************************************* 
 * $Id: ICdDAO.java,v 1.1 2006/10/29 09:13:18 kusung25 Exp $
 *  
 * *** empty log message ***
/******************************************************************* 
 * 표준지방재정정보시스템 *  
 * Copyright (c) 2005 ~ 2006 by LG CNS, Inc. 
 * All rights reserved. 
 ******************************************************************* 
 * $Id: ICdDAO.java,v 1.1 2006/10/29 09:13:18 kusung25 Exp $
 *  
 *
 * 
 ******************************************************************/
package lfis.sample.cd.dao;
import java.util.List;
import lfis.framework.vo.PageVO;
import lfis.sample.cd.vo.CdVO;
/**
 * 코드 리스트를 조회하는 CMD 클래스이다.
 * 
 * @author $$Author: kusung25 $$
 * @version $$Revision: 1.1 $$
 */
public interface ICdDAO {
	public void createCd(CdVO cdVO);
	public void updateCd(CdVO cdVO);
	public void deleteCd(CdVO cdVO);
	
	public List findCdListFC(String cdTpId);
	public PageVO findCdList(CdVO cdVO);
	public List findExcelCdList(CdVO cdVO);
	public CdVO findCd(CdVO cdTO);
}