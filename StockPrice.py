# import required modules
import yfinance as yf
import streamlit as st

#title of the web app
st.write("""
# Stock Price App

Shown are the stock **closing price** and **volume price** of Google.

""")

# define the ticker symbol
ticker_symbol = 'GOOGL'
#get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)
# get the historical prices for this ticker
ticker_dataset = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open, High, Low, Close, Volume, Dividends, Stock Splits (columns in the data)
# subheading for closing price chart
st.write("""
## Closing Price
""")
# closing price chart
st.line_chart(ticker_dataset.Close)
# subheading for volume chart
st.write("""
## Volume Price
""")
# volume price chart
st.line_chart(ticker_dataset.Volume)


