#!/usr/bin/env python
# coding: utf-8

# In[17]:


def calcu (a, b):
    for i in range(a, b+1):
        if all(num and not i % num for num in (int(c) for c in str(i))):
            print(i, end=' ')


# In[21]:


calcu (1, 22)


# In[20]:





# In[ ]:




