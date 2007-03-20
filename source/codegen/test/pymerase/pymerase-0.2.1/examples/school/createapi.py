#!/usr/bin/env python

import os
import pymerase
from pymerase.util import NameMangling

if __name__ == "__main__":
  #base_dir = os.path.expanduser("~/proj/genex/mged/lib/Python/pymerase/examples/school")
  base_dir = os.getcwd()
  schema = os.path.abspath(os.path.join(base_dir, "test.zargo"))
  output = os.path.abspath(os.path.join(base_dir, "test"))

  translator = pymerase.Pymerase()
  translator.setDefaultPackage("untitled")
  mangler = NameMangling.underscore_word()
  classesInModel ={}
  translator.setNameMangler(mangler, 'CreateSQL')
  parsed_input = translator.read(schema, 'parseXMI', classesInModel)
  print classesInModel
  translator.write(parsed_input, output, 'CreateDBAPI')


