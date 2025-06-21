# -------------------------------------------
# Intraday Volatility-Based Selector
# Author : Shivanand
# -------------------------------------------

import yfinance as yf
import pandas as pd
import numpy as np

symbols = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS','ICICIBANK.NS','HDFCBANK.NS']

intervals = '1m'
period = '1d'

result = []

for symbol in symbols:
  print(f"\n Fetching Data for : {symbol}")

  df =  yf.download(tickers=symbol, interval=intervals, period=period, progress=False, auto_adjust=False)

  if df.empty or len(df) < 30:
    print(f"Not enough data for {symbol}. Skipping.")
    continue

  df.reset_index(inplace=True)

  df['log_return'] = np.log(df['Close'] / df['Close'].shift(1))

  df['rolling_volatility'] = df['log_return'].rolling(window=30).std()

  latest_vol = df['rolling_volatility'].iloc[-1]

  result.append({'Symbol' : symbol, 'Volatility' : latest_vol})


result_df = pd.DataFrame(result)
result_df.dropna(inplace=True)

mean_vol = result_df['Volatility'].mean()
std_vol = result_df['Volatility'].std()

result_df['Z_Score'] = (result_df['Volatility'] - mean_vol) / std_vol

result_df.sort_values(by='Z_Score', ascending=False, inplace=True)

print(f"\n Top Intraday Volatile Stocks : ")
print(result_df[['Symbol', 'Volatility', 'Z_Score']].head(5))

result_df.to_csv("data/volatility_rank.csv", index=False)