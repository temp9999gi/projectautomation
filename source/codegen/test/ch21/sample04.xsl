<?xml version="1.0"?> 
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"> 
  <xsl:output method='html' indent='yes'/> 
 
  <xsl:template match="/"> 
    <HTML><HEAD><TITLE>USER LIST</TITLE></HEAD> 
    <BODY> 
    <H1>User List</H1> 
    <TABLE border="1"> 
    <TR><TH>Sex</TH><TH>Name</TH><TH>Email</TH></TR> 
    <xsl:apply-templates/> 
    </TABLE> 
    </BODY> 
    </HTML> 
  </xsl:template> 
 
  <xsl:template match="user"> 
    <TR> 
    <TD><xsl:value-of select='@sex'/></TD> 
    <xsl:apply-templates select='name|email'/> 
    </TR> 
  </xsl:template> 
 
  <xsl:template match="name"> 
    <TD><xsl:apply-templates/></TD> 
  </xsl:template> 
 
  <xsl:template match="email"> 
    <TD><xsl:apply-templates/></TD> 
  </xsl:template> 
 
</xsl:stylesheet> 
