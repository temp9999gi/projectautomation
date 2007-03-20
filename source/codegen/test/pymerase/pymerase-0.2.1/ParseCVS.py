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
import string

class CvsTreeUtil:

  def __init__(self):
    pass

  def getSetupDataFiles(self, basePath, dataFilesPath):
    """
    getSetupDataFilesTupleList(tree) --> list of tuples to pass
    to the setup.py dataFiles variable
    """
    parser = ParseCVS()

    treeRoot = parser.parseTree(dataFilesPath)
    
    allNodes = treeRoot.getAllNodes()
    
    list = []
    for node in allNodes:
      list.append((os.path.join(basePath, node.getRelPath()),
                   node.getRelFilePaths()))

    return list

class CvsTreeNode:

  def __init__(self):
    self.__abspath = None
    self.__relpath = None
    self.__dirName = None
    self.__fileNames = []
    self.__filePaths = []
    self.__relFilePaths = []
    self.__parentNode = None
    self.__childrenNodes = []

  def getAbsPath(self):
    return self.__abspath

  def setAbsPath(self, path):
    self.__abspath = path

  def getFilePaths(self):
    return self.__filePaths

  def setFilePaths(self, pathList):
    self.__filePaths = pathList

  def appendFilePath(self, path):
    self.__filePaths.append(path)

  def getRelPath(self):
    return self.__relpath

  def getRelFilePaths(self):
    return self.__relFilePaths

  def updateRelPaths(self):
    node = self

    list = []
    while node.getParentNode() is not None:
      dirName = node.getDirName()
      if dirName is not None:
        list.append(dirName)
      node = node.getParentNode()

    dirName = node.getDirName()
    if dirName is not None:
      list.append(dirName)
      
    list.reverse()
    self.__relpath = string.join(list, os.sep)

    relFilePathList = []
    for fileName in self.__fileNames:
      relFilePathList.append(os.path.join(self.__relpath, fileName))
    self.__relFilePaths = relFilePathList

  def updateAllRelPaths(self):
    node = self.getRootNode()

    nodeList = node.getAllNodes()

    for nd in nodeList:
      nd.updateRelPaths()

      
  def getAllChildrenNodes(self, node):
    nodeList = []
    tmpList = node.getChildrenNodes()

    if len(tmpList) >= 1:
      nodeList.extend(tmpList)

    if len(tmpList) >= 1:
      for nd in tmpList:
        cNodes = self.getAllChildrenNodes(nd)
        if len(cNodes) >= 1:
          nodeList.extend(cNodes)
        return nodeList
    else:
      return nodeList

  def getAllNodes(self):
    node = self.getRootNode()
    nodeList = [node]
    nodeList.extend(self.getAllChildrenNodes(node))
    return nodeList
    

  def getDirName(self):
    return self.__dirName

  def setDirName(self, name):
    self.__dirName = name

  def getFileNames(self):
    return self.__fileNames

  def setFileNames(self, fileNameList):
    self.__fileNames = fileNameList

  def appendFileName(self, fileName):
    self.__fileNames.append(fileName)

  def getParentNode(self):
    return self.__parentNode

  def setParentNode(self, node):
    self.__parentNode = node

  def getChildrenNodes(self):
    return self.__childrenNodes

  def setChildrenNodes(self, nodeList):
    self.__childrenNodes = nodeList

  def appendChildNode(self, node):
    self.__childrenNodes.append(node)

  def getRootNode(self):
    node = self
    while node.getParentNode() is not None:
      node = node.getParentNode()
    return node


class ParseCVS:

  def __init__(self):
    pass

  def parseEntries(self, entriesPath):
    """
    Parses Cvs Entries File
    
    return (cvsDirs, cvsFiles)
    """
    if os.path.exists(entriesPath) and os.path.isfile(entriesPath):
      file = open(entriesPath)
      entries = file.read()
      file.close()
      
      entries = string.split(entries, '\n')

      cvsFiles = []
      cvsDirs = []
      
      for entry in entries:
        entryList = string.split(entry, '/')
        if len(entryList) >= 2:
          if entryList[0] == 'D':
            cvsDirs.append(entryList[1])
          elif entryList[0] == '':
            # skip cvs meta files
            if entryList[1] != '.cvsignore':
              cvsFiles.append(entryList[1])
          else:
            print "WARNING: entry[0]=%s, entry[1]=%s" % \
                (entryList[0], entryList[1])
        else:
          pass

      return (cvsDirs, cvsFiles)
    else:
      print "EntriesPath(%s) Invalid... Ignoring." % (entriesPath)
      return ([],[])


  def __parseTree(self, treePath):
    """
    Parses a cvs tree
    """
    treeNode = CvsTreeNode()
    
    if os.path.exists(treePath) and os.path.isdir(treePath):
      treeNode.setAbsPath(treePath)

      tmp, dirName = os.path.split(treePath)
      treeNode.setDirName(dirName)
      
      cvsEntriesPath = os.path.join(treePath, 'CVS', 'Entries')
      cvsDirs, cvsFiles = self.parseEntries(cvsEntriesPath)

      if len(cvsFiles) >= 1:
        treeNode.setFileNames(cvsFiles)

        filePathList = []
        for fileName in cvsFiles:
          filePathList.append(os.path.join(treePath, fileName))
        treeNode.setFilePaths(filePathList)

      if len(cvsDirs) >= 1:
        for directory in cvsDirs:
          fullPath = os.path.join(treePath, directory)
          extTreeNode = self.__parseTree(fullPath)
          if extTreeNode is not None:
            treeNode.appendChildNode(extTreeNode)
            extTreeNode.setParentNode(treeNode)

      return treeNode
    else:
      return None

  def parseTree(self, treePath):

    treePath = os.path.abspath(treePath)
    treeNode = self.__parseTree(treePath)
    treeNode.updateAllRelPaths()

    return treeNode

if __name__ == "__main__":
  from pprint import pprint
  util = CvsTreeUtil()
  pprint(util.getSetupDataFiles('/tmp', 'examples'))
