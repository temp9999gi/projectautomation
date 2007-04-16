# Integrating Python and MS Excel
#
# Basic example

# this example starts Excel, creates a new workbook,
# puts some text in the first and second cell
# closes the workbook without saving the changes
# and closes Excel.  This happens really fast, so
# you may want to comment out some lines and add them
# back in one at a time ... or do the commands interactively


from win32com.client import Dispatch

hwpApp = Dispatch("HWPFrame.HwpObject.1")
hwpDocs = hwpApp.XHwpDocuments

#Open(BSTR path, BSTR format, BSTR arg)
#hwpApp.Open("C:\__2007\hwp자동화_실습","","누름틀.hwp")

hwpApp.HAction.GetDefault("FileOpen", hwpApp.HParameterSet.HFileOpenSave.HSet);
hwpApp.HParameterSet.HFileOpenSave.OpenFlag = 0;
hwpApp.HParameterSet.HFileOpenSave.FileName = "C:\\__2007\\hwp자동화_실습\\writeHwp\테이블정의서.hwp";
hwpApp.HParameterSet.HFileOpenSave.OpenReadOnly = 0;
hwpApp.HAction.Execute("FileOpen", hwpApp.HParameterSet.HFileOpenSave.HSet);


#번호컬럼ID컬럼명타입길이NULL비고no columnId cn1 type colLengh nullYn pk
#PutFieldText(BSTR fieldlist, BSTR textlist)

hwpApp.PutFieldText("tableId","tableId_val")
hwpApp.PutFieldText("tableName","tableName_val")
hwpApp.PutFieldText("tableDescription","tableDescription_val")

hwpApp.PutFieldText("no1","no1_val")
hwpApp.PutFieldText("columnId1","ci1_val")
hwpApp.PutFieldText("columnName1","cn1_val")
hwpApp.PutFieldText("type1","type1_val")
hwpApp.PutFieldText("colLengh1","colLengh1_val")
hwpApp.PutFieldText("nullYn1","nullYn1_val")
hwpApp.PutFieldText("pk1","pk1_val")

