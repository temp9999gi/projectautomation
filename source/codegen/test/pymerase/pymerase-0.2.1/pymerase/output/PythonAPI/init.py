"""Class factory for packages created by pymerase.
"""

import os
import sys
import types

import pgdb as db_api

%%IMPORT_MODULES%%

class Functor:
  def __init__(self, function, *args, **kargs):
    assert callable(function), "function should be a callable obj"
    self._function = function
    self._args = args
    self._kargs = kargs
    
  def __call__(self, *args, **kargs):
    """call function"""
    _args = list(self._args)
    _args.extend(args)
    _kargs = self._kargs.copy()
    _kargs.update(kargs)
    return apply(self._function,_args,_kargs)      

class Session:
  """Provides object factory and a place for the serialization mixins.
  """
  def __init__(self):
    # class references is used to lookup the table class variable information
    # in get_objects and get_all_objects
    self.class_references = {}
    
    modules_to_load = %%MODULES%%
    
    self.__load_classes(modules_to_load)

  #############################
  # Database session management
  def connect(self):
    if self.db is None:
      self.db = db_api.connect(dsn=self.dsn,
                               user=self.user,
                               database=self.database,
                               password=self.password)
      
  def cursor(self):
    #if self.db is None:
    #  self.connect()
    return self.db.cursor()

  def rollback(self):
    if self.db is not None:
      self.db.rollback()

  def commit(self):
    if self.db is not None:
      self.db.commit()

  ############################
  # attribute access
  def __load_classes(self, module_list):
    for className, classRef in module_list:
      # construct arguments for functor
      _args = [classRef]
      kargs = {'db_session': self}

      # create class factory application function
      functor = apply(Functor, _args, kargs)

      # store reference to class reference, so we can
      # get access to the class variables when doing
      # certain types of lookups. (Yes this seems icky)
      self.class_references[functor] = classRef
      
      # add constructor to our class object
      setattr(self, className, functor)

    return
    for m in module_list:
      self.__load_class(m)
      

  def __getClassRef(self, class_functor):
    """Given a class or class factory reference return a class reference
    """
    
    if type(class_functor) == types.ClassType:
      class_ref = class_functor
    elif isinstance(class_functor, Functor):
      class_ref = self.class_references[class_functor]
    else:
      raise ValueError("unrecognized class type")

    return class_ref
  
  def get_objects(self, class_functor, keys):
    """Returns a list of objects from a list of primary keys.
    """
    if keys is None or len(keys) == 0:
      # FIXME: Should this raise an error instead?
      return None
    
    class_ref = self.__getClassRef(class_functor)
    
    sql = "select * from %s where %s in (" % (
      self.table_name,
      self.getPrimaryKeyName())
    sql += keys[0]
    for k in keys[1:]:
      sql += ", %s" % (k)
    sql += ")"
  
    return self.load_records(class_ref, sql)
  
  def get_all_objects(self, class_functor):
    """Return all records of type class_ref as a list.
    """
    class_ref = self.__getClassRef(class_functor)
    
    sql = "select * from %s" % (class_ref.table_name)
    return self.load_records(class_ref, sql)

  def get_objects_where(self, class_functor, where_clause):
    """Returns all records of type class ref that matches the sql where expr.
    """
    class_ref = self.__getClassRef(class_functor)
    
    sql = "select * from %s where %s" % (class_ref.table_name, where_clause)
    return self.load_records(class_ref, sql)
    
  def load_records(self, class_ref, sql):
    """Returns a list of objects selected by an sql statement.
    
    Given a class_reference and an sql statement for each record returned
    bind the values to an object instantiated from the class_ref.
    """
    objects = []
    try:
      cursor = self.db.cursor()
      try:
        cursor.execute(sql)
        
        record = cursor.fetchone()
        while record is not None:
          o = class_ref(db_session=self)
          # tag this object as having been loaded from the database
          o.loaded = 1
          o.bind_fields(cursor.description, record)
          objects.append(o)
          record = cursor.fetchone()
      finally:
        cursor.close()
    except Exception, e:
      # pgdb isn't too informative about exception
      sys.stderr.write(str(e))
      sys.stderr.write(os.linesep)
      self.rollback()
    else:
      self.commit()
      
    return objects
