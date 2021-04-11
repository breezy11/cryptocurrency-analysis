# Imports
import pandas as pd
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn import preprocessing

# Set the plotting style
plt.style.use('fivethirtyeight')

# Private methods ------------------------------

def __download_data(crypto_symbol, currency_symbol):

    url = 'https://min-api.cryptocompare.com/data/histoday'

    params = {'fsym': crypto_symbol, 'tsym': currency_symbol,
              'limit': 2000, 'aggregate': 1,
              'e': 'Bitstamp', 'api_key': 'd7dbd7e6d9cae9935042cc55b1f85b7fa27322c9b1ed04e00895c5766dad41ee'}
    request = requests.get(url, params=params)
    data = request.json()
    return data

def __convert_to_dataframe(data):
    df = pd.json_normalize(data, ['Data'])
    df['Date'] = pd.to_datetime(df.time, unit='s')
    df = df[['Date', 'low', 'high', 'open',
             'close']]
    return df

def __filter_empty_datapoints(df):
    indices = df[df.sum(axis=1) == 0].index
    df = df.drop(indices)
    return df

def __plot(data, title, xlabel, ylabel, lw, alpha):
    fig, ax = plt.subplots(figsize=(14, 6))

    for c in data.columns.values:
        ax.plot(data[c], label=c, lw=lw, alpha=alpha)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
    plt.gcf().autofmt_xdate()

    ax.set(xlabel=xlabel,
           ylabel=ylabel,
           title=title)

    plt.legend(data.columns.values)
    plt.show()

#-----------------------------------------------

def price(crypto_symbol, currency_symbol):

    data = __download_data(crypto_symbol, currency_symbol)
    df = __convert_to_dataframe(data)
    df = __filter_empty_datapoints(df)

    return df

def analyze(crypto_symbols, currency_symbol):
    df = pd.DataFrame()

    data = __download_data(crypto_symbols[0], currency_symbol)
    df_current = __convert_to_dataframe(data)
    df_current = __filter_empty_datapoints(df_current)

    dates = df_current['Date']
    max_length = len(df_current['Date'])

    for crypto_symbol in crypto_symbols:
        data = __download_data(crypto_symbol, currency_symbol)
        df_current = __convert_to_dataframe(data)
        df_current = __filter_empty_datapoints(df_current)
        df[crypto_symbol] = df_current['close']
        if (len(df_current['Date']) > max_length):
            dates = df_current['Date']

    df.index = dates

    # Get statistics on the data
    print(df.describe())

    __plot(df, "Cryptocurrency Graph", "Date", "Crypto Price ($)", 3, 1)

    # Scale the data
    min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 100))
    scaled = min_max_scaler.fit_transform(df)

    # Convert the scaled data into a data frame
    df_scaled = pd.DataFrame(scaled, columns=df.columns)

    df_scaled.index = df.index

    # Visualize the scaled data
    __plot(df_scaled, "Cryptocurrency Scaled Graph", "Date", "Crypto Scaled Price ($)", 3, 1)

    # Get the daily simple return
    DSR = df.pct_change(1)

    # Visualize the daily simple return
    __plot(DSR, "Daily Simple Returns", "Date", "Percentage (in decimal form)", 2, .7)

    # Get the volatility
    print("The cryptocurrency volatility")
    print(DSR.std())

    # Show the mean / average daily simple return
    print("Average daily simple return")
    print(DSR.mean())

    # Get the correlation
    print("Correlation")
    print(DSR.corr())

    # Get the daily cumulative simple returns
    DCSR = (DSR + 1).cumprod()

    # Visualize the daily cumulative simple returns
    __plot(DCSR, "Daily Cumulative Simple Returns", "Date", "Growth of $1 investment", 3, 1)