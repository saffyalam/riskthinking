import os
import pandas as pd

# Define the paths to the ETF and stock directories
etf_dir = r"C:\Users\safwana\pythonproject\etfs"
stock_dir = r"C:\Users\safwana\pythonproject\stocks"

# Create empty lists to hold the ETF and stock dataframes
etf_dfs = []
stock_dfs = []

# Loop through the CSV files in the ETF directory and read them into dataframes
for filename in os.listdir(etf_dir):
    if filename.endswith(".csv"):
        filepath = os.path.join(etf_dir, filename)
        df = pd.read_csv(filepath, usecols=["Symbol", "Security Name", "Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])
        etf_dfs.append(df)

# Loop through the CSV files in the stock directory and read them into dataframes
for filename in os.listdir(stock_dir):
    if filename.endswith(".csv"):
        filepath = os.path.join(stock_dir, filename)
        df = pd.read_csv(filepath, usecols=["Symbol", "Security Name", "Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])
        stock_dfs.append(df)

# Combine the ETF and stock dataframes into one
etfs_df = pd.concat(etf_dfs)
stocks_df = pd.concat(stock_dfs)
combined_df = pd.concat([etfs_df, stocks_df])

# Convert the combined dataframe to Parquet format
combined_df.to_parquet("combined_dataset.parquet")