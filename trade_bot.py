#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


stock_symbol = 'AAPL'  # Apple Inc. (you can choose any S&P 500 stock symbol)
start_date = '2022-01-01'
end_date = '2022-12-31'

stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
stock_data


# In[3]:


short_window = 50
long_window = 200

stock_data['Short_MA'] = stock_data['Close'].rolling(window=short_window).mean()
stock_data['Long_MA'] = stock_data['Close'].rolling(window=long_window).mean()


# In[4]:


stock_data


# In[6]:


print(stock_data.columns)


# In[9]:


plt.figure(figsize=(10, 6))
plt.plot(stock_data.index, stock_data['Close'], label='AAPL Close Price', color='blue')

# Plot the short and long moving averages
plt.plot(stock_data.index, stock_data['Short_MA'], label=f'Short {short_window} days MA', color='orange')
plt.plot(stock_data.index, stock_data['Long_MA'], label=f'Long {long_window} days MA', color='red')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('AAPL Stock Price with Moving Averages')
plt.legend()
plt.show()


# In[10]:


print(stock_data.head())


# In[12]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download historical data
stock_symbol = 'AAPL'
start_date = '2022-01-01'
end_date = '2022-12-31'
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Calculate MACD
short_window = 12
long_window = 26
signal_window = 9

stock_data['Short_MA'] = stock_data['Close'].rolling(window=short_window).mean()
stock_data['Long_MA'] = stock_data['Close'].rolling(window=long_window).mean()

stock_data['MACD'] = stock_data['Short_MA'] - stock_data['Long_MA']
stock_data['Signal_Line'] = stock_data['MACD'].rolling(window=signal_window).mean()

# Generate buy and sell signals
stock_data['Signal'] = 0  # 0 indicates no action

# Buy signal: MACD crosses above Signal Line
stock_data.loc[stock_data['MACD'] > stock_data['Signal_Line'], 'Signal'] = 1

# Sell signal: MACD crosses below Signal Line
stock_data.loc[stock_data['MACD'] < stock_data['Signal_Line'], 'Signal'] = -1

# Plot the stock prices, MACD, and Signal Line
plt.figure(figsize=(10, 6))
plt.plot(stock_data.index, stock_data['Close'], label='AAPL Close Price', color='blue')
plt.plot(stock_data.index, stock_data['Short_MA'], label=f'Short {short_window} days MA', color='orange')
plt.plot(stock_data.index, stock_data['Long_MA'], label=f'Long {long_window} days MA', color='red')
plt.plot(stock_data.index, stock_data['MACD'], label='MACD', color='green')
plt.plot(stock_data.index, stock_data['Signal_Line'], label='Signal Line', color='purple')

# Add buy and sell signals to the plot
buy_signals = stock_data[stock_data['Signal'] == 1]
sell_signals = stock_data[stock_data['Signal'] == -1]
plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='g', label='Buy Signal')
plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='r', label='Sell Signal')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('AAPL Stock Price with MACD Signals')
plt.legend()
plt.show()


# In[13]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download historical data
stock_symbol = 'AAPL'
start_date = '2022-01-01'
end_date = '2022-12-31'
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Calculate MACD
short_window = 25
long_window = 50
signal_window = 9

stock_data['Short_MA'] = stock_data['Close'].rolling(window=short_window).mean()
stock_data['Long_MA'] = stock_data['Close'].rolling(window=long_window).mean()

stock_data['MACD'] = stock_data['Short_MA'] - stock_data['Long_MA']
stock_data['Signal_Line'] = stock_data['MACD'].rolling(window=signal_window).mean()

# Generate buy and sell signals
stock_data['Signal'] = 0  # 0 indicates no action

# Buy signal: MACD crosses above Signal Line
stock_data.loc[stock_data['MACD'] > stock_data['Signal_Line'], 'Signal'] = 1

# Sell signal: MACD crosses below Signal Line
stock_data.loc[stock_data['MACD'] < stock_data['Signal_Line'], 'Signal'] = -1

# Plot the stock prices, MACD, and Signal Line
plt.figure(figsize=(10, 6))
plt.plot(stock_data.index, stock_data['Close'], label='AAPL Close Price', color='blue')
plt.plot(stock_data.index, stock_data['Short_MA'], label=f'Short {short_window} days MA', color='orange')
plt.plot(stock_data.index, stock_data['Long_MA'], label=f'Long {long_window} days MA', color='red')
plt.plot(stock_data.index, stock_data['MACD'], label='MACD', color='green')
plt.plot(stock_data.index, stock_data['Signal_Line'], label='Signal Line', color='purple')

# Add buy and sell signals to the plot
buy_signals = stock_data[stock_data['Signal'] == 1]
sell_signals = stock_data[stock_data['Signal'] == -1]
plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='g', label='Buy Signal')
plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='r', label='Sell Signal')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('AAPL Stock Price with MACD Signals')
plt.legend()
plt.show()


# In[ ]:




