#!/usr/bin/env python

import sys
import os

import pymerase
import pymerase.input.parseGenexSchemaXML
import pymerase.output.CreateCppAPI

if __name__ == "__main__":
  schema = os.path.abspath("./schema")
  outputPath = os.path.abspath("./CppAPI")
    
  pymerase.run(schema, pymerase.input.parseGenexSchemaXML, outputPath, pymerase.output.CreateCppAPI)

