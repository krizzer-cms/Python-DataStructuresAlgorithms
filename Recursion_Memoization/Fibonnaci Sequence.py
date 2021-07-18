#!/usr/bin/env python
# coding: utf-8

# Fibonnaci Sequence
# In this interview excercise we will begin to get a feel of having to solve a single problem multiple ways!
# 
# Problem Statement
# Implement a Fibonnaci Sequence in three different ways:
# 
# Recursively
# Dynamically (Using Memoization to store results)
# Iteratively
# Function Output
# Your function will accept a number n and return the nth number of the fibonacci sequence
# 
# Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with a base case checking to see if n = 0 or 1, then it returns 1.
# 
# Else it returns fib(n-1)+fib(n+2).

# # Recursively

# In[1]:


def fib_rec(n):
    # base check 
    if n == 0 or n == 1:
        return n

    else:
        return fib_rec(n-1) + fib_rec(n-2)


# In[2]:


get_ipython().run_cell_magic('timeit', '', 'fib_rec(10)')


# # Dynamically (with Memoization)

# In[3]:


fb_memo = {}

def fib_dyn(n):
    
    if n == 0 or n == 1: 
        return n
    
    if not n in fb_memo:
        fb_memo[n] = fib_dyn(n-1) + fib_dyn(n-2)
        print(fb_memo)
    return fb_memo[n]


# In[4]:


get_ipython().run_cell_magic('timeit', '', 'fib_dyn(10)')


# In[9]:


# Instantiate Cache information
n = 10
cache = [None] * (n + 1)


def fib_dyn(n):
    
    # Base Case
    if n == 0 or n == 1:
        return n
    
    # Check cache
    if cache[n] != None:
        return cache[n]
    
    # Keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    print(cache)
    
    return cache[n]


# In[11]:


get_ipython().run_cell_magic('timeit', '', 'fib_dyn(10)')


# In[10]:


get_ipython().run_cell_magic('timeit', '', 'fib_dyn(10)')


# # Iteratively 

# In[7]:


def fib_iter(n):
    
    # Set starting point
    a = 0
    b = 1
    
    # Follow algorithm
    for i in range(n):
        
        a, b = b, a + b

    return a


# In[8]:


get_ipython().run_cell_magic('timeit', '', 'fib_iter(10)')

