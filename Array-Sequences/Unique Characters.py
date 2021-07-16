#!/usr/bin/env python
# coding: utf-8

# # Unique Characters in String

# Problem
# Given a string,determine if it is compreised of all unique characters. 
# For example, the string 'abcde' has all unique characters and should return True. 
# The string 'aabcde' contains duplicate characters and should return false.

# In[3]:


# Solution 1
def unique(s):
    
    l = len(s)
    
    #edge case for string of 0
    if l < 1:
        return print('empty string')
    
    #edge case for string of 1
    if l == 1:
        return True
    
    #initialize a set
    seen = set()
    
    for item in s:
        #if character matches in a string
        if item in seen:
            return False
        seen.add(item)
    return True
        


# In[ ]:


# Solution 2
def unique(s):
    return len(set(s)) == len(s)

