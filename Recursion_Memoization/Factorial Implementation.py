#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fact(n):
    # Base case
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


# In[2]:


fact(5)

