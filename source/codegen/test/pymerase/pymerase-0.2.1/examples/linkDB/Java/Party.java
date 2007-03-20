/** 
 * Create a new Party
 *
 * All collections will be initialized (as empty).
 */

public Party 
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
  	System.out.println("class Party");
  	debugDumpAttributes();
  	System.out.println();
  }
  
  
  protected void debugDumpAttributes()
  {
  	System.out.println("	_id: " + _id);
  	System.out.println(" PartyPk: " +PartyPk);
  	System.out.println(" Name: " +Name);
  	System.out.println(" Address: " +Address);
  	System.out.println(" Age: " +Age);
  	System.out.println(" Insert: " +Insert);
  	System.out.println(" Update: " +Update);
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