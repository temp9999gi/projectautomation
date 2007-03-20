#!/usr/bin/env python

import sys
import os

import pymerase

if __name__ == "__main__":
  schema = os.path.abspath("./school.zargo")
  outputPath = os.path.abspath("./school.dot")
    
  pymerase.run(schema, 'parseXMI', outputPath, 'CreateDBAPI')



