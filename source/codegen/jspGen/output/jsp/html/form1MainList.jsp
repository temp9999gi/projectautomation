<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<title>민원접수관리_민원신청서 등록</title>
<meta http-equiv="Content-Type" content="text/html; charset=euc-kr">
<link href="../../common/css/main_yellow.css" rel="stylesheet" type="text/css">
<script language="javascript" src="../../script.js"></script>
</head>

<body leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">

<table width="100%" border="0" cellspacing="0" cellpadding="0">

  <!-------상단여백 H10 S --------->
  <tr>
    <td colspan="3" height="10"></td>
  </tr>
  <!-------상단여백 H10 E--------->

  <tr>

    <!-------왼쪽여백 W10 S --------->
    <td width="10">&nbsp;</td>
    <!-------왼쪽여백 W10 E --------->


    <!---------------------------------------------본문 S ----------------------------------------------------->
    <td>

      <!-----------------------------------------본문 Table S ----------------------------------------------->
      <table width="100%" border="0" cellpadding="0" cellspacing="0">

        <!-------타이틀 S --------->
        <tr>
          <td>

            <!-------타이틀 Table S --------->
            <table border="0" cellpadding="0" cellspacing="0">
              <tr>
                <td><img src="../../common/images/tit_icon.gif" width="16" height="16"></td>
                <td width="3"></td>
                <td class="title">민원접수관리</td>
                <td class="text_left">- 민원신청서 등록</td>
              </tr>
            </table>
            <!-------타이틀 Table E --------->

          </td>
        </tr>
        <!-------타이틀 E --------->



        <!-------기능메뉴 S --------->
        <tr>
          <td>

            <!-------기능메뉴 Table S --------->
            <table border="0" align="right" cellpadding="0" cellspacing="0">
              <tr> 
                <td><img src="../../common/images/menu_icon.gif" width="11" height="11"nowrap><a href="#">링크1</a></td>
                <td width="5"></td>
                <td><img src="../../common/images/menu_icon.gif" width="11" height="11" nowrap><a href="#">링크2</a></td>
            </table>
            <!-------기능메뉴 Table E --------->

          </td>
        </tr>
        <!-------기능메뉴 E --------->


        <!-------여백 H10 S --------->
        <tr>
          <td height="10"></td>
        </tr>
        <!-------여백 H10 E --------->



        <!-------상세검색 S --------->
        <tr>
          <td>

            <!-------라인 S --------->
            <table width="100%" border="0" cellpadding="0" cellspacing="0">
              <tr>
                <td height="1" class="tb_bg_bgr"></td>
              </tr>
            </table>
            <!-------라인 E --------->

            <!-------상세검색 Table S --------->
            <table width="100%" border="0" cellpadding="0" cellspacing="1" class="table_bg">
              <tr>
                <td width="18%" class="tb_tit_center"><nobr>접수기간</nobr></td>
                <td class="tb_left">

                  <!--접수기간 S-->
                  <table border="0" cellspacing="0" cellpadding="0">
                    <tr> 
                      <td><input name="textfield2" type="text" class="td_input_bg" size="15" readonly></td>
                      <td width="3"><img border="0" src="../../common/images/trans.gif" width="3" height="1"></td>
                      <td class="text_center"><a href="javascript:calendar_open('calendar.html','','toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=no,resizable=no,width=200,height=255');"><img src="../../common/images/bu_icon_carlendar.gif" width="18" height="18" border="0"></a></td>
                      <td width="25" class="text_center">~</td>
                      <td><input name="textfield3" type="text" class="td_input_bg" size="15" readonly></td>
                      <td width="3"><img border="0" src="../../common/images/trans.gif" width="3" height="1"></td>
                      <td class="text_center" ><a href="javascript:calendar_open('calendar.html','','toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=no,resizable=no,width=200,height=255');"><img src="../../common/images/bu_icon_carlendar.gif" width="18" height="18" border="0"></a></td>
                    </tr>
                  </table>
                  <!--접수기간 E-->

                </td>
                <td width="18%" class="tb_tit_center"><nobr>입력검색</nobr></td>
                <td width="19%" class="tb_left">

                  <!----입력검색 S---->
                  <table width="100%" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td>
                        <select name="select" class="text_gr">
                          <option>접수번호</option>
                          <option>************</option>
                        </select></td>
                      <td width="100%" class="tb_left"><input name="" type="text" class="td_input" style="width:100%"></td>
                    </tr>
                  </table>
                  <!----입력검색 E---->

                </td>
                <td width="70" rowspan="3" class="tb_tit_center">

                  <!----검색버튼 S----->
                  <table border="0" cellpadding="0" cellspacing="0">
                    <tr>
                      <td><img src="../../common/images/bu2_left.gif" width="8" height="20"></td>
                      <td background="../../common/images/bu2_bg.gif" class="text_left" nowrap><a href="#">검색</a></td>
                      <td><img src="../../common/images/bu2_right.gif" width="8" height="20"></td>
                    </tr>
                  </table>
                  <!----검색버튼 S----->

                </td>
              </tr>
              <tr>
                <td class="tb_tit_center"><nobr>민원구분</nobr></td>
                <td class="tb_left">

                  <input type="checkbox" name="checkbox" value="checkbox">즉결기타 
                  <input type="checkbox" name="checkbox" value="checkbox">결재증명 
                  <input type="checkbox" name="checkbox" value="checkbox">단순 
                  <input type="checkbox" name="checkbox" value="checkbox">복합 
                  <input type="checkbox" name="checkbox" value="checkbox">고충

                </td>
                <td class="tb_tit_center"><nobr>접수구분</nobr></td>
                <td class="tb_left">

                  <select name="" class="text_gr">
                    <option>창구접수</option>
                    <option>************</option>
                  </select>

                </td>
              </tr>
            </table>
            <!--------- 상세검색 Table E ---------->

            <!-------라인 S --------->
            <table width="100%" border="0" cellpadding="0" cellspacing="0">
              <tr>
                <td height="1" class="tb_bg_bgr"></td>
              </tr>
            </table>
            <!-------라인 E --------->

          </td>
        </tr>
        <!--------- 상세검색 E ---------->



        <!-------여백13 S --------->
        <tr>
          <td height="13"></td>
        </tr>
        <!-------여백13 E --------->



        <!------ 검색결과정보 S --------->
        <tr>
          <td class="text_right">2/33 (총 123건)</td>
        </tr>
        <!------ 검색결과정보 E --------->

        <!------ 리스트 S --------->
        <tr> 
          <td>

            <!------ 리스트 Table S --------->
            <table width="100%" border="0" cellpadding="0" cellspacing="0">
              <tr>
               <td width="20" class="ltb_head"><a href="#"><img src="../../common/images/icon_allcheck.gif" width="13" height="14" border="0"></a></td>
               <td class="ltb_head_left">순번</td>
               <td class="ltb_head_left">접수번호</td>
               <td class="ltb_head_left">접수일자</td>
               <td class="ltb_head_left">민원명</td>
               <td class="ltb_head_left">신청인</td>
               <td class="ltb_head_left">신청인주소</td>
              </tr>

              <!------ 샘플데이타 S --------->
              <tr OnMouseOver="this.className='list_over'"  OnMouseOut="this.className='list_out'">
                <td class="ltb_left"><input type="checkbox" name="checkbox" value="checkbox"></td>
                <td class="ltb_left">순번1</td>
                <td class="ltb_left">접수번호1</td>
                <td class="ltb_left">접수일자1</td>
                <td class="ltb_left">민원명1</td>
                <td class="ltb_left">신청인1</td>
                <td class="ltb_left">신청인주소1</td>
              </tr>
              <tr OnMouseOver="this.className='list_over'"  OnMouseOut="this.className='list_out'">
                <td class="ltb_left"><input type="checkbox" name="checkbox" value="checkbox"></td>
                <td class="ltb_left">순번2</td>
                <td class="ltb_left">접수번호1</td>
                <td class="ltb_left">접수일자1</td>
                <td class="ltb_left">민원명1</td>
                <td class="ltb_left">신청인1</td>
                <td class="ltb_left">신청인주소1</td>
              </tr>
            </table>
            <!-------- 리스트 Table E ----------->

          </td>
        </tr>
        <!------ 리스트 E --------->


        <!-------여백15 S --------->
        <tr>
          <td height="15"></td>
        </tr>
        <!-------여백15 E --------->



        <!---------- 페이지이동정보 S ---------->
        <tr>
          <td>

            <!---------- 페이지이동정보 Table S ---------->
            <table height="16" border="0" cellpadding="0" cellspacing="0" align="center">
              <tr>
                <td height="16"><a href="#"><img src="../../common/images/icon_prevend.gif" width="13" height="13" border="0"></a></td>
                <td width="3"></td>
                <td><a href="#"><img src="../../common/images/icon_prev.gif" width="13" height="13" border="0"></a></td>
                <td class="text_center" nowrap>
                  | <a href="#">1</a> | <a href="#">2</a> | <a href="#">3</a> | <a href="#">4</a> | <a href="#">5</a> 
                        | <a href="#">6</a> | <a href="#">7</a> | <a href="#">8</a> | <a href="#">9</a> | <a href="#">10</a> |
                </td>
                <td height="16"><a href="#"><img src="../../common/images/icon_next.gif" width="13" height="13" border="0"></a></td>
                <td width="3"></td>
                <td><a href="#"><img src="../../common/images/icon_nextend.gif" width="13" height="13" border="0"></a></td>
              </tr>
            </table>
            <!---------- 페이지이동정보 Table E ---------->

          </td>
        </tr>
        <!------ 페이지이동정보 E --------->

      </table>
      <!---------------------------------------------본문 Table E ------------------------------------------->	

    </td>
    <!-------------------------------------------------본문 E ------------------------------------------------>



    <!-------오른쪽여백 W10 S --------->
    <td width="10">&nbsp;</td>
    <!-------오른쪽여백 W10 E --------->
  </tr>
</table>



</body>
</html>

