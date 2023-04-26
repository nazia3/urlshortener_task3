#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyshorteners


# In[2]:


import pyshorteners

url = input("Enter the URL: ")
s = pyshorteners.Shortener()
short_url = s.tinyurl.short(url)
print("Short URL:", short_url)


# In[ ]:




