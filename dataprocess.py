

class dataprocess():
    import pandas as pd
#    def __init__(self):
        
        
    def clean(data):
        cat_var = data.dtypes.loc[data.dtypes == 'object'].index
        con_var = data.dtypes.loc[data.dtypes != 'object'].index
        
        for col in con_var:
            if data[col].isnull().sum() > 50:
                data = data.drop(columns = col)
            else:
                data = data.fillna(data[col].median())
        
        
        for col in cat_var:
            if data[col].isnull().sum() > 50:
                data = data.drop(columns = col)
            else:
                data = data.fillna("XXX")
                


