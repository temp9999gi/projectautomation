#!/usr/bin/env python

import pymerase
from pymerase.util import NameMangling


import os

if __name__ == "__main__":
  base_path = os.getcwd()
  schema = base_path + "/schema"
  sql_output = base_path + "/school.sql"

  translator = pymerase.Pymerase()
  translator.setDefaultPackage("school")
  mangler = NameMangling.underscore_word()

  translator.setNameMangler(mangler, 'CreateSQL')
  parsed_input = translator.read(schema, 'parseGenexSchemaXML', {})
  translator.write(parsed_input, sql_output, 'CreateSQL')


