#!/usr/bin/env python

import sys
import os

import pymerase
#import pymerase.input.parseXMI
#import pymerase.output.CreateReport

if __name__ == "__main__":
  schema = os.path.abspath("./dvd.zargo")
  outputPath = os.path.abspath("./report.txt")

  pymerase.run(schema, "parseXMI", outputPath, "CreateReport")
  #pymerase.run(schema, pymerase.input.parseXMI, outputPath, pymerase.output.CreateReport)

