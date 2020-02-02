#!/usr/bin/env python
# coding: utf-8

# In[36]:


import re
from scipy.spatial import distance


# In[37]:


with open('sentences.txt') as file:
    sentences = [[word for word in re.split(r'[^a-z]+', line.lower()) if word] for line in file]


# In[38]:


words = set().union(*sentences)
print(words, len(words))


# In[39]:


counts = [[s.count(w) for w in words] for s in sentences]


# In[40]:


distances = sorted(enumerate([distance.cosine(counts[0], c) for c in counts]), key = lambda t: t[1])
print(distances)


# In[41]:


with open('submission-1.txt', 'w') as submission:
    submission.write(' '.join(str(distances[i][0]) for i in range(1, 3)))


# In[ ]:




