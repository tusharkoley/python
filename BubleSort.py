#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Bubble Sort and Factorial Demo

'''


# In[3]:


a=[3,4,5,11,9]


# In[11]:


def bubble( lst): 
    l=len(lst)
    for i in range(l-1):
        for j in range(l-i):       
            temp=lst[i]
      
            if( lst[i]>lst[i+1]):   
                lst[i+1]=lst[i]
                lst[i]=temp
            


# In[15]:


def fact(n):
    if n==1:
        return 1
        
    return( n*fact(n-1) )


# In[16]:


fact(5)

