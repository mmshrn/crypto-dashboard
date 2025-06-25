# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 13:00:19 2025

@author: M-Shirinzad
"""

import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import time

st.set_page_config(page_title="Live Crypto Dashboard", layout="wide")

st.title("📊 Live Cryptocurrency Dashboard")


coins = st.multiselect("Select coins to display", ["BTC-USD", "ETH-USD", "DOGE-USD"], default=["BTC-USD", "ETH-USD"])
interval = st.selectbox("Refresh Interval (seconds)", [5, 10, 30, 60])

placeholder = st.empty()

while True:
    data = {}
    for coin in coins:
        ticker = yf.Ticker(coin)
        df = ticker.history(period="1d", interval="1m")
        df.reset_index(inplace=True)
        data[coin] = df

    with placeholder.container():
        st.subheader("Live Price Charts")
        for coin in coins:
            fig = px.line(data[coin], x="Datetime", y="Close", title=f"{coin} Live Price")
            st.plotly_chart(fig, use_container_width=True)

    time.sleep(interval)