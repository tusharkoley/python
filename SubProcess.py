#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
This program Demonstrate how to do networking operation like tracerount by using Pythoon.
'''


# In[1]:



import subprocess

lst=['127.0.0.1','127.0.0.2']
for l in lst:
    address = l
    res = subprocess.call(['ping', '-c', '3', address])
    if res == 0:
        print ("ping to", address, "OK")
    elif res == 2:
        print("no response from", address)
    else:
        print ("ping to", address, "failed!")


# In[ ]:


traceroute = subprocess.Popen(["traceroute", '-w', '100','www.google.com'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

for line in iter(traceroute.stdout.readline,""):
    print(line)


# In[ ]:


traceroute = subprocess.Popen(["traceroute", '-w', '100','www.google.com'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

for line in iter(traceroute.stdout.readline,""):
    print(line)


# In[ ]:




