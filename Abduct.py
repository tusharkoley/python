#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Write a pyhton code to get Factors of a number

'''
This program tries find the sum of the abduct number. 
Which means the sum of its factos are grater than the original number
'''


# In[2]:


from math import floor 
def get_factor(n):
    lst=[]
    
    m=floor(n**0.5) +1

    if n<=2:
        return []
    if n%2==0:
        lst.append(2)
        lst.append( n//2)
        
    for i in range(3,m):
      
        if n%i==0:
            lst.append(i)
            lst.append(n//i)
            
    return lst
    


# In[4]:


get_factor(17)


# In[81]:


def is_abduct(n):
    lst=get_factor(n)
    return sum(lst)>n


# In[28]:





# In[112]:


size=30000

lst_ab=[]
for i in range(3,size):
    
    if( is_abduct(i) ):
        lst_ab.append(i)
        
s=set()
for l in lst_ab:
    for k in lst_ab:
        sm=l+k
        if(sm<size):
            s.add(sm)
            
lst_sum=list(s)
lst_all=list(range(1,size))

sm1=sum(lst_all)
sm2=sum(lst_sum)
            
sm1-sm2        


# In[ ]:




