import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
         
Shown are   the stocks closing price and volume of Google!
""")

tickerSymbol = 'GOOGL'
# tickerSymbol = 'aapl'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2023-5-1', end='2023-6-1')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)