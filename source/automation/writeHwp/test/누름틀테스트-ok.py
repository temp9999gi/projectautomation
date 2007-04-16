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

hwpApp.HAction.GetDefault("InsertFieldTemplate", hwpApp.HParameterSet.HInsertFieldTemplate.HSet);
hwpApp.HParameterSet.HInsertFieldTemplate.TemplateDirection = "필드이름TemplateDirection";
hwpApp.HParameterSet.HInsertFieldTemplate.TemplateName = "field1";
hwpApp.HAction.Execute("InsertFieldTemplate", hwpApp.HParameterSet.HInsertFieldTemplate.HSet);
#hwpApp.HAction.Run("MoveLeft");


hwpApp.PutFieldText("field1","field내용")

#PutFieldText(BSTR fieldlist, BSTR textlist)

hwpApp.HAction.GetDefault("InsertText", hwpApp.HParameterSet.HInsertText.HSet);
hwpApp.HParameterSet.HInsertText.Text = "필드2에입력";
hwpApp.HAction.Execute("InsertText", hwpApp.HParameterSet.HInsertText.HSet);
