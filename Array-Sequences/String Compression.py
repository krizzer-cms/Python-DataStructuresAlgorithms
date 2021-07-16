#!/usr/bin/env python
# coding: utf-8

# In[ ]:


String Compression
Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.


# In[3]:


def compress(s):
    # edge check for string of 0
    if len(s) == 0:
        return ''
    
    if len(s) == 1:
        return s + '1'
    
    
    # Initialize Iterator
    letter = s[0]
    count = 1
    i = 1
    #Initialize string
    string = ''
    
    while i < len(s):
        if s[i] == s[i-1]:
            # add count if same as previous
            count += 1
        else:
            # store previous data
            string = string + s[i-1] + str(count)
            # reset counter
            count = 1
        # add index count to terminate while loop
        i += 1
    string = string + s[i-1] + str(count)
    return string
        
        

