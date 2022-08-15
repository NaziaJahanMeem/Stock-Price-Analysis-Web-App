import yfinance as yf
import streamlit as st
import pandas as pd 

st.write("""

# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Google

""")

#defining the ticker symbol
tickerSymbol = 'GOOGL'

#getting data on this ticker 
tickerData = yf.Ticker(tickerSymbol)

#getting the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-5-31')

#Open   High    Low Close   Volume  Dividents   Stock Splits
st.write("""

# Open Price

""")
st.line_chart(tickerDf.Open)
st.write("""

# High Price

""")
st.line_chart(tickerDf.High)
st.write("""

# Low Price

""")
st.line_chart(tickerDf.Low)
st.write("""

# Closing Price

""")
st.line_chart(tickerDf.Close)

st.write("""

# Volume Price

""")
st.line_chart(tickerDf.Volume)

