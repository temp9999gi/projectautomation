<%@ page language="java" contentType="text/html;charset=EUC-KR" %>

<HTML>
<HEAD>
<TITLE>�α���</TITLE>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=EUC-KR">
<SCRIPT LANGUAGE="javascript">
<!--
function validate() {

	// �Էµ� ���̵�� ��ȣ�� ��ȿ���� �Ǵ��Ѵ�.
	// ������ ���̵� 4 �����̰� ��ȣ�� 7�ڸ� ������ ������ �Ǵ� ���� ������ Ȯ���Ͽ��� ������,
	// ������ ������ �ϱ� ���Ͽ� ���̵�� ��ȣ�� �Է� ���θ��� �����ϰ� �ִ�.
	
	if (document.frmLogin.txtId.value.length == 0) {
		alert("���̵� �Է����ּ���.");
		document.frmLogin.txtId.focus();
		return false;
	}
	if (document.frmLogin.txtPassword.value.length == 0) {
		alert("�н����带 �Է����ּ���.");
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
	<TD ALIGN="center" COLSPAN="2">�α���</TD>
</TR>   
<TR>
	<TD ALIGN="center">���̵�</td>
	<TD><INPUT TYPE="text" NAME="txtId"></TD>
</TR>
<TR> 
	<TD ALIGN="center">�н�����</TD>
	<TD><INPUT TYPE="password" NAME="txtPassword"></TD>
</TR>
<TR>    
	<TD ALIGN="center" COLSPAN="2">
	<INPUT TYPE="submit" VALUE="�α���">
	<INPUT TYPE="reset" VALUE="�������">
	</TD>
</TR>
</TABLE>
</FORM>
</BODY>
</HTML>
