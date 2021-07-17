#!/usr/bin/env python
# coding: utf-8

# Reverse a String
# This interview question requires you to reverse a string using recursion. Make sure to think of the base case here.
# 
# Again, make sure you use recursion to accomplish this. Do not slice (e.g. string[::-1]) or use iteration, there must be a recursive call for the function.

# In[1]:


# Solution 1 
def reverse(s):
    # Take last character in string and store it
    value = s[len(s)-1]

    if len(s) == 1:
        return s
    else:
        # Remove last character from string and call function
        s = s[:len(s)-1]
        return value + reverse(s)


# In[2]:


s = 'hello world'
reverse(s)


# In[3]:


# Solution 2
def reverse(s):
    
    # Base Case
    if len(s) <= 1:
        return s

    # Recursion
    return reverse(s[1:]) + s[0]


# In[4]:


s = 'hello world'
reverse(s)

