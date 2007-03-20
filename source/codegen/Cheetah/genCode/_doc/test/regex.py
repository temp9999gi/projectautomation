import re
import string

reg1 = re.compile('WHERE.*')

inSqlText = """
    FROM ACCOUNT, PROFILE, SIGNON, BANNERDATA
    WHERE ACCOUNT.USERID = #username#
      AND SIGNON.PASSWORD = #password#
      AND SIGNON.USERNAME = ACCOUNT.USERID
      AND PROFILE.USERID = ACCOUNT.USERID
      AND PROFILE.FAVCATEGORY = BANNERDATA.FAVCATEGORY
"""

sqlText = string.replace(inSqlText,'\n',' ')

whereStr = reg1.findall(sqlText, re.I | re.M)



reg2 = re.compile('#(\w+)#')

inArg = reg2.findall(str(whereStr), re.I | re.M)

print inArg