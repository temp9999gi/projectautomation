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
hwpApp.HParameterSet.HFileOpenSave.FileName = "C:\\__2007\\hwp자동화_실습\\누름틀.hwp";
hwpApp.HParameterSet.HFileOpenSave.OpenReadOnly = 0;
hwpApp.HAction.Execute("FileOpen", hwpApp.HParameterSet.HFileOpenSave.HSet);


##hwpApp.HAction.GetDefault("InsertFieldTemplate", hwpApp.HParameterSet.HInsertFieldTemplate.HSet);
##hwpApp.HParameterSet.HInsertFieldTemplate.TemplateDirection = "필드이름TemplateDirection";
##hwpApp.HParameterSet.HInsertFieldTemplate.TemplateName = "field1";
##hwpApp.HAction.Execute("InsertFieldTemplate", hwpApp.HParameterSet.HInsertFieldTemplate.HSet);

#PutFieldText(BSTR fieldlist, BSTR textlist)
hwpApp.PutFieldText("field1","field내용999")

# 
hwpApp.HAction.GetDefault("FileSaveAs", hwpApp.HParameterSet.HFileOpenSave.HSet);
hwpApp.HParameterSet.HFileOpenSave.Attributes = 2048;
hwpApp.HParameterSet.HFileOpenSave.FileName = "C:\\__2007\\hwp자동화_실습\\999.hwp";
hwpApp.HParameterSet.HFileOpenSave.Format = "HWP";
hwpApp.HAction.Execute("FileSaveAs", hwpApp.HParameterSet.HFileOpenSave.HSet);




