import yfinance as yf
import streamlit as st

st.title("Simple Stock Price App")

tickerSymbol ="TSLA"

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='max')

st.write( """Shown are the stock **closing price** and ***volume*** of TESLA """)
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
