"""Assorted functions to sort the list of parsed input returned by an input
translator.
"""
from __future__ import nested_scopes
import copy
import warnings
from warnings import warn

def computeDependencyGraph(classes):
  """Compute graph showing which objects inherit from which other objects
  """
  class TreeNode:
    def __init__(self, name=None, classMetaInfo = None):
      self.name = name
      self.parents = []
      self.children = []
      self.visited = 0
      self.classMetaInfo = classMetaInfo
      
  def findVertex(branch, name):
    """Given a branch, search through the leaves for a name.

    In this code a branch is a tree starting from the top level dictionary
    we keep.
    """
    for child in branch.children:
      if name == child.name:
        return child
      else:
        node = findVertex(child, name)
        if node is not None:
          return node
    return None
  
  def addVertex(tree, parentMap, vertex):
    """Add a vertex/node to the correct part of the tree
    """
    vertexName, (vertexParentList, classMetaInfo) = vertex
    # if this vertex depends on nothing just go ahead and add it to the top
    # level
    if len(vertexParentList) == 0:
      tree[vertexName] = TreeNode(vertexName, classMetaInfo)
    else:
      # we depend on something, so go look for it/them
      while len(vertexParentList) > 0:
        vertexParent = vertexParentList.pop()
        # is it already in the top level?
        if tree.has_key(vertexParent):
          node = TreeNode(vertexName, classMetaInfo)
          node.parents.append(tree[vertexParent])
          tree[vertexParent].children.append(node)
        # is it in the unadded verticies?
        elif parentMap.has_key(vertexParent):
          # add parent
          grandparents = parentMap[vertexParent]
          del parentMap[vertexParent]
          addVertex(tree, parentMap, (vertexParent, grandparents))
          # be lazy, and just reset the current state so other branches
          # can add
          vertexParentList.append(vertexParent)
        # it's somewhere in the tree
        else:
          nodes_added = 0
          for branch in tree.values():
            parent = findVertex(branch, vertexParent)
            if parent is not None:
              node = TreeNode(vertexName, classMetaInfo)
              node.parents.append(parent)
              parent.children.append(node)
              nodes_added += 1
          if nodes_added == 0:
            warn("graph build error, parent %s missing" % (vertexParent),
                 RuntimeWarning)

  # build parentMap
  parentMap = {}
  for c in classes:
    parentMap[c.getName(None)] = (copy.copy(c.getBaseClassNames(None)), c)

  # build the tree
  tree = {}
  while len(parentMap) > 0:
    vertex = parentMap.popitem()
    addVertex(tree, parentMap, vertex)

  return tree

def forwardDeclarationSort(classes):
  """Order a list of classes so forward declaration requirements are met.

  Since the class heirarchy can inherit from itself, we need to make
  sure that classes are declared after their parent class. 
  """
  
  def addSortedNode(list, node):
    """Insert a node into the correct place in the declaration list.
    """
    if node.visited == 0:
      # display all parents
      for parent in node.parents:
        addSortedNode(list, parent)
      list.append(node.classMetaInfo)
      node.visited = 1
      for child in node.children:
        addSortedNode(list, child)
        
    return list
            
  tree = computeDependencyGraph(classes)
  # construct the list sorted by declaration
  list = []
  for node in tree.values():
    addSortedNode(list, node)
    
  return list
