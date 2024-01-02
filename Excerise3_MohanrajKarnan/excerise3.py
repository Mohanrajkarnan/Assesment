"""
Revenue of sales happend

Dependencies:
- pandas: A powerful data manipulation library.
- matplotlib: A plotting library for data visualization.
- statsmodels: A library for time series anaflalysis.

Usage:
1. Make sure you have the necessary dependencies installed.
2. Execute the script.

Author Information:
    Name: Mohanraj Karnan
    Date: 12 Nov 2023
    Contact: 

Abstract/Description:
This code will read the csv and provide total revenue of product
"""

import pandas as pd
import matplotlib.pyplot as plt

class SalesDataProcessor:
    def __init__(self, file_path):
        self.data = self._load_data(file_path)

    def _load_data(self, file_path):
        """
        This method will load the csv file and read using given path retrun dataframes
        """
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError as fe:
            print(f"File is not avaliable in the given path")
        except Exception as e:
            print(f"This is exception : {e}")

    def summarize_revenue(self):
        # TODO: Implement this method
        try:
            print(self.data.groupby(self.data['Product'])["Revenue"].sum())
        except Exception as e:
            print(f"This is exception : {e}")


    def plot_revenue_summary(self):
        # TODO: Implement this method
        pass

# Example usage
file_path = 'C:\\Users\\Mohanraj.Karnan\\.vscode\\TestWorplace\\de\\data.csv'
try:
    data_processor = SalesDataProcessor(file_path)
    data_processor.summarize_revenue()
except Exception as e:
    print(e)