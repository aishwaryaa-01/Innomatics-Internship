#!/usr/bin/env python
# coding: utf-8

# # task 1

# In[1]:


#1


# In[2]:


if __name__ == '__main__':
    print("Hello, World!")


# In[3]:


#2


# In[4]:


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    #n = int(raw_input().strip())
    #n = int(raw_input())
if n %2 != 0 or 5<n<21:print ("Weird")
else:print ("Not Weird")


# In[5]:


#3


# In[6]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    #a = int(raw_input())
    #b = int(raw_input())
    print(a+b)
    print(a-b)
    print(a*b)


# In[7]:


#4


# In[8]:


from __future__ import division

if __name__ == '__main__':
    
    a = int(input())
    b = int(input())
    #a = int(raw_input())
    #b = int(raw_input())

print(a//b)
print(a/b)


# In[9]:


#5


# In[16]:


if __name__ == '__main__':
    n = int(input())
    

for k in range(n):
    print(k * k)  


# In[11]:


#6


# In[10]:


def LeapYear(y):  #y=year
    LEAP = False
    
    # Write your logic here
    if y%4 == 0:
        if(y%100 != 0 or y%400 == 0):LEAP = True
    return LEAP
    return LEAP

y = int(input())
print(LeapYear(y))


# In[15]:


#7


# In[14]:


from __future__ import print_function

if __name__ == '__main__':
    n = int(input())
    #n = int(raw_input())
for k  in range(n):
        print(k+1,end='')


# In[ ]:




