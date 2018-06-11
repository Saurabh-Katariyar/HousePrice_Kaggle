import pandas as pd
import numpy as np
from dataprocess import dataprocess
train = pd.read_csv('train.csv')

cat_var = train.dtypes.loc[train.dtypes == 'object'].index
con_var = train.dtypes.loc[train.dtypes != 'object'].index

#def clean(data):
#    for col in data.columns:
#        if data[col].dtype == 'object':
#            if data[col].isnull().sum() > 50:
#                del data[col]
#            
#
#        elif data[col].dtype != 'object':
#            if data[col].isnull().sum() > 50:
#                del data[col]
#            
#    for col in data.columns:
#        if data[col].isnull().sum() != 0:
#            if data[col].dtype == 'object':
#                data = data.fillna("XXX") 
#            elif data[col].dtype != 'object':
#                data = data.fillna(data[col].median())
                
dataprocess.clean(train)
   


