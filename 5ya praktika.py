#!/usr/bin/env python
# coding: utf-8

# In[28]:


import os
#biblioteka funkciy dlya raboti s operacionnoy sistemoy.


# In[34]:


def CountSize(a):
    dirs = os.listdir(a) #sozdaem spisok file'ov dannoy directorii, !gde dirs = directories!
    size = 0 #vvodim peremennuyu, dlya oboznacheniya summi.
    for file in dirs: #nachinaetsa cikl, gde mi obraschaemsya k kazhndomu file'u, nahodyaschihsya v spiske file'ov dannoy directorii.
        size += os.path.getsize(a) #razmer kazhdogo file'a pribavlyaetsa k summe.
    print(size)


# In[37]:


CountSize('C:\\Users\Acer\Desktop\projects')


# In[38]:


os.listdir('C:\\Users\Acer\Desktop\projects')


# In[ ]:




