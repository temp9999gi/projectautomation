package lfis.fe.commcd.prc;

import java.util.List;

import lfis.fe.commcd.mgr.ICommCdMgr;
import lfis.fe.commcd.vo.CommCdVO;
import lfis.fe.commcd.vo.CommDetlCdVO;
import lfis.framework.exception.BizException;
import lfis.framework.vo.PageVO;

public class ${klassName}App implements I${klassName}App 
{
   
	private ICommCdMgr commCdMgr;
	
	/**
	 * @param commCdMgr 설정하려는 commCdMgr.
	 */
	public void setCommCdMgr(ICommCdMgr commCdMgr) {
		this.commCdMgr = commCdMgr;
	}
	
	/**
	*/
	public ${klassName}App() 
	{
	
	}
	
	/**
	@param commCdVO
	*/
	public void createCommCd(CommCdVO commCdVO) throws BizException
	{
		commCdMgr.createCommCd(commCdVO);
	}
	
	/**
	@param commCdList
	*/
	public void deleteCommCdList(List commCdList) throws BizException
	{
		commCdMgr.deleteCommCdList(commCdList);
	}
	
	/**
	@param commCdVO
	@return lfis.framework.vo.PageVO
	*/
	public PageVO findCommCdList(CommCdVO commCdVO) 
	{
		return commCdMgr.findCommCdList(commCdVO);
	}
	
	/**
	@param commCdVO
	*/
	public void updateCommCd(CommCdVO commCdVO) throws BizException
	{
		commCdMgr.updateCommCd(commCdVO);
	}
	
	/**
	@param commCdVO
	*/
	public CommCdVO findCommCd(CommCdVO commCdVO) 
	{
		return commCdMgr.findCommCd(commCdVO);
	}
	
	/**
	@param commDetlCdVOList
	*/
	public void saveCommDetlCdList(List commDetlCdVOList) throws BizException
	{
		commCdMgr.saveCommDetlCdList(commDetlCdVOList);
	}
	
	/**
	@param commDetlCdVO
	@return java.util.List
	*/
	public List findCommDetlCdList(CommDetlCdVO commDetlCdVO) 
	{
		return commCdMgr.findCommDetlCdList(commDetlCdVO);
	}
	
}
