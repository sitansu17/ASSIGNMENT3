#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20
#Explanation:
#Summation should like 8+2+3+0+7 = 20
#ANSWER:::::::
def sumn(x):
    print(sum(x))
sum([8,2,3,0,7])


# In[2]:


def sumn(x):
    s=0
    for i in x:
        s=s+x
    print(s)
sum([8,2,3,0,7])


# In[9]:


#(2).Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"
#ANSWER:::::
def rev(string):
    print(string[::-1])

rev("1234abcd")
    


# In[11]:


#(3).Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12
#ANSWER::::

def conv(string):
    up=0
    lo=0
    for i in string:
        if i.isalpha():
            if i.isupper():
                up=up+1
            else:
                lo=lo+1
    print("No of Upper case characters",up)
    print("No. of Lower case Characters",lo)
conv("The quick Brow Fox")


# In[ ]:




