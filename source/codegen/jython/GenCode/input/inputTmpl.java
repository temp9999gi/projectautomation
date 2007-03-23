package lfis.sample.cd.vo;

import lfis.framework.vo.BaseVO;

public class ${aTable.tableEng} extends BaseVO {

    public ${aTable.tableEng}() {
    }
	#foreach ($t in $aTable.columnList)
    private ${t.propertyType} ${t.columnEng};
    public ${t.propertyType} get${t.upperNameIndex0}() {
        return ${t.columnEng};
    }
    public void set${t.upperNameIndex0}(String ${t.columnEng}) {
        this.${t.columnEng} = ${t.columnEng};
    }
#end
}