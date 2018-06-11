import pandas as pd
import numpy as np

train = pd.read_csv('train.csv')

cat_var = train.dtypes.loc[train.dtypes == 'object'].index
con_var = train.dtypes.loc[train.dtypes != 'object'].index
def clean(train):
    train = pd.DataFrame(train)
    for col in train.columns:
        if train[col].dtype == 'object':
            if train[col].isnull().sum() > 50:
                train = train.drop(columns = col)           
            

        elif train[col].dtype != 'object':
            if train[col].isnull().sum() > 50:
                train = train.drop(columns = col)
            
    for col in train.columns:
        if train[col].isnull().sum() != 0:
            if train[col].dtype == 'object':
                train = train.fillna("XXX") 
            elif train[col].dtype != 'object':
                train = train.fillna(train[col].median())
                
clean(train)
    
#def cleandata(data):
#    
##    for col in con_var:
##        if data[col].isnull().sum() > 50:
##                data = data.drop(col, 1)
##        else:
##                data = data.fillna(data[col].median())
##        
##        
##    for col in cat_var:
##        if data[col].isnull().sum() > 50:
##                data = data.drop(col, 1)
##        else:
##                data = data.fillna("XXX") 
#                
#    for col in data.columns:
#        if data[col].dtype == 'object':
#            if data[col].isnull().sum() > 50:
#                data = data.drop(columns = col)           
#            
#
#        elif data[col].dtype != 'object':
#            if data[col].isnull().sum() > 50:
#                data = data.drop(columns = col)
#            
#    for col in data.columns:
#        if data[col].isnull().sum() != 0:
#            if data[col].dtype == 'object':
#                data = data.fillna("XXX") 
#            elif data[col].dtype != 'object':
#                data = data.fillna(data[col].median())    
#                
##cleandata(train)


