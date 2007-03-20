/** 
 * Create a new MyFirstAGXContent
 *
 * All collections will be initialized (as empty).
 */

public MyFirstAGXContent 
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
    System.out.println("class MyFirstAGXContent");
    debugDumpAttributes();
    System.out.println();
  }
  
  
  protected void debugDumpAttributes()
  {
    System.out.println("  _id: " + _id);
    System.out.println(" MyFirstAGXContentPk: " +MyFirstAGXContentPk);
    System.out.println(" MyTextField: " +MyTextField);
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