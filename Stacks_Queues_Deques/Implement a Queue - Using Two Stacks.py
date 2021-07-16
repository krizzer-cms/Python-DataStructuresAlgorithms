#!/usr/bin/env python
# coding: utf-8

# Implement a Queue - Using Two Stacks
# Given the Stack class below, implement a Queue class using two stacks! Note, this is a "classic" interview problem. Use a Python list data structure as your Stack.

# In[2]:


class Queue2Stacks(object):
    
    def __init__(self):
        
        # Two Stacks
        self.in_stack = []
        self.out_stack = []
     
    def enqueue(self, element):
        return self.in_stack.append(element)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
        pass


# Test Your Solution
# You should be able to tell with your current knowledge of Stacks and Queues if this is working as it should. For example, the following should print as such:

# In[3]:


"""
RUN THIS CELL TO CHECK THAT YOUR SOLUTION OUTPUT MAKES SENSE AND BEHAVES AS A QUEUE
"""
q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print (q.dequeue())


# In[ ]:




