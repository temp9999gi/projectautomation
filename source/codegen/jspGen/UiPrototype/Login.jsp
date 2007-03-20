<%@ page language="java" contentType="text/html;charset=EUC-KR" %>

<HTML>
<HEAD>
<TITLE>로그인</TITLE>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=EUC-KR">
<SCRIPT LANGUAGE="javascript">
<!--
function validate() {

	// 입력된 아이디와 암호의 유효성을 판단한다.
	// 원래는 아이디가 4 문자이고 암호는 7자리 이하의 영문자 또는 숫자 인지를 확인하여야 하지만,
	// 설명을 간단히 하기 위하여 아이디와 암호의 입력 여부만을 조사하고 있다.
	
	if (document.frmLogin.txtId.value.length == 0) {
		alert("아이디를 입력해주세요.");
		document.frmLogin.txtId.focus();
		return false;
	}
	if (document.frmLogin.txtPassword.value.length == 0) {
		alert("패스워드를 입력해주세요.");
		document.frmLogin.txtPassword.focus();
		return false;
	}    
	return true;
}
//-->
</SCRIPT>
</HEAD>
<BODY TOPMARGIN="50">
<FORM NAME="frmLogin" METHOD="post" ACTION="LoginProc.jsp" ONSUBMIT='return validate()'>
<TABLE BORDER="1" ALIGN="center">
<TR>
	<TD ALIGN="center" COLSPAN="2">로그인</TD>
</TR>   
<TR>
	<TD ALIGN="center">아이디</td>
	<TD><INPUT TYPE="text" NAME="txtId"></TD>
</TR>
<TR> 
	<TD ALIGN="center">패스워드</TD>
	<TD><INPUT TYPE="password" NAME="txtPassword"></TD>
</TR>
<TR>    
	<TD ALIGN="center" COLSPAN="2">
	<INPUT TYPE="submit" VALUE="로그인">
	<INPUT TYPE="reset" VALUE="원래대로">
	</TD>
</TR>
</TABLE>
</FORM>
</BODY>
</HTML>
