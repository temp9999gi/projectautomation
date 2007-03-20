import os
import sys
import types
import psycopg as db_api
from dbAPI import Functor
from dbAPI import reloadModuleList
from dbAPI import DBSessionImpl
from dbAPI import TransactionManager

import NameLinkPair
import Group

moduleReload = Functor(reloadModuleList, (NameLinkPair, Group))

class DBSession(DBSessionImpl):
  def __init__(self, dsn=None, database=None, user=None, password=None):
    classes_to_load = [('NameLinkPair', NameLinkPair.NameLinkPair), ('Group', Group.Group), ]

    DBSessionImpl.__init__(self, dsn, database, user, password)
    self.loadClasses(classes_to_load)
    self.connect()