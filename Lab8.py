#!/usr/bin/env python
# coding: utf-8

# In[30]:


from urllib.request import urlopen
from urllib.request import urlopen
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
target_url0 = 'http://www.gutenberg.org/files/135/135-0.txt'
book_raw = urlopen(target_url0).read().decode('utf-8')


# In[31]:


type(book_raw)


# In[32]:


len(book_raw)


# In[33]:


book_raw[1:250]


# In[34]:


import nltk
nltk.download('punkt')
word_tokens = word_tokenize(book_raw)


# In[35]:


print(book_raw[1:200])


# In[ ]:


print(word_tokens[1:40])


# In[ ]:


import nltk
nltk.download('stopwords')


# In[ ]:


print(book_raw[1:200])


# In[ ]:


print(word_tokens[1:40])


# In[ ]:


from nltk.tokenize import sent_tokenize
Miserables_sentences = sent_tokenize(book_raw)


# In[ ]:


Miserables_sentences[1001]


# In[29]:


from nltk import FreqDist 
fdist_example = FreqDist(example)
example = ['a', 'a', 'The', 'The','The', ]


# In[ ]:




