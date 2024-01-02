"""
Author : Mohanraj Karnan
Class created on : 12/11/2023
"""
import pandas as pd
import logging

class ProcessCsv():
    def __init__(self,path):
        self.path = path
    def readCsv(self):
        """
        Input : a valid CSV path (string)
        Output : Dataframe 
        Desc : This function will read Csv and return dataframe type.
        """
        try:
            return pd.read_csv(self.path)
        except FileNotFoundError as fe:
            logging.error(f"The file is not avaliable in the path")

    def getSchema(self,df):
        """
        This is return schema
        """
        return df.columns
       

processCsv = ProcessCsv("sales.csv")
df_input = processCsv.readCsv()
df_col = processCsv.getSchema(df_input)
print(df_col)
