#!/usr/bin/env python
# coding: utf-8

# # Problem
# Given an integer array, output all the unique pairs that sum up to a specific value k.
# 
# So the input:
# 
# pair_sum([1,3,2,2],4)
# 
# would return 2 pairs:
# 
#  (1,3)
#  (2,2)
# 
# NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS

# In[18]:


def pair_sum(arr,k):
    
    # edge case check
    if len(arr) < 2:
        return
    
    # initialize sets for tracking
    seen = set()
    output = set()
    
    for num in arr:
        #set target difference
        target = k-num
        
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))
            
    #return len(output)
    print('\n'.join(map(str,list(output)))) 


# In[ ]:




