#!/usr/bin/env python

import sys
import os

import pymerase
import pymerase.input.parseXMI
import pymerase.output.CreateSQL

if __name__ == "__main__":
  schema = os.path.abspath("./manyToMany.xmi")
  outputPath = os.path.abspath("./manyToMany.sql")
    
  pymerase.run(schema, pymerase.input.parseXMI, outputPath, pymerase.output.CreateSQL)

