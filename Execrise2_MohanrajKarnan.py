import pandas as pd



def converToDatafram(df):
    """
    This converToDataframe takes dict as input and returns dataframe type
    """
    return pd.DataFrame(data)

# Convert date column to datetime
def convertToDateTime(df):
    """
    This converToDataframe takes dataframe and column to convert to date format and returns dataframe type
    The value of the column should be in this format "yyyy-mm-dd" ,eg: "2021-01-15"
    """
    try:
        return pd.to_datetime(df['date'])
    
    except ValueError as e:
        print(f"Error in creating dataframe",{e})
        
    except Exception as e:
        print(f"Error in creating dataframe",{e})
        
        
        
if __name__ == "__main__":
    
    # Sample data
    data = {
        'date': ['2021-01-15', '2021-02-15', '2021-03-15', '2022-01-15', '2022-02-15'],
        'sales': [100, 200, 150, 300, 250]
    }
    
    
    df_data = converToDatafram(data)
    
    df_data['date'] = convertToDateTime(df_data)
    
    # Filter data for the year 2021
    df_2021 = df_data[df_data['date'].dt.year == 2021]
    
    # Group by month and sum sales
    monthly_sales_2021 = df_2021.groupby(df_2021['date'].dt.month).sum()
    print(monthly_sales_2021)