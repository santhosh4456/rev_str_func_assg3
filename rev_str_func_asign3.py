#!/usr/bin/env python
# coding: utf-8

# In[1]:


def rev(s):
    str = " "
    for i in s:
        str = i + str
    return str
s = "1234abcd"
print("The reversed string is: ", end=" ")
print(rev(s))


# In[ ]:




