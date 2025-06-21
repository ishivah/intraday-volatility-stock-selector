# Intraday Volatility-Based Stock Selector

A Python tool that ranks NSE stocks by their intraday volatility using 1-minute price data.

## Features

- Downloads 1-minute OHLCV data using `yfinance`
- Calculates log returns and rolling volatility
- Computes Z-score to rank stocks by volatility
- Prints top 3 volatile stocks intraday

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/intraday-volatility-stock-selector.git
cd intraday-volatility-stock-selector
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python src\volatility_selector.py
