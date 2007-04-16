 <%
    Dim sTags, sValues, sDestPath, sSourcePath, resValue 
 
    ' Get all the User Input values from the Form
    sName = Request("Name")
    sAddress = Request("Address")
    sCity = Request("City")
    sState = Request("State")
    sZip = Request("Zip")
    sCountry = Request("Country")
    sEmail = Request("Email")
    sDate = Now()
 
    ' Create a list of all the tags as defined in the Word Template by You
    sTags = "<Name>, <Address>, <City>, <State>, <Zip>, <Country>, " & _
       "<Email>, <Date>"
 
    ' Gather up all the User Input values into one delimited string
    sValues = sName & " | " & sAddress & " | " & sCity & " | " & sState & _
       " | " & sZip & " | " & sCountry & " | " & sEmail & " | " & sDate
 
    ' Identify the location of the Source (Template) and Destination
    ' (Document) files. APPL_PHYSICAL_PATH returns the directory
    ' where the CustomDoc.asp file is located. To it, we append the Documents 
    ' folder and the filename, which is the name of the User minus spaces
    sSourcePath = Request.ServerVariables("APPL_PHYSICAL_PATH") & _ 
       "Templates\" & "EmployeeTemplate.dot"
    sDestPath = Request.ServerVariables("APPL_PHYSICAL_PATH") & _ 
       "Documents\" & Replace(sName, " ","") & ".doc"  
 
    ' Create an Instance of the object MyDocument Object
    Set myDocObj = Server.CreateObject("MyDocument.DocumentObject")
 
    ' Call the GenerateDocument function while passing the required
    ' Parameters 
    retValue = myDocObj.GenerateDocument(sTags, sValues, sSourcePath, _
       sDestPath)
 
    ' Take appropriate action based on the returned value
    If retValue = "Success" Then
       Msg = "Successfully generated your Document : " & Replace(sName, _
          " ", "") & ".doc"
       Response.Write("<font face=arial size=-1 color=Green><br>" & Msg)
       Response.Write("<br><br><a href=Documents/" & _
          Replace(sName, " ","") & ".doc" & ">Here it is!</a>")
    Else
       Response.Write("<font face=arial size=-1 color=Red><br>" & retValue)
    End If
 %>
