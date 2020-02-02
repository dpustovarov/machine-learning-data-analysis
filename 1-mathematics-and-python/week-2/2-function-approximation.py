#!/usr/bin/env python
# coding: utf-8

# In[14]:


import math
from scipy import linalg
from matplotlib import pyplot


# In[6]:


def f(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)


# In[18]:


x0 = range(1, 16)
b = [f(x) for x in x0]
pyplot.plot(x0, b)


# In[28]:


def B(X):
    A = [[x**i for i in range(len(X))] for x in X]
    W = linalg.solve(A, [f(x) for x in X])
    return W, [sum(w * x**i for i, w in enumerate(W)) for x in x0]


# In[29]:


x2 = [1, 15]
w2, b2 = B(x2)
pyplot.plot(x0, b, x0, b2)


# In[30]:


x3 = [1, 8, 15]
w3, b3 = B(x3)
pyplot.plot(x0, b, x0, b2, x0, b3)


# In[35]:


x4 = [1, 4, 10, 15]
w4, b4 = B(x4)
pyplot.plot(x0, b, x0, b2, x0, b3, x0, b4)
print(w4)


# In[38]:


with open('submission-2.txt', 'w') as submission:
    submission.write(' '.join(str(w) for w in w4))


# In[ ]:




