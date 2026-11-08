# TSX Stock Analyzer

Python tool that downloads Toronto Stock Exchanges (TSX) stock prices and measures how a stock has performed.

## Purpose

This is the starting point for a personal research paper on **momentum vs. mean reversion** in TSX stocks. Have stocks that have gone up keep going up, or do they tend to fall back?

## What it does

- Asks for a TSX ticker (exg. `RY` or `RY.TO`) and adds `.TO` if it's missing
- Keeps asking if the ticker isn't found
- Downloads daily prices from Nov 2024 to Nov 2026. The tool adjusts for dividends and splits
- The tool then prints the daily returns and the total return over the period
- Plots the price with a 50-day moving average

## How to run

Install the libraries:

```bash
pip install yfinance matplotlib
```

Run the program:

```bash
python main.py
```

## Planned next

- Rank several TSX stocks by their 6-month return (a simple momentum ranking)
- Test whether past winners keep outperforming afterward

## Built with

Python, yfinance, pandas, matplotlib
