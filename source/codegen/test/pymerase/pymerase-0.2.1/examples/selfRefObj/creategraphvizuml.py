#!/usr/bin/env python

import sys
import os

import pymerase
import pymerase.input.parseXMI
import pymerase.output.CreateGraphvizUML

if __name__ == "__main__":
  schema = os.path.abspath("./selfRefObj.xmi")
  outputPath = os.path.abspath("./selfRefObj.dot")
    
  pymerase.run(schema, pymerase.input.parseXMI, outputPath, pymerase.output.CreateGraphvizUML)

