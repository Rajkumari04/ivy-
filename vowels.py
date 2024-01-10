#!/usr/bin/env python
# coding: utf-8

# # Write a program to check whether a given word contains vowels or not Also detail the number of vowels present.

# In[8]:


vowels=input("enter the any word :")
x=['a','e','i','o','u']
count=0
for i in vowels:
    if i in x:
        count +=1
print("the number of vowels is: ",count)        


# In[ ]:




