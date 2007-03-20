#!/usr/bin/env python

import sys
import os

import pymerase
#import pymerase.input.parseXMI
#import pymerase.output.CreatePyTkDBWidgets

if __name__ == "__main__":
  schema = os.path.abspath("./dvd.zargo")
  outputPath = os.path.abspath("./widgets")
    
  pymerase.run(schema, 'parseXMI', outputPath, 'CreatePyTkDBWidgets')
  #pymerase.run(schema, pymerase.input.parseXMI, outputPath, pymerase.output.CreatePyTkDBWidgets)
  


