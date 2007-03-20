#!/usr/bin/env python2.2
###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) 2003 by:                                                 #
#    * California Institute of Technology                                 #
#                                                                         #
#    All Rights Reserved.                                                 #
#                                                                         #
# Permission is hereby granted, free of charge, to any person             #
# obtaining a copy of this software and associated documentation files    #
# (the "Software"), to deal in the Software without restriction,          #
# including without limitation the rights to use, copy, modify, merge,    #
# publish, distribute, sublicense, and/or sell copies of the Software,    #
# and to permit persons to whom the Software is furnished to do so,       #
# subject to the following conditions:                                    #
#                                                                         #
# The above copyright notice and this permission notice shall be          #
# included in all copies or substantial portions of the Software.         #
#                                                                         #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,         #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF      #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                   #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS     #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN      #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN       #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE        #
# SOFTWARE.                                                               #
###########################################################################
#
#       Authors: Brandon King
# Last Modified: $Date: 2006/12/18 15:54:02 $
# 

import os
import sys
import getopt
import time

from PubMedAPI import DBSession
from Bio import PubMed
from Bio import Medline

rev = "$Revision: 1.1 $"
rev = rev.replace('$Revision: ', '')
rev = rev.replace(' $', '')

VERSION = 'v0.%s' % (rev)

def printUseage():
  useage = """
  Welcome to PubMed-Test!
  
  Useage:
    pubmed-test.py -s [search]
  
    pubmed-test.py --search=[search]

  Options:
    -s, --search=[foo]         Pubmed Search you would like to try.

    -v, --version              Displays version number
    -h, --help                 Displays this help page
    
  """  
  print useage

def parseCommandLine():
  """
  Processes Command Line Arguments

  return (source, inputModule, destination, outputModule)
  """
  try:
    opts, args = getopt.getopt(sys.argv[1:], "s:hv",
                               ["search=",
                                "version",
                                "help"])
  except getopt.GetoptError:
    print "-------------------------------"
    print "- Invalid Command Line Option -"
    print "-------------------------------"
    printUseage()
    sys.exit(2)
    
  if len(sys.argv) <= 1:
    printUseage()
    sys.exit(2)

  search = None
  for arg, val in opts:
    if arg in ('-h', '--help'):
      printUseage()
      sys.exit()

    if arg in ('-v', '--version'):
      print ''
      print 'pubmed-test.py %s' % (VERSION)
      print ''
      sys.exit()

    if arg in ('-s', '--search'):
      print "SEARCH: %s" % (val)
      search = val
      return search

if __name__ == '__main__':
  search = parseCommandLine()

  print 'Searching Now... please wait. %s' % (time.ctime())
  pubmedList = PubMed.search_for(search)
  print 'Search Complete! %s' % (time.ctime())
  print pubmedList
  print ''
  print 'Preparing Local Database %s' % (time.ctime())
  dbs = DBSession(dsn='localhost', database='pubmed', user='king')
  print 'Local Database Connection Complete %s' % (time.ctime())
  print ''
  print 'Creating GroupLabel(%s) %s' % (search, time.ctime())
  grpList = dbs.GroupList()
  grpList.setName(search)                            
  print 'Created GroupLabel(%s) %s' % (search, time.ctime())
  print ''
  print 'Retrieving Records %s' % (time.ctime())
  rec_parser = Medline.RecordParser()
  medline_dict = PubMed.Dictionary(parser=rec_parser)

  counter = 0
  for rec in pubmedList:
    myRec = dbs.PubMedRecord()
    pmRec = medline_dict[rec]
    print pmRec.title
    myRec.setTitle(pmRec.title)
    myRec.setAbstract(pmRec.abstract)
    myRec.setPubmedAccess(pmRec.pubmed_id)
    myRec.commit()
    grpList.appendPubMedRec(myRec)
    counter += 1

  print 'Retrieved %s Records. %s' % (counter, time.ctime())
  print 'Saving Search to Local Database. %s' % (time.ctime())
  grpList.commit()
  print 'Records saved to Local Database. %s' % (time.ctime())

  print 'DONE'
