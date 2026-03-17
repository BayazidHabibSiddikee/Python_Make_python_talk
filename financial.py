from mptpkg import print_say
import requests
import sys
import yfinance as yf
import arrow
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def get_ticker_from_company(company_name):
    """Get stock ticker symbol from company name using Yahoo Finance API"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        url = f"https://query1.finance.yahoo.com/v1/finance/search?q={company_name}"
        response = requests.get(url, headers=headers, timeout=10)
        res = response.json()
        
        if res.get('quotes') and len(res['quotes']) > 0:
            symbol = res['quotes'][0]['symbol']
            return symbol
        else:
            print_say("No ticker found for that company name!")
            return None
    except Exception as e:
        print_say(f"Error retrieving ticker: {e}")
        return None


def stock(ticker=None, company_name=None):
    """
    Display stock price and historical graph
    
    Parameters:
    ticker: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
    company_name: Company name (e.g., 'Apple', 'Google') - will be converted to ticker
    """
    
    # If company name is provided, get ticker symbol
    if company_name:
        print_say(f"Looking up ticker for {company_name}...")
        ticker = get_ticker_from_company(company_name)
        if ticker is None:
            return
    
    # Default to AMZN if no ticker provided
    if ticker is None:
        ticker_symbol = "AMZN"
        print_say("No ticker provided, using default: AMZN")
    else:
        ticker_symbol = ticker
    
    try:
        stock_obj = yf.Ticker(ticker_symbol)
        
        # Get current price and company info
        price = stock_obj.info.get("regularMarketPrice")
        company_full_name = stock_obj.info.get("longName", ticker_symbol)
        
        if price is None:
            print_say(f"Could not retrieve price for {ticker_symbol}")
            return
        
        say = f"{company_full_name} (Ticker: {ticker_symbol}) has stock price ${price}"
        print_say(say)
        
        # Set date range - last 30 days to today
        e_date = arrow.now().format("YYYY-MM-DD")
        s_date = arrow.now().shift(days=-30).format("YYYY-MM-DD")
        
        print(f"Fetching data from {s_date} to {e_date}...")
        
        # Get historical data
        data = stock_obj.history(start=s_date, end=e_date)
        
        # Check if data is empty
        if data.empty:
            print_say("No data retrieved! Check your ticker symbol and dates.")
            return
        
        print(data)
        
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
        ax.plot(data['Date_num'], data['Close'], c='blue', linewidth=2, label='Close Price')
        
        # Format plot
        ax.set_title(f"Stock Price of {company_full_name} ({ticker_symbol})", 
                     fontsize=16, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel("Price ($)", fontsize=12)
        
        # Auto-format x-axis date labels
        fig.autofmt_xdate(rotation=45)
        
        # Add grid for better readability
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print_say(f"Error: {e}")
        print_say("Sorry, not a valid entry!")


if __name__ == '__main__':
    # Example usage:
    
    # Method 1: Use company name directly
    stock(company_name='jpmorgan chase')
    
    # Method 2: Use ticker symbol directly
    # stock(ticker='AAPL')
    
    # Method 3: Interactive mode
    # while True:
    #     company = input("Enter company name (or 'done' to quit): ").lower()
    #     if company == 'done':
    #         break
    #     stock(company_name=company)