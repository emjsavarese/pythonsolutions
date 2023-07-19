"""File: huffman.py
Author: Emily Savarese
Purpose: Produces a post order traversal and a number sequence from a inorder
traversal, preorder traversal, and a sequence of 1's and 0's. 
#CSC 120, Section 1C, Fall 2018"""


import sys


class Tree:
    def __init__(self):
        self._value = None
        self._ltree = None
        self._rtree = None

    def set_value(self,value):
        self._value = value

    def set_left(self,ltree):
        self._ltree = ltree

    def set_right(self,rtree):
        self._rtree = rtree

    def __str__(self):
        if self._value == None:
            return "None"
        else:
            return "({} {} {})".format(self._value, str(self._ltree), str(self._rtree))

    def is_leaf(self):
        """figures out whether or not tree is a leaf
        based on if it has no left and right nodes.
        postconditions: returns a boolean value."""
        return (self._ltree == None) and (self._rtree == None)

    def return_value(self):
        return self._value

    def return_left(self):
        return self._ltree

    def return_right(self):
        return self._rtree



def read_file(tree):
    """Reads in the given file, seperates
    the preorder, inorder, and prefix
    codes from eachother before constructing a
    tree.
    preconditons: tree is a Tree object.
    postconditions: onezerocode is a sequence of 1's and 0's"""
    try:
        file=input("Input file: ")
        file=open(file)
    except:
        print("ERROR: Could not open file " + file)
        sys.exit(1)

    file = file.readlines()
    preorder = file[0].strip().split()
    inorder = file[1].strip().split()
    onezerocode = file[2].strip()
    construct_tree(tree,preorder,inorder)
    return onezerocode
    

def construct_tree(tree, preorder,inorder):
    """Recursively creates a tree based on the preorder
    and the inorder lists. It locates the root,
    then finds which values are on its left and its
    right to then add as left and right subtrees.
    preconditions: tree is a Tree object, preorder is a list of numbers(branches for the current root),
    inorder is a list of numbers (roots for the tree).
    postconditions: tree is a Tree object."""
        if len(preorder) == 0 or len(inorder)==0:
            return
        else:
            root = preorder[0]
            tree.set_value(root)
            rootpos=inorder.index(root)
            leftvals = inorder[:rootpos]
            rightvals = inorder[rootpos+1:]
            tree.set_left(construct_tree(Tree(), preorder[1:rootpos+1], leftvals))
            tree.set_right(construct_tree(Tree(),preorder[rootpos+1:], rightvals))
            return tree
            
            
def decode(onezerocode,littletree,basetree):
    """Decodes the prefix code by traversing the tree;
    if the current number in the prefix code is a 0, it will
    traverse left, and if it's a 1, it will traverse right.
    precondtions: onezerocode is a sequence of 1's and 0's,
    littletree is a Tree object(used to search for current leaf),
    basetree is a Tree object (used to reset the tree when leaf is found).
    postconditions: returns string of numbers.
    """
    if littletree.is_leaf(): 
        return str(littletree.return_value()) + str(decode(onezerocode,basetree,basetree))
    if len(onezerocode) == 0:
        return ""
    else:
        if onezerocode[0] == "0":
            return "" + decode(onezerocode[1:],littletree.return_left(),basetree)
        else:
            return "" + decode(onezerocode[1:],littletree.return_right(),basetree)

    
def postorder(basetree):
    """recursively creates a string of a Tree object
    in a postorder fashion.
    preconditions: basetree is a Tree object.
    postconditions: a string is returned. """
    if basetree == None:
        return ""
    else:
        return str(postorder(basetree.return_left())) + str(postorder(basetree.return_right())) + str(basetree.return_value()) + " "



def main():
    basetree=Tree()
    onezerocode=read_file(basetree)
    post=postorder(basetree).rstrip()
    print(post)
    nums=decode(onezerocode,basetree,basetree)
    print(nums)
    




main()
