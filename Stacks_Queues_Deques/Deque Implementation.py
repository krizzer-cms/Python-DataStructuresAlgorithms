#!/usr/bin/env python
# coding: utf-8

# Implement a Deque
# Finally, implement a Deque class! It should be able to do the following:
# 
# Check if its empty
# Add to both front and rear
# Remove from Front and Rear
# Check the Size

# In[ ]:


def Deque(object):
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addRear(self,item):
        return self.items.insert(0,item)
    
    def addFront(self,item):
        return self.items.append(item)
    
    def removeRear(self):
        return self.items.pop(0)
    
    def removeFront(self):
        return self.items.pop()
    
    def size(self)
        return len(self.items)

