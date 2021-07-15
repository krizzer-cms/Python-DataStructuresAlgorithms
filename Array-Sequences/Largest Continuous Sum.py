#!/usr/bin/env python
# coding: utf-8

# Problem
# Given an array of integers (positive and negative) find the largest continuous sum.

# In[4]:


def large_cont_sum(arr):
    #edge case: check to see if array length in 0 
    if len(arr) == 0: 
        return 0
    
    #initialize sum counter for max and current sum equal to arr[0]
    max_sum = current_sum = arr[0]
    
    
    for num in arr[1:]:
        #find the max of the current sum and num
        current_sum = max(current_sum+num, num)
        #keep track of max sum compared to current sum
        max_sum = max(current_sum, max_sum)
    return max_sum
    
    


# In[5]:


arr = [1,2,-1,3,4,10,10,-10,-1]


# In[6]:


large_cont_sum(arr)

