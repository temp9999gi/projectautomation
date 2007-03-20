#!/usr/bin/env python

import sys
import os

import pymerase
#import pymerase.input.parseXMI
#import pymerase.output.CreateDBAPI

if __name__ == "__main__":
  schema = os.path.abspath("./manyToMany.zargo")
  outputPath = os.path.abspath("./m2mAPI")
    
  pymerase.run(schema, 'parseXMI', outputPath, 'CreateDBAPI')
  #pymerase.run(schema, pymerase.input.parseXMI, outputPath, pymerase.output.CreateDBAPI)


