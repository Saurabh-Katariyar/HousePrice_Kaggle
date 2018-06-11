

class dataprocess():
    import pandas as pd
#    def __init__(self):
        
        
      
    def clean(data):
        for col in data.columns:
            if data[col].dtype == 'object':
                if data[col].isnull().sum() > 50:
                    del data[col]
            

            elif data[col].dtype != 'object':
                if data[col].isnull().sum() > 50:
                    del data[col]
            
        for col in data.columns:
            if data[col].isnull().sum() != 0:
                if data[col].dtype == 'object':
                    data = data.fillna("XXX") 
                elif data[col].dtype != 'object':
                    data = data.fillna(data[col].median())
                


