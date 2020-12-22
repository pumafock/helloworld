#!/usr/bin/env python
# coding: utf-8

# In[1]:


def evaluate (x):
    U=1
    S=0
    for i in range(len(x)):
        if x[i] % 2 == 0:
            U=U*x[i]
        else:
            S=S+x[i]
    print (S-U)


# In[2]:


x = [1,3,4,2,9]
evaluate (x)


# In[ ]:




