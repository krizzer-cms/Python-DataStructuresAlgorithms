#!/usr/bin/env python
# coding: utf-8

# Singly Linked List Cycle Check
# Problem
# Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".
# 
# A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.
# 
# You've been given the Linked List Node class code:

# In[1]:


class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


# In[2]:


def cycle_check(node):
    # Both markers begin at first node
    marker1 = node
    marker2 = node
    
    # Go until end of list
    while marker2 != None and marker2.nextnode != None:
        
        # Note
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode
        
        # Check if markers have matched
        if marker2 == marker1:
            return True
        
    # Case where marker ahead reaches the end of the list
    return False


# In[3]:


# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.nextnode = b
b.nextnode = c
c.nextnode = d


# In[4]:


cycle_check(a)


# In[5]:


# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = a # Cycle Here!


# In[6]:


cycle_check(a)

