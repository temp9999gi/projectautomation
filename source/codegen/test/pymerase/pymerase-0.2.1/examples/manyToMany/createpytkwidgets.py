#!/usr/bin/env python

import sys
import os

import pymerase
#import pymerase.input.parseXMI
#import pymerase.output.CreatePyTkWidgets

if __name__ == "__main__":
  schema = os.path.abspath("./manyToMany.zargo")
  outputPath = os.path.abspath("./widgets")
    
  pymerase.run(schema, 'parseXMI', outputPath, 'CreatePyTkWidgets')
  #pymerase.run(schema, pymerase.input.parseXMI, outputPath, pymerase.output.CreatePyTkWidgets)


