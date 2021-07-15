#!/usr/bin/env python
# coding: utf-8

# Sentence Reversal
# Problem
# Given a string of words, reverse all the words. For example:
# 
# Given:
# 
# 'This is the best'
# 
# Return:
# 
# 'best the is This'
# 
# As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
# 
# '  space here'  and 'space here      '
# 
# both become:
# 
# 'here space'

# In[ ]:


# 1st solution
def str_rev(s):
    return " ".join(reversed(s.split())) 


# In[ ]:


# 2nd solution
def str_rev(s):
    return " ".join(s.split()[::-1])


# In[ ]:


#3rd Solution
def str_rev(s):
    
    words = []
    length = len(s)
    spaces = [' ']
    
    # Index Tracker
    i = 0
    
    # While index is less than length of string
    while i < length:
        
        # If element isn't a space
        if s[i] not in spaces:
            
            # The word starts at this index
            word_start = i
            
            while i < length and s[i] not in spaces:
                
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1
        
    # Join the reversed words
    return " ".join(reversed(words))

