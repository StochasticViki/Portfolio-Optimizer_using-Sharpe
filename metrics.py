import yfinance as yf
import numpy as np
import pandas as pd
from investing import rf

# Temporary Variables
choices = ["aapl", "msft"]
rf_rate = rf()

def data_grab(ticker_vector):
    
    prices_df = pd.DataFrame()

    for ticker in ticker_vector:
        data = yf.download(ticker, period="5y", interval="1d")

        temp_df = data[["Adj Close"]].copy()
        temp_df.reset_index(inplace = True)
        temp_df.rename(columns = {"Adj Close" : ticker}, inplace = True)

        if prices_df.empty:
            prices_df = temp_df
        else:
            prices_df = pd.merge(prices_df, temp_df, on="Date", how="outer")


    return prices_df


def weight_gen(choices):
    weights = np.random.rand(len(choices))
    weights /= weights.sum()
    return weights



def metrics(price, weights, choices, rf_rate):

    log_return = np.log(price[choices] / price[choices].shift(1))

    port_ret = np.sum(log_return.mean() * weights) * 252

    # Step 2: Calculate covariance matrix
    cov_matrix = log_return.cov() * 252

    # Step 3: Portfolio Variance using generalized formula
    portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))

    # Portfolio Risk (Volatility)
    port_risk = np.sqrt(portfolio_variance)

    sharpe = (port_ret - rf_rate) / port_risk

    return port_ret, port_risk, sharpe








