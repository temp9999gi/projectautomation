# Integrating Python and MS Excel
#
# Basic example

# this example starts Excel, creates a new workbook,
# puts some text in the first and second cell
# closes the workbook without saving the changes
# and closes Excel.  This happens really fast, so
# you may want to comment out some lines and add them
# back in one at a time ... or do the commands interactively


def array2comma(aTable):
	s = ''
	for c in aTable.fieldList:
		s = s + c.columnEng +'\n, '

	out = s[0:len(s)-2]
	# print 'array2comma', out
	return out



from win32com.client import Dispatch

hwpApp = Dispatch("HWPFrame.HwpObject.1")
hwpDocs = hwpApp.XHwpDocuments

hwpApp.HAction.GetDefault("InsertText", hwpApp.HParameterSet.HInsertText.HSet);
hwpApp.HParameterSet.HInsertText.Text = "글자입력";
hwpApp.HAction.Execute("InsertText", hwpApp.HParameterSet.HInsertText.HSet);
hwpApp.HAction.Run("MoveSelLineBegin");
hwpApp.HAction.GetDefault("CharShape", hwpApp.HParameterSet.HCharShape.HSet);
hwpApp.HParameterSet.HCharShape.TextColor = 16750848;
hwpApp.HAction.Execute("CharShape", hwpApp.HParameterSet.HCharShape.HSet);
hwpApp.HAction.Run("Cancel");


