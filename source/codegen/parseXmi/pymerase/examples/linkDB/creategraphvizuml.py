#!/usr/bin/env python

import sys
import os

import pymerase
import pymerase.input.parseXMI
import pymerase.output.CreateGraphvizUML

if __name__ == "__main__":
  schema = os.path.abspath("./linkDB.xmi")
  outputPath = os.path.abspath("./linkDB.dot")
    
  pymerase.run(schema, pymerase.input.parseXMI, outputPath, pymerase.output.CreateGraphvizUML)

