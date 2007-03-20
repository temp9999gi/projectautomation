#!/usr/bin/env python

import sys
import os

import pymerase
#import pymerase.input.parseXMI
#import pymerase.output.CreateSQL

if __name__ == "__main__":
  schema = os.path.abspath("./pubmed.xmi")
  outputPath = os.path.abspath("./pubmed.sql")

  pymerase.run(schema, "parseXMI", outputPath, "iPymerase")
  #pymerase.run(schema, pymerase.input.parseXMI, outputPath, pymerase.output.CreateSQL)

