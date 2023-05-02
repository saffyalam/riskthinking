import os
import pandas as pd
import logging

logging.basicConfig(filename='pipeline.log', level=logging.INFO)

# Define the paths to the ETF and stock directories
etf_dir = r"C:\Users\safwana\pythonproject\etfs"
stock_dir = r"C:\Users\safwana\pythonproject\stocks"

# Define the path to the output directory
output_dir = r"C:\Users\safwana\pythonproject\output"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create empty lists to hold the ETF and stock dataframes
etf_dfs = []
stock_dfs = []

# Loop through the CSV files in the ETF directory and read them into dataframes
for filename in os.listdir(etf_dir):
    if filename.endswith(".csv"):
        filepath = os.path.join(etf_dir, filename)
        df = pd.read_csv(filepath)
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)
        df["vol_moving_avg"] = df["Volume"].rolling(window=30).mean()
        df["adj_close_rolling_med"] = df["Adj Close"].rolling(window=30).median()
        etf_dfs.append(df)

# Loop through the CSV files in the stock directory and read them into dataframes
for filename in os.listdir(stock_dir):
    if filename.endswith(".csv"):
        filepath = os.path.join(stock_dir, filename)
        df = pd.read_csv(filepath)
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)
        df["vol_moving_avg"] = df["Volume"].rolling(window=30).mean()
        df["adj_close_rolling_med"] = df["Adj Close"].rolling(window=30).median()
        stock_dfs.append(df)

# Combine the ETF and stock dataframes into one
etfs_df = pd.concat(etf_dfs)
stocks_df = pd.concat(stock_dfs)
combined_df = pd.concat([etfs_df, stocks_df])

# Write the resulting dataset to a new CSV file in the output directory
output_filepath = os.path.join(output_dir, "combined_dataset_with_metrics.csv")
combined_df.to_csv(output_filepath, index=False)
