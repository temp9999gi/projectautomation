#!/usr/bin/env python

import sys
import os

import pymerase

if __name__ == "__main__":
  schema = os.path.abspath("./school.xmi")
  output = os.path.abspath("./school")
    
  pymerase.run(schema, 'parseXMI', output, 'iPymerase')

