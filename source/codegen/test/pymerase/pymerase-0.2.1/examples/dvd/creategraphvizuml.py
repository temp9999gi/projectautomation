#!/usr/bin/env python

import sys
import os

import pymerase
#import pymerase.input.parseXMI
#import pymerase.output.CreateGraphvizUML

if __name__ == "__main__":
  schema = os.path.abspath("./dvd.zargo")
  outputPath = os.path.abspath("./dvd.dot")
    
  pymerase.run(schema, "parseXMI", outputPath, "CreateGraphvizUML")

