#!/usr/bin/env python
# coding: utf-8

# Problem
# Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.
# 
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
# 
# Input:
# 
# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
# 
# Output:
# 
# 5 is the missing number

# In[7]:


# O(NlogN) solution #1
def finder1(arr1, arr2):
    # Assume you only know that one element is missing 
    # Sort Arrays 
    arr1.sort()
    arr2.sort()
    
    #Compare arrays to find missing element in array 2 
    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    # return last element
    return arr1[-1]


# In[16]:


# log(N) solution #2
import collections
def finder2(arr1,arr2):
    # Helps avoid key errors by automatically adding key
    # if key is missing in the dictionary.
    d = collections.defaultdict(int)
    
    for num in arr2:
        d[num] += 1
        
    for num in arr1:
        if d[num] == 0:
            return num
         
        else:
            d[num] -= 1


# In[ ]:


# log(N) Time and O(1) Space complexity solution #3: Clever but 
# conceptually difficult to understand
def finder3(arr1, arr2): 
    result=0 
    
    # Perform an XOR between the numbers in the arrays
    for num in arr1+arr2: 
        result^=num 
        print result
        
    return result 

