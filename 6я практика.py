#!/usr/bin/env python
# coding: utf-8

# In[1]:


def CountSize(a , b): #sozdaem funkciyu CountSize, kotoraya prinimaet 2 argumenta.
    counter = 0 #sozdaem schetchik mutaciy
    if len(a) == len(b): #proveryaem, ravni li stroki drug drugu po kolichestvu elementov
        for i in range (len(a)): #cikl dlya proverki kazhdogo elementa, gde i ot 0 do dlinni odnogo iz spiskov.
            if a[i] != b[i]: #sravnivaem kazhdiy element stroki A s sootvetstvuyuschim elementom stroki B.
                counter += 1 #esli sootvetstvuyuschie elementi ne ravni, to pribavlyaem 1 k schetchiq mutaciy.
        print(counter) #posle zaversheniya cikla, vizivaem znachenie schetchika oshibok
    else: print("wrong size") #eto esli spiski ne ravni po razmeru


# In[2]:


CountSize("AAAA" , "AAAT") #vizov funkciy
CountSize("AAAA" , "CCCT")
CountSize("AAAA" , "AAAA")


# In[ ]:




