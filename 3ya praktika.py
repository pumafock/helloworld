#!/usr/bin/env python
# coding: utf-8

# In[3]:


dic={'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '10#':'j', '11#':'k', '12#':'l', '13#':'m', '14#':'n', '15#':'o', '16#':'p', '17#':'q', '18#':'r', '19#':'s', '20#':'t', '21#':'u', '22#':'v', '23#':'w', '24#':'x', '25#':'y', '26#':'z'}

s = str(input("s = "))
l = list(s)
tmp = []
for i in range(0, len(l)):
    
    if i < len(l)-2:
        if l[i+2] == ("#"):
            l[i] = l[i]+l[i+1]+l[i+2]
            l.remove("#")
            l.pop(i+1)
            tmp.append(l[i])
            i+=2            
        else:
            tmp.append(l[i])

tmp2 = ''

for i in range(0, len(tmp)):
    if tmp[i] in dic:
        tmp2 += str(dic[tmp[i]])


print(tmp2)


# In[2]:





# In[ ]:




