
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


train = pd.read_csv('train.csv')
train.head(5)


# In[3]:


for col in train.columns:
    if train[col].isnull().sum() != 0:
        print(col)


# In[4]:


for col in train.columns:
    if train[col].dtype == 'object':
        if train[col].isnull().sum() > 50:
            print("Droping Column : {}".format(col))
            train = train.drop(columns = col)

    elif train[col].dtype != 'object':
        if train[col].isnull().sum() > 50:
            print("Droping Column : {}".format(col))
            train = train.drop(columns = col)


# In[5]:


train.head()


# In[10]:


for col in train.columns:
    if train[col].isnull().sum() != 0:
        if train[col].dtype == 'object':
            train = train.fillna("XXX") 
        elif train[col].dtype != 'object':
            train = train.fillna(train[col].median())
        


# In[20]:


train.head()

