#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Week 14 Assignment Part 1



def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("6th number of the Fibonnaci Sequence: {}".format(fibonacci(6)))


#Week 14 Assignment Part 2

def gcd(a,b): 
    if(b == 0):
        return a 
    else: 
        return gcd(b,a%b) 

print("GCD of 80 and 64 using Euclid’s Algorithm: {}".format(gcd(80, 64)))



#Week 14 Assignment Part 3

def compareTo(s1, s2):
    s1=str(s1)
    s2=str(s2)
    if s1 == s2:
        return 0
    elif s1 < s2:
        return "-1"
    elif s1 > s2:
        return "1"
    else:
        return compareTo(s1[1:], s2[1:])

print("Compare appples to apples: {}".format(compareTo("apples", "apples")))



# In[ ]:




