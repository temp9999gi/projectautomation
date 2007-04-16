VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
  Persistable = 0  'NotPersistable
  DataBindingBehavior = 0  'vbNone
  DataSourceBehavior  = 0  'vbNone
  MTSTransactionMode  = 0  'NotAnMTSObject
END
Attribute VB_Name = "DocumentObject"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = True
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = True
Option Explicit
' Declare a New word application Object
Dim wdApp As New Word.Application

' Start of the function, with the 4 parameters passed to it from the ASP file _
  It returns a string type, as we shall see
Public Function GenerateDocument(sTags, sValues, sSourcePath, sDestPath) As _
String
    
   On Error GoTo ErrHandler
   Dim arrTags() As String, arrValues() As String, iLoop As Integer
    
   ' Open the template file from the specified source path (sent from the ASP _
     file as a parameter). A reference to a new Word document, based on the _
     template is created on the server
   wdApp.Documents.Open sSourcePath
    
   ' Get all the tags as obtained from the HTML Form, into the array arrTags, _
     using the Split function. A comma has been used as the delimiter for _
     separating tag values in the ASP file
   arrTags = Split(sTags, ", ")

    
   ' Store the corresponding user input values into the array arrValues. The _
     pipe character (|) has been used as the delimiter for separating these _
     values.
   arrValues = Split(sValues, " | ")
    
   ' Loop through the tags in the array arrTags and use the find and replace _
     operation (using Visual Basic for Applications script) to find tags from _
     the tags array, in the created Word document, and replace with _
     corresponding values from the arrValues array. The long string of commas _
     that you see is the different attributes of the Find-Execute method, _
     which we have not set. We are only interested in setting the _
     MatchWholeWord, ReplaceWith, and ReplaceAll (which is represented by the _
     numeric constant 2) options.
   For iLoop = 0 To UBound(arrTags)
       wdApp.ActiveDocument.Content.Find.Execute arrTags(iLoop), , True, , _
       , , , , , arrValues(iLoop), 2
   Next iLoop
    
   ' Save the document in the specified destination path and filename
   wdApp.ActiveDocument.SaveAs sDestPath
   
   ' Close the word document object; quit and release it
   wdApp.ActiveDocument.Close
   wdApp.Quit
   Set wdApp = Nothing
    
   ' Return a Success Flag, and exit the function
   GenerateDocument = "Success"
   Exit Function
   
   ' This is the error handling routine. It simply returns the error _
     Message, if any error was encountered during the processing of the _
     above application.
ErrHandler:
    
   ' Quit and release the word document object
   wdApp.Quit
   Set wdApp = Nothing
   
   ' Build the Error Message, and pass it back
   Dim ErrMsg As String
   ErrMsg = "Error Number: " & Err.Number & "<BR><BR>"
   ErrMsg = ErrMsg & "Error Source: " & Err.Source & "<BR><BR>"
   ErrMsg = ErrMsg & "Error Description: " & Err.Description & "<BR><BR>"
   GenerateDocument = ErrMsg
   Exit Function
        
End Function

Private Sub Class_Terminate()
   ' Release the reference
   Set wdApp = Nothing
End Sub


