#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:
 	""" a node and its child is a list """
	def __init__(self, data):
		self._data = data
		self._children = []
 
	def getdata(self):
		return self._data
 
	def getchildren(self):
		return self._children
 
	def add(self, node):
		self._children.append(node)
 
    # def go(self, data):
    #     for child in self._children:
    #         if child.getdata() == data:
    #             return child
    #     return None
 
class Tree:
	""" a multiway hierarchy tree """
	def __init__(self):
		self._head = Node('header')
 
	def linktohead(self, node):
		self._head.add(node)

	def add(self, node, child):	
		node.add(child)

	def get(self, node):
		leaflist = []
		self.getleaf(node, leaflist)
		return leaflist

	def getleaf(self, node, leaflist):
		for child in node.getchildren():
			if child.getchildren():
				self.getleaf(child, leaflist)
			else:
				leaflist.append(child)



                      
if __name__ == "__main__":
	'''
	define node
	'''
	a = Node('A')
	b = Node('B')
	c = Node('C')
	d = Node('D')
	e = Node('E')
	f = Node('F')
	g = Node('G')
	h = Node('H')
	i = Node('I')
	j = Node('J')
	k = Node('K')

	'''
	define tree
	'''
	Tree = Tree()
	Tree.linktohead(a)
	 
	Tree.add(a,b)
	Tree.add(a,c)
	Tree.add(a,d)
	Tree.add(a,e)
	Tree.add(b,f)
	Tree.add(b,g)
	Tree.add(c,h)
	Tree.add(c,i)
	Tree.add(f,j)
	Tree.add(f,k)

	#testcase
	b_leaves = Tree.get(a)
	for l in b_leaves:
		print str(l.getdata())+" ",

