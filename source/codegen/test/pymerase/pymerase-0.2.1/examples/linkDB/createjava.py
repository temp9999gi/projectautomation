# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import os

import pymerase
##import pymerase.pyMeraseMain as pymerase #import *
from pymerase.pyMeraseMain import *
import pymerase.input.parseXMI
import pymerase.output.CreateJava

if __name__ == "__main__":
  schema = os.path.abspath("./linkDB/Party.xmi")
  #schema = os.path.abspath("./linkDB/linkDB.xmi")
  outputPath = os.path.abspath("./Java")
    
  #pymerase.run(schema, pymerase.input.parseXMI, outputPath, pymerase.output.CreateJava)
  run(schema, pymerase.input.parseXMI, outputPath, pymerase.output.CreateJava)

