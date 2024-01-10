#!/usr/bin/env python
# coding: utf-8

# In[3]:


x="boat"
y=list(x)
print(y)


# In[4]:


def swap(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
swap(y,0,2)


# In[5]:


str="   "
d=str.join(y)
print(d)


# In[8]:


x="create"
y=list(x)
print(y)
def swap(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
swap(y,1,4) 
str="   "
d=str.join(y)
print(d)


# In[10]:


x="create"
y=list(x)
print(y)
def swap(list,pos1,pos2,pos3):
    list[pos1],list[pos2],list[pos3]=list[pos3],list[pos1],list[pos2]
    return list    
swap(y,1,3,5) 
str="   "
d=str.join(y)
print(d)
    


# In[ ]:





# In[ ]:





# In[12]:


x="smoke"
y=list(x)
print(y)


# In[15]:


y[0],y[4]=y[4],y[0]
print(y)


# In[19]:


word=""
z=word.join(y)
print(z)


# In[20]:


a="aditya"
b=list(a)
print(b)


# In[21]:


b[1],b[4]=b[4],b[0]
print(b)


# In[23]:


c=""
d=c.join(b)
print(d)


# In[24]:


a="cat"
b=list(a)
print(b)


# In[25]:


b[0],b[2]=b[2],b[0]
print(b)


# In[26]:


c=""
d=c.join(b)
print(d)


# In[3]:


x="create"
y=list(x)
print(y)


# In[4]:


y[0],y[2]=y[2],y[0]
print(y)


# In[5]:


y[0],y[4]=y[4],y[0]
print(y)


# In[7]:


z=""
a=z.join(y)
print(a)


# In[ ]:




