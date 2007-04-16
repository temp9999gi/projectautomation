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

hwpApp.HAction.GetDefault("TableCreate", hwpApp.HParameterSet.HTableCreation.HSet);
hwpApp.HParameterSet.HTableCreation.Rows = 1;
hwpApp.HParameterSet.HTableCreation.Cols = 2;
hwpApp.HParameterSet.HTableCreation.WidthType = 2;
hwpApp.HParameterSet.HTableCreation.HeightType = 1;
hwpApp.HParameterSet.HTableCreation.WidthValue = 41954;
hwpApp.HParameterSet.HTableCreation.HeightValue = 6410;
hwpApp.HParameterSet.HTableCreation.TableTemplateValue = 60592;
hwpApp.HParameterSet.HTableCreation.CreateItemArray("ColWidth", 2);

xx = hwpApp.HParameterSet.HTableCreation.ColWidth

# 아래에서 에러나더라..
hwpApp.HParameterSet.HTableCreation.ColWidth.Item(0,20695)
hwpApp.HParameterSet.HTableCreation.ColWidth.Item[1] = 20695;
hwpApp.HParameterSet.HTableCreation.CreateItemArray("RowHeight", 1);
hwpApp.HParameterSet.HTableCreation.RowHeight.Item[0] = 6128;
hwpApp.HParameterSet.HTableCreation.TableProperties.Width = 41954;

hwpApp.HAction.Execute("TableCreate", hwpApp.HParameterSet.HTableCreation.HSet);
hwpApp.HAction.Run("TableRightCellAppend");
hwpApp.HAction.Run("TableAppendRow");
hwpApp.HAction.Run("TableRightCellAppend");
hwpApp.HAction.GetDefault("InsertText", HParameterSet.HInsertText.HSet);

hwpApp.HParameterSet.HInsertText.Text = "111";

hwpApp.HAction.Execute("InsertText", HParameterSet.HInsertText.HSet);
hwpApp.HAction.Run("MoveRight");
hwpApp.HAction.GetDefault("InsertText", HParameterSet.HInsertText.HSet);
hwpApp.HParameterSet.HInsertText.Text = "222";
hwpApp.HAction.Execute("InsertText", HParameterSet.HInsertText.HSet);
hwpApp.HAction.Run("TableAppendRow");
hwpApp.HAction.Run("TableRightCellAppend");