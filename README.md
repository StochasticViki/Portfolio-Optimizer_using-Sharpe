# Portfolio Optimizer

## Overview
A Python-based portfolio optimization tool that helps investors find optimal stock portfolios using modern portfolio theory.

## Features
- Scrape risk-free rate from financial websites
- Download historical stock price data
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
Run the main application:
```bash
python src/main.py
```

Enter stock tickers and number of iterations in the GUI.

## Example
Input tickers: AAPL, MSFT, NVDA
Iterations: 100
- Generates portfolios with different weights
- Finds portfolio with maximum Sharpe ratio
- Finds portfolio with minimum risk

## Contributing
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create pull request

## License
MIT License
