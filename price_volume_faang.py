import yfinance as yf
import streamlit as st
import pandas as pd
from PIL import Image


image = Image.open('yahoo_finance_en-US_h_p_financev2.png')

st.image(image, use_column_width=True)

st.write("""
# Aplicación Precios de FAANG
#### Precios y Volumen al cierre del mercado de FAANG

""")

#Seleccionar el Simbolo
st.sidebar.header('Seleccione la empresa')

tickerSymbol = st.sidebar.selectbox(
     'Seleccione la empresa de su preferencia:',
     ('FB', 'AMZN', 'AAPL', 'NFLX' ,'GOOGL'))

st.write('Empresa:', tickerSymbol)


#get data on this ticker

tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2009-5-31', end='2021-5-31')

# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.header('Precios al cierre')
st.line_chart(tickerDf.Close)

st.header('Volumen al cierre')
st.line_chart(tickerDf.Volume)