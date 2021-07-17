#!/usr/bin/env python
# coding: utf-8

# Problem 1
# Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer
# 
# For example, if n=4 , return 4+3+2+1+0, which is 10.
# 
# This problem is very similar to the factorial problem presented during the introduction to recursion. Remember, always think of what the base case will look like. In this case, we have a base case of n =0 (Note, you could have also designed the cut off to be 1).
# 
# In this case, we have: n + (n-1) + (n-2) + .... + 0

# In[1]:


def rec_sum(n):
    # base case
    if n == 1:
        return 1
    else:
        return n + rec_sum(n-1)


# In[2]:


rec_sum(4)


# Problem 2
# Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1

# In[3]:


# Solution 1
def sum_func(n):
    # Base case
    if n == 0:
        return 0
    
    # Recursion
    return (n%10) + sum_func(int(n/10))


# In[4]:


sum_func(4321)


# In[5]:


# Solution 2
def sum_func(n):
    # Base case
    if len(str(n)) == 1:
        return n
    
    # Recursion
    else:
        return n%10 + sum_func(int(n/10))


# In[6]:


sum_func(4321)


# Problem 3
# Note, this is a more advanced problem than the previous two! It aso has a lot of variation possibilities and we're ignoring strict requirements here.
# 
# Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable.

# In[7]:


def word_split(phrase, list_of_words, output = None):
    
    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []
        
    # For every word in list
    for word in list_of_words:
        
        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):
            
            # Add the word to the output
            output.append(word)
            
            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split(phrase[len(word):],list_of_words,output)
    
    # Finally return output if no phrase.startswith(word) returns True
    return output 


# In[8]:


word_split('themanran',['the','ran','man'])


# In[9]:


word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])


# In[10]:


word_split('themanran',['clown','ran','man'])

