/*******************************************************************
 * 표준지방재정정보시스템 *
 * Copyright (c) 2005 ~ 2006 by LG CNS, Inc.
 * All rights reserved.
 *******************************************************************
 * $Id: CdDAO.java,v 1.1 2006/12/01 14:02:33 kusung25 Exp $
 *
 * $Log: CdDAO.java,v $
 * Revision 1.1  2006/12/01 14:02:33  kusung25
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
 * $Id: CdDAO.java,v 1.1 2006/12/01 14:02:33 kusung25 Exp $
 *
 * Revision 1.2  2005/09/08 00:02:48  dhychang
/*******************************************************************
 * 표준지방재정정보시스템 *
 * Copyright (c) 2005 ~ 2006 by LG CNS, Inc.
 * All rights reserved.
 *******************************************************************
 * $Id: CdDAO.java,v 1.1 2006/12/01 14:02:33 kusung25 Exp $
 *
 * *** empty log message ***
/*******************************************************************
 * 표준지방재정정보시스템 *
 * Copyright (c) 2005 ~ 2006 by LG CNS, Inc.
 * All rights reserved.
 *******************************************************************
 * $Id: CdDAO.java,v 1.1 2006/12/01 14:02:33 kusung25 Exp $
 ******************************************************************/
package lfis.sample.cd.dao;

import java.util.List;

import lfis.framework.dao.SuperOracleDAO;
import lfis.framework.vo.PageVO;
import lfis.sample.cd.vo.CdVO;

/**
 * 코드 리스트를 조회하는 CMD 클래스이다.
 *
 * @author $$Author: kusung25 $$
 * @version $$Revision: 1.1 $$
 */

public class CdDAO extends SuperOracleDAO implements ICdDAO {

	public void createCd(CdVO cdVO) {
		insert("createCd", cdVO);
	}

	public void updateCd(CdVO cdVO) {
		update("updateCd", cdVO);
	}

	public void deleteCd(CdVO cdVO) {
		delete("deleteCd", cdVO);
	}

	public List findCdListFC(String cdTpId) {
		return queryForList("findCdListFC", cdTpId);
	}

	public PageVO findCdList(CdVO cdVO) {
		return queryForPaging("findCdList", cdVO, "twenty_row", cdVO.getCurrentPage());
	}

	public List findExcelCdList(CdVO cdVO) {
		return queryForList("findCdList", cdVO);
	}

	public CdVO findCd(CdVO cdTO) {
		return (CdVO) queryForObject("findCd", cdTO);
	}

}
