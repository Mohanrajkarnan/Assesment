import pandas as pd
from time import time,ctime

def timeDecor(func):
    """
    This decorator func will take a input as function 
    and display the time taken for the function.
    """
    def wrapperfunc(*args,**kwargs):
        startTime = time()
        df_func = func(*args,**kwargs)
        endTime = time()
        print(f"***********************************************")
        print(f"Function start : {ctime(startTime)}")
        print(f"Function end : {ctime(endTime)}")
        print(f"Total time taken : {endTime-startTime} ms")
        print(f"***********************************************")
        return df_func
    return wrapperfunc

        
@timeDecor
def readJson(jsonPath):
    """
    Input : a valid JSON str, path (string)
    Output : Dataframe 
    Desc : This function will read json and return dataframe type.
    """
    try:
        return pd.read_json(jsonPath)
    except FileNotFoundError as fn:
        print(f"File is not present in the given location{fn}")
    except Exception as e:
        print(f"This is exception : {e}")
     

df_infile = readJson("practice.json")

# Calculate revenue -> price * quantity_sold
try:
    df_infile = df_infile.astype({'price': 'int64','quantity_sold': 'int64'})
    df_infile["revenue"] = df_infile.price * df_infile.quantity_sold
except TypeError as ty:
    print(f"Values in column is not in appropriate type :{ty}")
except ValueError as v:
    print(f"Values in column is not appropriate : {v}")
except Exception as e:
    print(f"This is exception : {e}")


# Get max of revenue
df_revenueMax = df_infile[df_infile.revenue == df_infile['revenue'].max()]





