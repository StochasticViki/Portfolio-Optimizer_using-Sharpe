import tkinter as tk
from tkinter import messagebox, ttk
from investing import rf
from metrics import data_grab, weight_gen, metrics
import pandas as pd
import numpy as np

class PortfolioOptimizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Portfolio Optimizer")
        master.geometry("600x700")

        # Ticker Input Section
        tk.Label(master, text="Enter Stock Tickers (comma-separated):", font=("Arial", 12)).pack(pady=(10,5))
        self.ticker_entry = tk.Entry(master, width=50, font=("Arial", 10))
        self.ticker_entry.pack(pady=5)
        self.ticker_entry.insert(0, "aapl,msft,nvda")

        # Number of Iterations
        tk.Label(master, text="Number of Portfolio Iterations:", font=("Arial", 12)).pack(pady=(10,5))
        self.iterations_entry = tk.Entry(master, width=20, font=("Arial", 10))
        self.iterations_entry.pack(pady=5)
        self.iterations_entry.insert(0, "100")

        # Optimize Button
        self.optimize_button = tk.Button(master, text="Optimize Portfolio", command=self.optimize_portfolio, font=("Arial", 12))
        self.optimize_button.pack(pady=20)

        # Results Display
        self.results_frame = tk.Frame(master)
        self.results_frame.pack(pady=10, expand=True, fill='both')

        # Best Sharpe Ratio Portfolio Results
        tk.Label(master, text="Best Sharpe Ratio Portfolio", font=("Arial", 12, "bold")).pack()
        self.sharpe_results = tk.Text(master, height=10, width=70, font=("Courier", 10))
        self.sharpe_results.pack(pady=5)

        # Lowest Risk Portfolio Results
        tk.Label(master, text="Lowest Risk Portfolio", font=("Arial", 12, "bold")).pack()
        self.risk_results = tk.Text(master, height=10, width=70, font=("Courier", 10))
        self.risk_results.pack(pady=5)

    def optimize_portfolio(self):
        try:
            # Parse tickers
            tickers = [ticker.strip().lower() for ticker in self.ticker_entry.get().split(',')]
            iterations = int(self.iterations_entry.get())

            # Fetch prices
            prices = data_grab(tickers)
            rf_rate = rf()

            # Generate portfolios
            results = []
            for _ in range(iterations):
                weights = weight_gen(tickers)
                port_ret, port_risk, sharpe = metrics(prices, weights, tickers, rf_rate)
                results.append({
                    "Weights": weights,
                    "Return": port_ret,
                    "Risk": port_risk,
                    "Sharpe Ratio": sharpe
                })

            results_df = pd.DataFrame(results)
            sorted_by_sharpe = results_df.sort_values(by="Sharpe Ratio", ascending=False)
            sorted_by_risk = results_df.sort_values(by="Risk", ascending=True)

            best_sharpe = sorted_by_sharpe.iloc[0]
            lowest_risk = sorted_by_risk.iloc[0]

            # Clear previous results
            self.sharpe_results.delete('1.0', tk.END)
            self.risk_results.delete('1.0', tk.END)

            # Display Sharpe Ratio Portfolio Results
            sharpe_text = (
                f"Return:       {best_sharpe['Return']:.2f}\n"
                f"Risk:         {best_sharpe['Risk']:.2f}\n"
                f"Sharpe Ratio: {best_sharpe['Sharpe Ratio']:.2f}\n"
                f"Weights:      {' '.join([f'{t}: {w:.2f}' for t, w in zip(tickers, best_sharpe['Weights'])])}"
            )
            self.sharpe_results.insert(tk.END, sharpe_text)

            # Display Lowest Risk Portfolio Results
            risk_text = (
                f"Return:       {lowest_risk['Return']:.2f}\n"
                f"Risk:         {lowest_risk['Risk']:.2f}\n"
                f"Sharpe Ratio: {lowest_risk['Sharpe Ratio']:.2f}\n"
                f"Weights:      {' '.join([f'{t}: {w:.2f}' for t, w in zip(tickers, lowest_risk['Weights'])])}"
            )
            self.risk_results.insert(tk.END, risk_text)

        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = PortfolioOptimizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()