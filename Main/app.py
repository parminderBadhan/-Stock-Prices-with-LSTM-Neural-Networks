import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

st.title("📈 Stock Price Predictor (LSTM)")

ticker = st.text_input("Enter stock ticker (e.g., AAPL)", "AAPL")
start = st.date_input("Start date", pd.to_datetime("2012-01-01"))
end = st.date_input("End date", pd.to_datetime("2019-12-17"))

if st.button("Predict Next Day's Price"):
    df = yf.download(ticker, start=start, end=end)
    data = df.filter([('Close' ,'AAPL')])
    dataset = data.values
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(dataset)
    last_60_days = data[-60:].values
    last_60_scaled = scaler.transform(last_60_days)
    X_future = np.array([last_60_scaled])
    X_future = np.reshape(X_future, (1, 60, 1))
    model = load_model("stock_lstm_model.h5")
    prediction = model.predict(X_future)
    predicted_price = scaler.inverse_transform(prediction)
    st.subheader(f"📅 Predicted next day's closing price: ${predicted_price[0][0]:.2f}")
    st.line_chart(data["Close"])
