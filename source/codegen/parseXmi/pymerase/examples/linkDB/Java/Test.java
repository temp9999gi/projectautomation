/** 
 * Create a new Test
 *
 * All collections will be initialized (as empty).
 */

public Test 
{
	#writeNoArgCtor
	#writeArgCtor

	/**
	 * Getter / Setter Pairs
	 */


	/**
	 * Collection adder/removers
	 */


	/**
	 * Debugging
	 */
  /**
   * Prints a string represenation of this class to aid in debugging
   */
  public void debugPrint()
  {
  	System.out.println("class Test");
  	debugDumpAttributes();
  	System.out.println();
  }
  
  
  protected void debugDumpAttributes()
  {
  	System.out.println("	_id: " + _id);
  	System.out.println(" TestPk: " +TestPk);
  	System.out.println(" Attribute1: " +Attribute1);
  	System.out.println(" Attribute2: " +Attribute2);
  	System.out.println(" Operation1: " +Operation1);
  }

	/**
	 * Attributes
	 */ 

	/**
	 * Extra attributes to hold the primary key of the different object
	 * references.
	 */


	/**
	 * Extra Object Relational Bridge (OJB) attributes for mapping back
	 * to classses which have a 1:N relation with this specific class.
	 */


	/**
	 * Primary Key in database
	 */ 
};