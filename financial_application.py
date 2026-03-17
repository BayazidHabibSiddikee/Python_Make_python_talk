import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd


def stock():
    # Get stock ticker
    ticker_symbol = "AMZN"
    stock = yf.Ticker(ticker_symbol)
    # Get current price
    price = stock.info.get("regularMarketPrice")
    company_name = stock.info.get("longName", "Company")
    print(f"{company_name} has stock price ${price}")
    # Set start and end dates
    s_date = "2020-09-01"
    e_date = "2021-02-01"
    # Get historical data
    data = stock.history(start=s_date, end=e_date)
    print(data)
    # Check if data is empty
    if data.empty:
        print("No data retrieved! Check your ticker symbol and dates.")
    else:
        # Reset index to convert Date from index to column
        data = data.reset_index()
        # Convert dates to matplotlib format
        data['Date_num'] = mdates.date2num(data['Date'])
        # Create figure with size and DPI
        fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
        
        # Format date for x-axis
        formatter = mdates.DateFormatter('%m/%d/%Y')
        ax.xaxis.set_major_formatter(formatter)
        
        # Plot data
        ax.plot(data['Date_num'], data['Close'], c='blue', linewidth=2, label='Adjusted Close')
        
        # Format plot
        ax.set_title(f"The Stock Price of {company_name}", fontsize=16, fontweight='bold')
        ax.set_xlabel('Date', fontsize=10)
        ax.set_ylabel("Price ($)", fontsize=10)
        
        # Auto-format x-axis date labels
        fig.autofmt_xdate(rotation=45)
        
        # Add grid for better readability
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        plt.tight_layout()
        plt.show()
        
if __name__=='__main__':
    stock()