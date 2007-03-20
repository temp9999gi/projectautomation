#!/usr/bin/env python

import sys
import os

import pymerase
# NOTE: Jython can't use the python way to load modules based on their name
# NOTE: so we have to manually import the modules we're using
# NOTE: and pass them to pymerase.run
import pymerase.input.parseXMI
import pymerase.output.CreatePyTkWidgets

if __name__ == "__main__":
  schema = os.path.abspath("./school.xmi")
  outputPath = os.path.abspath("./widgets")
    
  #pymerase.run(schema, 'parseXMI', output, 'CreateDBAPI')
  pymerase.run(schema, pymerase.input.parseXMI, outputPath, pymerase.output.CreatePyTkWidgets)


