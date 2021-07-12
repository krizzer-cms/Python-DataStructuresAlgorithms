#!/usr/bin/env python
# coding: utf-8

# In[4]:


def anagram(s1,s2):
    
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    # Edge Case Check
    if len(s1) != len(s2):
        return False
    # Create a counting dicitionary
    count = {}
    
    # Count freq of each letter appearance and make sure count is same
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    # Subtract from the count dictionary
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    # Check if dictionary is not equal to zero       
    for k in count:
        if count[k] != 0:
            return False
        
    return True

