"""File: friends.py
Author: Emily Savarese
Purpose: Finds mutual friends between 2 people.
#CSC 120, Section 1C, Fall 2018"""

from linked_list import *

import sys



def read_file(name_list):
    """edits the LinkedList name_list by adding each name
    provided in the file. Errors out if file not found.
    Preconditions: name_list is a LinkedList"""
    try:
        file=input("Input file: ")
        file=open(file)
    except:
        print("ERROR: Could not open file " + file)
        sys.exit(1)
        
    file=file.readlines()
    for i in range(len(file)):
        friends=file[i].strip().split()
        name1=Node(friends[0])
        name2=Node(friends[1])
        name_process(name1,name2,name_list)
        name_process(name2,name1,name_list)

        
   
        
def name_process(name1,name2,name_list):
    """if name1 is not already in name_list, then it is
    added and given temp2 (name2's .name) as a friend.
    If name1 is already in name_list, then it is retrieved
    from name_list and if temp2 not already in name1's friends
    LinkedList, then it is added.
    Preconditions: name1 is a Node, name2 is a Node, name_list is a
    LinkedList"""
    temp1=Node(name1.name())
    temp2=Node(name2.name())
    if not name_list.find_friend(name1):
        name1.give_friends(temp2)
        name_list.add(name1)
    else:
        adjustedname1=name_list.return_friend(name1)
        if not adjustedname1.friends().find_friend(name2):
            adjustedname1.friends().add(temp2)


    
def find_mutuals(name_list):
    """takes two user input names and checks to see
    whether they're in name_list. If so, they are
    retrieved from name_list and their mutuals are
    checked.
    Preconditions: name_list is a LinkedList"""
    find1=input("Name 1: ")
    check_friend(name_list,find1)
    find2=input("Name 2: ")
    check_friend(name_list,find2)

    friend1=name_list.find_str(find1)
    friend2=name_list.find_str(find2)

    friend1.friends().mutuals(friend2)

    

def check_friend(name_list,name):
    """exits the program if name is
    not found in name_list.
    Preconditions: name_list is a LinkedList,
    and name is a string.
    """
    if not name_list.find_str(name):
        print("ERROR: Unknown person " + name)
        sys.exit(1)
    
        




def main():
    """creates a LinkedList name_list before
    reading the file and then finding mutuals
    of friends."""
    name_list=LinkedList()
    read_file(name_list)
    find_mutuals(name_list)





main()
