import yfinance as yf
import streamlit as st
st.title("Simple Stock Price App")
tickerName = st.text_input("Enter name of the company ")
tickerSymbol = str(st.text_input("Enter its ticker"))
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='max')
st.write( """Shown are the stock **closing price** and ***volume*** of""" ,tickerName )

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
