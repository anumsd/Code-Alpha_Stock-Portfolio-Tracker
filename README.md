# Stock-Portfolio-Tracker_Code-Alpha
This is a simple Stock Portfolio Manager written in Python that allows users to track and manage their stock investments. It utilizes the yfinance library to fetch real-time stock data, including current prices, and calculates the performance of each stock in the user's portfolio based on the number of shares and purchase prices.

Features
Add Stocks: Add a stock to the portfolio by specifying the stock ticker, the number of shares, and the purchase price.
Remove Stocks: Remove a stock from the portfolio by specifying the stock ticker.
View Portfolio: Display all the stocks in the portfolio, including the current market price and the performance (gain or loss) for each stock based on the difference between the current price and purchase price.
Track Performance: The total performance of the portfolio is displayed, helping users keep track of their overall investment gains or losses.
How it Works
The program fetches real-time stock data from Yahoo Finance using the yfinance library.
Users can add stocks by entering the stock ticker, the number of shares, and the purchase price.
The portfolio stores the stocks with the associated details, and users can view the portfolio to see the performance of their investments.
Users can remove stocks from the portfolio as needed.
Technologies Used
Python 3.x
yfinance: A Python library for fetching real-time stock market data from Yahoo Finance.
json: For managing portfolio data (if extended for persistent storage).
Requirements
Python 3.x
yfinance (You can install it via pip install yfinance)
