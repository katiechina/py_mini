import yfinance as yf
import streamlit as st


# st.write("""
# # Simple Stock Price App
# Shown are the stock closing price and volume of Google!
# """)

# #define the ticker symbol
# tickerSymbol = 'GOOGL'
# #get data on this ticker
# tickerData = yf.Ticker(tickerSymbol)
# #get the historical 10 years prices for this ticker
# tickerDf = tickerData.history(start='2011-6-22', end='2021-6-22')


# st.line_chart(tickerDf.Close)
# st.line_chart(tickerDf.Volume)


ticker_dict = {'Google':'GOOGL','Microsoft':'MSFT','Apple':'AAPL'}

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Which company would you like to be displayed?',
    (list(ticker_dict.keys()))
)


st.write(f"""
# Simple Stock Price App
Shown are the stock closing price and volume of {add_selectbox}!
""")

tickerSymbol = ticker_dict[add_selectbox]

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(start='2011-6-22', end='2021-6-22')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

