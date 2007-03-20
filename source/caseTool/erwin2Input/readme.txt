erwin에서 export한 것을
input시트를 만든다.

VARCHAR ==> String으로 만든다.

[TABLE_Source]
Table/View Name	Column Name	Column Datatype	Column Null Option	Column Is PK	Column Is FK	Attribute Name	EntityName
TB_BTR_DOMESTIC_PURPOSE	RQST_NO	VARCHAR(20)	NOT NULL	Yes	Yes	신청번호	방문목적

[input]
NO	ClassName	가시성	타입	속성명
1	방문목적	private	String	신청번호

