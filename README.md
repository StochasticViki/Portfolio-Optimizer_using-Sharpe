# Portfolio Optimizer (Indian Portfolio)

## Overview
A Python-based portfolio optimization tool that helps investors find optimal stock portfolios (consisting of indian securities) using modern portfolio theory.

## Features
- Scrape indian risk-free rate from investing.com
- Download historical stock price data from YahooFinance
- Generate random portfolio weights
- Calculate portfolio metrics:
  - Expected return
  - Portfolio risk
  - Sharpe ratio
- Interactive Tkinter GUI for portfolio analysis

## Prerequisites
- Python 3.8+
- Libraries: 
  - beautifulsoup4
  - requests
  - yfinance
  - numpy
  - pandas
  - tkinter

## Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install beautifulsoup4 requests yfinance numpy pandas tk
```

## Usage
Run the main application (main.py):
```bash
python src/main.py
```

Enter stock tickers from YahooFinance's website and number of iterations/simulations (atleast 2000 is recommended) in the GUI.

## Example
Input tickers: RELIANCE.NS, ADANIPORTS.NS, JPPOWER.BO
Iterations: 2000
- Generates portfolios with different weights
- Finds portfolio with maximum Sharpe ratio
- Finds portfolio with minimum risk (Volatility/Standard Deviation)

## Contributing
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create pull request

## License
MIT License
