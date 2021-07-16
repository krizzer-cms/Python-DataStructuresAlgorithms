#!/usr/bin/env python
# coding: utf-8

# Balanced Parentheses Check
# 
# Problem Statement
# Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not.
# 
# You can assume the input string has no spaces.

# In[16]:


def balance_check(s):
    
    #Edge case
    if len(s)%2 != 0:
        return False
    
    # set of opening brackets
    opening = set('([{')
    
    # set of matches
    matches = set([('(',')'),('{','}'), ('[',']')])
    
    # Use list as Stack
    stack = []
    
    for paren in s:
        
        if paren in opening:
            stack.append(paren)
        else:
            
            #Check if there are parenthesis in Stack
            if len(stack) == 0:
                return False
            
            # Check last open parenthesis
            last_open = stack.pop()
            
            # Check if it has a closing match
            if (last_open,paren) not in matches:
                return False
            
    return len(stack) == 0

