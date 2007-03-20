# Placeholder for a transaction manager singleton
theTM=None

relaxedMode=0
strictMode=1

class TransactionManager:

    """
    A transaction groups a sequence of modifications to a model
    that can be undone and redone again. Transactions are the basis
    for using the toolkit in an interactive way. Transactions support
    command history with undo/redo and updating presentations
    selectively.  Using a transaction manager is completely
    transparent for the programmer. Instances of MMAtom report changes
    in a model as soon as a transaction manager is created. A
    transaction starts with a call to the beginModifyCmd method of the
    transaction manager and ends with a call to the endModifyCmd
    method. The model can be modified in between these calls as
    usual. After the transaction is finished, the transaction manager
    should update the presentations associated with the modified
    elements and creates a modification command in the command
    history.

    Transaction Manager Example
      from smw import Project
      from smw.metamodel import UML14
      prj=Project.Project()        # Create a project
      c=UML14.Class()              # It is possible to create objects
      c.name="Customer"            # and modify them out of a transaction
      prj.history.beginTransaction() # Begin a transaction
      c.name="Employee"            # Modify the model
      prj.history.endTransaction()   # Finish the transaction
      assert(c.name=="Employee")   # The changes are there
      prj.history.undo()           # Undo the last transaction
      assert(c.name=="Customer")   # We get the previous name
      prj.history.redo()           # Redo the last transaction
      assert(c.name=="Employee")   # Voila!     
    """   

    relaxedMode=0
    strictMode=1
    def canUndo(self):
        """returns true if it is possible to undo a modification"""
        raise "Not implemented!"
        
    def undo(self):
        """Undo last modification"""
        raise "Not implemented!"

    def canRedo(self):
        """returns true if it is possible to redo a modification"""
        raise "Not implemented!"
    
    def redo(self):
        """Redo previous undone modification"""
        
        raise "Not implemented!"

    
    def beginModifyCmd(self,mode=relaxedMode):
        """
        Use this method to start a modification of the model.

        If our application needs to check the consistency of the
        model after each change, we can use the transaction manager in
        strictMode.

        In this mode, the transaction manager checks if the updated
        elements are well-formed before committing the changes. If
        not, it undoes all the changes and raises an exception.

        A transaction manager should not enforce the well-formed rules
        by default (default mode=relaxedMode).This is done this way
        because it is quite possible and normal to violate the
        well-formed rules while manipulating a model.
        """
        
        raise "Not implemented!"

    def endModifyCmd(self):
       """Use this method to mark the end of a modification"""

       raise "Not implemented!"

    def lastTransaction(self):
       raise "Not implemented!"
   
    def beginTransaction(self):
       return self.beginModifyCmd()

    def beginStrictTransaction(self):
       return self.beginModifyCmd(mode=self.strictMode)
   
    def endTransaction(self):
       return self.endModifyCmd()

   
    def partialModifyCmd(self,obj,name,previous):
        """This method is used MMAtom to report that a model element
        has been modified during a transaction"""

        raise "Not implemented!"

    def newObjectModifyCmd(self,obj):
        """This method is used MMAtom to report that a model element
        has been created during a transaction"""

        raise "Not implemented!"
    
