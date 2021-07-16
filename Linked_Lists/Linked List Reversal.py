#!/usr/bin/env python
# coding: utf-8

# Linked List Reversal
# Problem
# Write a function to reverse a Linked List in place. The function will take in the head of the list as input and return the new head of the list.
# 
# You are given the example Linked List Node class:

# In[7]:


class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


# In[8]:


def reverse(head):
    # Set up current, previous and next nodes
    current = head
    previous = None
    nextnode = None
    
    # Go through to the end of the list
    while current:
        
        #copy the current nodes next node to a variable next_node
        #before ovewriting as the previous node for reversal
        nextnode = current.nextnode
        
        # Reverse the pointer of the next_node
        current.nextnode = previous
        
        # Go one forward in the list
        previous = current
        current = nextnode    


# In[9]:


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d


# In[10]:


reverse(a)


# In[13]:


print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)

