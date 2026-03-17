from datetime import date, timedelta
import statsmodels.api as sm
import yfinance as yf
import pandas as pd

# Set the start and end dates
end_date = date.today().strftime("%Y-%m-%d")
start_date = (date.today() - timedelta(days=180)).strftime("%Y-%m-%d")

market = "^GSPC"  # S&P 500
ticker = "MSFT"   # Microsoft

print(f"Analyzing {ticker} against {market}")
print(f"Period: {start_date} to {end_date}\n")

# Retrieve prices using yfinance
sp = yf.download(market, start=start_date, end=end_date, progress=False)
stock = yf.download(ticker, start=start_date, end=end_date, progress=False)

# Calculate returns for S&P 500 and the stock
sp['ret_sp'] = (sp['Close'] / sp['Close'].shift(1)) - 1
stock['ret_stock'] = (stock['Close'] / stock['Close'].shift(1)) - 1

# Merge the two datasets, keep only returns
df = sp[['ret_sp']].merge(stock[['ret_stock']], 
                          left_index=True, right_index=True)

# Add risk-free rate (assume constant for simplicity)
df['rf'] = 0.00001

# Add constant for regression
df['const'] = 1

# Calculate excess returns
df['exret_stock'] = df.ret_stock - df.rf
df['exret_sp'] = df.ret_sp - df.rf

# Remove missing values
df.dropna(inplace=True)

print(f"Data points used: {len(df)}\n")

# Calculate the stock's alpha and beta using OLS regression
reg = sm.OLS(endog=df['exret_stock'],
             exog=df[['const', 'exret_sp']], 
             missing='drop')

results = reg.fit()
print(results.summary())

# Extract alpha and beta
alpha = round(results.params['const'] * 100, 3)
beta = round(results.params['exret_sp'], 2)

# Print the values of alpha and beta
print(f"\n{'='*50}")
print(f"The alpha of the stock of {ticker} is {alpha} percent.")
print(f"The beta of the stock of {ticker} is {beta}.")
print(f"{'='*50}")

# Interpretation
print("\nInterpretation:")
if alpha > 0:
    print(f"✓ {ticker} outperforms the market by {alpha}% (positive alpha)")
else:
    print(f"✗ {ticker} underperforms the market by {abs(alpha)}% (negative alpha)")

if beta > 1:
    print(f"✓ {ticker} is more volatile than the market (beta > 1)")
elif beta < 1:
    print(f"✓ {ticker} is less volatile than the market (beta < 1)")
else:
    print(f"✓ {ticker} moves with the market (beta ≈ 1)")