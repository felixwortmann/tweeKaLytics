#!/usr/bin/env python
# coding: utf-8

# ## Imports

# In[1]:


from pymongo import MongoClient
from bson.json_util import loads, dumps
import json
import nltk
from nltk.corpus import stopwords
import collections


# ## Stopwords

# In[2]:


nltk.download('stopwords')
stop_words = stopwords.words('english')


# ## Connecting to database

# In[3]:


# client = MongoClient('mongodb://localhost:27017')
# db = client['twitter']
# collection = db['tweets']


# ## Get data

# In[76]:


#data = json.loads(dumps(collection.find()))
with open("4-5-11-20_twitter_data.json", "r") as f:
    data = f.read()
print("Loaded")

# ## Rausfiltern der Tweet-Inhalte
# {
#     ('word', 'year'): #count
# }

# In[8]:


text_strings = []
for d in data:
    if "text" in d.keys():
        text_strings += [d["text"]]

words_dict = {}
for d in data:
    if not "text" in d.keys() or not "user" in d.keys() or not "created_at" in d["user"].keys() or d["user"]["created_at"] == None:
        continue
    text = d["text"].lower()
    created = d["user"]["created_at"][-4:]
    
    for word in text.split(' '):
        pair = (word, created)
        if pair in words_dict.keys():
            words_dict[pair] += 1
        else:
            words_dict[pair] = 1
words_dict


# ## Wort-Jahr-Anzahl

# In[12]:


#ignore_words = stop_words + ['rt', '', '-', '&amp;', 'like', 'get', 'one', 'via', 'new', 'i\'m']
words = [(k,v) for k, v in sorted(words_dict.items(), key=lambda item: -item[1])]
words


# ## Top-10 Wörter pro Jahr der Account-Erstellung

# In[56]:


result = {}

for pair in words_dict.keys():
    word, year = pair
    amount = (word, words_dict[pair])
    
    if year in result.keys():              
        result[year] = result[year] + [(word, words_dict[pair])]
            
    else:
        result[year] = [(word, words_dict[pair])]
        
result


# ## Durchschnittliches Alter der Accounts

# In[74]:


years = [int(year) for d in data if "user" in d.keys() for year in [d["user"]["created_at"][-4:]]]
sum(years) / len(years)


# In[ ]:




