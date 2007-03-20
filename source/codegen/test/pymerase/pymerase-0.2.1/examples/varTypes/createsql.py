#!/usr/bin/env python

import sys
import os

import pymerase
import pymerase.input.parseXMI
import pymerase.output.CreateDBAPI

if __name__ == "__main__":
  schema = os.path.abspath("./varTypes.xmi")
  outputPath = os.path.abspath("./varTypes.sql")
    
  pymerase.run(schema, pymerase.input.parseXMI, outputPath, pymerase.output.CreateSQL)

