# Cryptocurrency Analysis

It is a python library I created for fun. It does a simple analysis of cryptocurrencies and plots a few graphs to help visualize the trends. <br>
It can also return the historical data of any cryptocurrency.

Data is collected from the Bitstamp exchange using cryptocompare API.

## features

* Getting the historical data of any cryptocurrency
* Showing the statistics of an asset and visualizing it
* Showing the statistics of multiple assets and visualizing them <br> <br>
visualization (price movements, scaled price movements, daily returns, cummulative daily returns)

## install
Use the following pip command: <br>
`pip install cryptoanalysis`

## methods

`price(crypto_symbol, currency_symbol)`

Returns the historical daily 'OHLC' price of any cryptocurrency from its inception until today. <br>
The data is returned in a data frame. <br>
The data frame is filtered, and the NA values are removed.

-------------------------------------------------------------

`analyze(crypto_symbols, currency_symbol)`

Shows the statistics of data (count, mean, max, min, std, correlation, volatility, average daily simple returns). <br>
Plots four graphs (price, scaled price, daily returns, cummulative daily returns).<br>
You can analyze one or multiple cryptocurrencies. 

## examples

~~~~
df_btc = price('BTC', 'USD')
print(df_btc.head())
~~~~

|   | Date       | low    | high   | open   | close  |
|---|------------|--------|--------|--------|--------|
| 0 | 2015-10-20 | 262.67 | 272.95 | 264.28 | 270.23 |
| 1 | 2015-10-21 | 264.00 | 272.69 | 270.30 | 267.80 |
| 2 | 2015-10-22 | 267.39 | 280.04 | 267.90 | 275.30 |
| 3 | 2015-10-23 | 273.46 | 280.19 | 275.12 | 277.71 |
| 4 | 2015-10-24 | 278.22 | 283.00 | 278.60 | 282.59 |

-------------------------------------------------------------

~~~~
analyze(['BTC', 'XRP', 'ETH'], 'USD')
~~~~

Data statistics

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

Volatility

| BTC | 0.040230 |
|-----|----------|
| XRP | 0.089986 |
| ETH | 0.053255 |

Mean / average daily simple return

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

Price graph

![Cryptocurrency price graph](https://github.com/breezy11/cryptocurrency-analysis/blob/master/plots/multi/mult-price.png)

Scaled price graph

![Cryptocurrency scaled price graph](https://github.com/breezy11/cryptocurrency-analysis/blob/master/plots/multi/mult-scaled-price.png)

Daily simple returns graph

![Cryptocurrency daily simple returns graph](https://github.com/breezy11/cryptocurrency-analysis/blob/master/plots/multi/mult-simple-returns.png)

Daily cummulative simple returns graph

![Cryptocurrency daily cummulative simple returns graph](https://github.com/breezy11/cryptocurrency-analysis/blob/master/plots/multi/mult-cumm-returns.png)
