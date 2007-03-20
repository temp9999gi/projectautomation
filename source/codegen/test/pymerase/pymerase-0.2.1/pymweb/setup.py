#!/usr/bin/env python
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

from distutils.core import setup
#from distutils.core import Command


#######################################
# Install Paths

#Default (Debian) CGI installation path
CGI_PATH = '/usr/lib/cgi-bin/'

#Default (Debian) Apache WWW path
WWW_PATH = '/var/www/'

#Default (Debian) Apache Conf path
CONF_PATH = '/etc/apache/conf/'


#######################################
# Command Line Install Paths

#List of argv items to be removed after being processed
# Need to be removed before passing to setup() below
rmList = []

#Command line options available for passing non debian paths
for item in sys.argv:

  #cgi install path from commandline
  if item[:10] == '--cgiPath=' and len(item) > 10:
    CGI_PATH = item[10:]
    rmList.append(item)

  #www install path from commandline
  if item[:10] == '--wwwPath=' and len(item) > 10:
    WWW_PATH = item[10:]
    rmList.append(item)

  #conf install path from commandline
  if item[:11] == '--confPath=' and len(item) > 11:
    CONF_PATH = item[11:]
    rmList.append(item)

#Remove processed argv items
if len(rmList) > 0:
  for item in rmList:
    sys.argv.remove(item)


#######################################
# Files to be copied
CGI_SCRIPT = (CGI_PATH,
              ['cgi/pymweb.py'])

HTML_FORM = (WWW_PATH,
             ['www/pymweb.html'])

LOGO_IMG = (os.path.join(WWW_PATH, 'images'),
            ['www/images/pymerase-title.jpg'])

CONF_FILE = (CONF_PATH,
             ['conf/pymweb.conf'])

DTD_FILE = (CGI_PATH,
            ['dtd/table.dtd'])


DATA_FILES=[CGI_SCRIPT,
            HTML_FORM,
            LOGO_IMG,
            CONF_FILE,
            DTD_FILE]

print DATA_FILES



#class install_paths(Command):
#
#    # Brief (40-50 characters) description of the command
#    description = "Allows paths to be given in command line."
#
#    # List of option tuples: long name, short name (None if no short
#    # name), and help string.
#    user_options = [('cgiPath=', None,
#                     "Path to cgi-bin directory"),
#                    ('wwwPath=', None,
#                     "Path to the apache www directory"),
#                    ('confPath=', None,
#                     "Path to the apache conf directory")
#                    ]
#
#
#    def initialize_options (self):
#        self.cgiPath = None
#        self.wwwPath = None
#        self.confPath = None
#
#    # initialize_options()
#
#
#    def finalize_options (self):
#      pass
#
#    # finalize_options()
#
#
#    def run (self):
#      #print self.cgiPath
#      if self.cgiPath is not None:
#        CGI_PATH = self.cgiPath
#
#      #print self.wwwPath
#      if self.wwwPath is not None:
#        WWW_PATH = self.wwwPath
#        
#      #print self.confPath
#      if self.confPath is not None:
#        CONF_PATH = self.confPath
#
#    # run()
#
## class install_paths

setup(name="Pymweb",
      version="0.1.0",
      description="Pymweb is a web front end for running Pymerase.",
      author="Brandon King",
      author_email="kingb@caltech.edu",
      url="http://pymerase.sf.net/",
      data_files=DATA_FILES,
      #cmdclass= {'install_paths': install_paths},
      )


