#!/usr/bin/env python

import sys
import os

import pymerase

if __name__ == "__main__":
  schema = os.path.abspath("./house.xmi")
  outputPath = os.path.abspath("./house.sql")

  pymerase.run(schema, "parseXMI", outputPath, "CreateSQL")

