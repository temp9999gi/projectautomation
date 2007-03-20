#!/usr/bin/env python

import sys
import os

import pymerase
# NOTE: Jython can't use the python way to load modules based on their name
# NOTE: so we have to manually import the modules we're using
# NOTE: and pass them to pymerase.run
import pymerase.input.parseXMI
import pymerase.output.CreateDBAPI

if __name__ == "__main__":
  schema = os.path.abspath("./inheritance.xmi")
  outputPath = os.path.abspath("./InheritAPI")
    
  #pymerase.run(schema, 'parseXMI', output, 'CreateDBAPI')
  pymerase.run(schema, pymerase.input.parseXMI, outputPath, pymerase.output.CreateDBAPI)


