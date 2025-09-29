# 💵Stock-Prices-with-LSTM-Neural-Networks
Stock Price Predictor using LSTM (Long Short-Term Memory) model. This Streamlit app allows users to predict the next day's closing price of a stock by entering a ticker symbol and selecting a date range. The model is trained on historical stock data and visualizes the predicted price alongside historical trends.


**🚀 Overview:**

The Stock Price Predictor app allows users to:
- Input a stock ticker (e.g., AAPL, MSFT, TSLA).
- Choose a date range for historical stock data.
- Get the predicted next day's closing price based on the LSTM model.
- Visualize historical stock prices via an interactive line chart.
- The app fetches historical stock data using yfinance, scales the data using MinMaxScaler, and then feeds it into a pre-trained LSTM model to predict the next day’s price.
-------------------------------------------------

**🛠️ Technologies Used:**

- Streamlit: A Python framework to create interactive web apps.
- yfinance: For fetching stock market data from Yahoo Finance.
- NumPy & Pandas: For data manipulation and preprocessing.
- TensorFlow (Keras): For building, training, and using the LSTM model.
- Matplotlib: For visualizing the historical stock price data.

-------------------------------------------------

**⚙️ How to Use:**

git clone https://github.com/yourusername/stock-price-predictor.git
cd stock-price-predictor

-------------------------------------------------

**How it Works?:**
1) Data Collection: The app uses yfinance to download historical stock data (based on the selected ticker and date range).

2) Data Preprocessing:

  - The data is filtered to include only the closing prices.

  - It’s scaled between 0 and 1 using MinMaxScaler to normalize the data.

3) Model Prediction:

- The LSTM model is loaded using Keras (load_model("stock_lstm_model.h5")).

- The model predicts the next day’s stock price based on the last 60 days of closing prices.

4) Visualization:

- The app displays a line chart of the historical closing prices for the selected stock using Matplotlib and Streamlit’s line_chart feature.


