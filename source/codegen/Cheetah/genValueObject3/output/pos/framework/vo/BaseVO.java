package org.framework.vo;

import java.io.Serializable;
import java.lang.reflect.Field;
import java.util.Arrays;

/**
 * <pre>
 *  
 * </pre>
 * 
 * @author kusung
 */
public class BaseVO implements Serializable {

	int monetaryUnit = 1;
	
	int rowCntPerPage;
	/**
	 * @return rowCntPerPage을 리턴합니다.
	 */
	public int getRowCntPerPage() {
		return rowCntPerPage;
	}
	/**
	 * @param rowCntPerPage 설정하려는 rowCntPerPage.
	 */
	public void setRowCntPerPage(int rowCntPerPage) {
		this.rowCntPerPage = rowCntPerPage;
	}	
	
	/**
	 * @return monetaryUnit을 리턴합니다.
	 */
	public int getMonetaryUnit() {
		return monetaryUnit;
	}
	/**
	 * @param monetaryUnit 설정하려는 monetaryUnit.
	 */
	public void setMonetaryUnit(int monetaryUnit) {
		this.monetaryUnit = monetaryUnit;
	}

	/**
	 * @param monetaryUnit 설정하려는 monetaryUnit.
	 */
	public void calcMoneytaryUnit(int calcUnit){
		
	}


	public String toString() {
		StringBuffer tempBuffer = new StringBuffer();
		tempBuffer.append("\n [" + this.getClass().getName() + "]");

		Field[] myFieldArray = this.getClass().getDeclaredFields();

		for (int i = 0; i < myFieldArray.length; i++) {
			try {
				Field myField = myFieldArray[i];
				myField.setAccessible(true);

				if (myField.getType().isArray()) {
					String className = myField.getType().getName();
					className = className.substring(2, className.length() - 1);

					tempBuffer.append("\n " + className + "[] ").append(myField.getName()).append(
							" = " + Arrays.asList((Object[]) myField.get(this)));
				} else if (myField.getType().isPrimitive() || (myField.getType() == String.class)) {
					String typeName = myField.getType().getName();
					typeName = ((myField.getType() == String.class) ? "String" : typeName);
					tempBuffer.append("\n " + typeName + " ").append(myField.getName()).append(" = [" + myField.get(this) + "]");
				} else if (myField.getType() == Class.class) {
					// ignore
				} else {
					String className = myField.getType().getName();
					tempBuffer.append("\n " + className + " ").append(myField.getName()).append(" = [" + myField.get(this) + "]");
				}
			} catch (Exception e) {
			}
		}

		return tempBuffer.toString();
	}
}