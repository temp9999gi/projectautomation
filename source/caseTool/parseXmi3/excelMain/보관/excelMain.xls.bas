Private Sub cmdDo_Click()
               '12345678901234567890123456789012345678901234567890
    'appPath = "C:\_kldp\codegen\excel\writeXmlFromExcel\excelMain"
    appPath = ActiveWorkbook.Path
    
    '�ٸ� ���ڿ� ������ �� ���ڿ��� �����ϴ� ��ġ�� ���ڿ� ���������� ����Ͽ� ��ȯ�մϴ�.
    wonLastPosition = InStrRev(appPath, "\")
    
    parentPath = Mid(appPath, 1, wonLastPosition)
    
    inputFile = ThisWorkbook.Sheets("Main").Cells(3, 3).Value
        
    'Call createFile(parentPath)
    
    
    Set WshShell = CreateObject("WScript.Shell")
    Dim str
    
    EXE_FILE_PATH = ThisWorkbook.Sheets("Main").Cells(4, 3).Value
    
    'FILE_EXE_PATH = parentPath & "\writeJava\WriteJavaFromExcel.py"
    
    str = "C:\_tools\Python24\python.exe " & FILE_EXE_PATH & " " & inputFile
    WshShell.Run str
    Set WshShell = Nothing
    
    Msg = "������"
    Response = MsgBox(Msg, vbYes)
    
End Sub

Sub createFile(parentPath)
    Set fs = CreateObject("Scripting.FileSystemObject")
    Set aFile = fs.CreateTextFile(parentPath + "input\etc\appEnv.xml", True)
    
    writer = ThisWorkbook.Sheets("Main").Cells(3, 3).Value
    writeDate = ThisWorkbook.Sheets("Main").Cells(4, 3).Value
    subSystemName = ThisWorkbook.Sheets("Main").Cells(5, 3).Value
    
    aFile.WriteLine ("<appEnv writer = '" + writer + "' writeDate = '" + writeDate + "' subSystemName = '" + subSystemName + "'>")
    aFile.WriteLine ("</appEnv>")
    aFile.Close
    
End Sub

Private Sub cmdInputFile_Click()
  inputFile = Application.GetOpenFilename("��������(*.xls), *.xls")
  ThisWorkbook.Sheets("Main").Cells(3, 3).Value = inputFile
End Sub

Private Sub cmdPgmPath_Click()
  inputFile = Application.GetOpenFilename("py����(*.py), *.py")
  ThisWorkbook.Sheets("Main").Cells(4, 3).Value = inputFile
End Sub

