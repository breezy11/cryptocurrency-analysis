# cryptocurrency-analysis

It is a python library I created for fun. It does a simple analysis of cryptocurrencies and plots a few graphs to help visualize the trends.

Data is collected from Bitstamp exchange using cryptocompare API.

## Analyze function

```
def analyze(crypto_symbols, currency_symbol):
```

It accepts two paramaters. </br>
crypto_symbols is a list of cryptocurrency symbols.</br>
currency_symbol is the currency symbol in which the cryptocurrency is expressed in.</br>

It calculates: daily simple return, daily cumulative simple returns, volatility, mean / average daily simple return, correlation.</br>
The value used is the close price.</br>

In this example the cryptocurrencies used are: Bitcoin (BTC), Ripple (XRP), Ethereum (ETH) in USD value. </br>

#### Creates the dataframe in which the 'close' values of each asset are placed.
```
    df = pd.DataFrame()

    dates = df_current['Date']
    max_length = len(df_current['Date'])

    for crypto_symbol in crypto_symbols:
        data = download_data(crypto_symbol, currency_symbol)
        df_current = convert_to_dataframe(data)
        df_current = filter_empty_datapoints(df_current)
        df[crypto_symbol] = df_current['close']
        if (len(df_current['Date']) > max_length):
            dates = df_current['Date']

    df.index = dates
```

#### Show statistics of the data
    
|       | BTC          | XRP         | ETH         |
|-------|--------------|-------------|-------------|
| count | 2001.000000  | 1511.000000 | 1215.000000 |
| mean  | 6953.735677  | 0.358421    | 393.061053  |
| std   | 7999.433072  | 0.300364    | 345.098991  |
| min   | 225.930000   | 0.005390    | 82.910000   |
| 25%   | 965.010000   | 0.214950    | 175.305000  |
| 50%   | 6307.400000  | 0.284000    | 244.140000  |
| 75%   | 9283.530000  | 0.424200    | 469.105000  |
| max   | 57492.910000 | 2.751000    | 1958.160000 |

#### First graph compares the close prices of different cryptocurrencies.

```
plot(df, "Cryptocurrency Graph", "Date", "Crypto Price ($)", 3, 1)
```

![Cryptocurrency graph](https://github.com/breezy11/cryptocurrency-analysis/blob/master/graphs/cryptocurrency.png)

#### Second graph compares the close prices after data-scaling.

```
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 100))
    scaled = min_max_scaler.fit_transform(df)
    df_scaled = pd.DataFrame(scaled, columns=df.columns)
    df_scaled.index = df.index
    plot(df_scaled, "Cryptocurrency Scaled Graph", "Date", "Crypto Scaled Price ($)", 3, 1)
```

![Cryptocurrency scaled graph](https://github.com/breezy11/cryptocurrency-analysis/blob/master/graphs/cryptocurrency-scaled.png)

#### Third graph visualizes the daily simple returns.

```
plot(DSR, "Daily Simple Returns", "Date", "Percentage (in decimal form)", 2, .7)
```

![Daily simple returns](https://github.com/breezy11/cryptocurrency-analysis/blob/master/graphs/daily-simple-returns.png)

#### Fourth graph visualizes the daily cumulative simple returns.

```
plot(DCSR, "Daily Cumulative Simple Returns", "Date", "Growth of $1 investment", 3, 1)
```

![Daily cumulative simple returns](https://github.com/breezy11/cryptocurrency-analysis/blob/master/graphs/daily-cumulative-simple-returns.png)

#### Printing some values helpful for analysis.

Volatility

| BTC | 0.040230 |
|-----|----------|
| XRP | 0.089986 |
| ETH | 0.053255 |

Mean / average daily simple return.

| BTC | 0.003523 |
|-----|----------|
| XRP | 0.006045 |
| ETH | 0.002805 |
    
Correlation

|     | BTC      | XRP      | ETH      |
|-----|----------|----------|----------|
| BTC | 1.000000 | 0.340729 | 0.757424 |
| XRP | 0.340729 | 1.000000 | 0.588645 |
| ETH | 0.757424 | 0.588645 | 1.000000 |
    

## Other functions

#### Function that downloades the data and returns it as an argument.

```
def download_data(crypto_symbol, currency_symbol):
```

### Function that converts data downloaded from the internet into a dataframe.
```
def convert_to_dataframe(data):
```

### Function that clears the dataframe.
```
def filter_empty_datapoints(df):
```

### Function that accepts parameters and based on them draws the graphs accordingly.
```
def plot(data, title, xlabel, ylabel, lw, alpha):
```


