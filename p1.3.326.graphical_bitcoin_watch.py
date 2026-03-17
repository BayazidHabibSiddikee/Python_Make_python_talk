import arrow, requests, tkinter as tk 

def coin(currency="bitcoin"):
    """
    Display live cryptocurrency price tracker
    
    Parameters:
    currency: cryptocurrency name (e.g., 'bitcoin', 'ethereum', 'dogecoin')
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={currency}&vs_currencies=usd"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    root = tk.Tk()
    root.title(f"{currency.title()} Watch")
    root.geometry("400x200")
    
    label1 = tk.Label(root, text='', fg='Blue', font=("Helvetica", 30))
    label1.pack()
    
    label2 = tk.Label(root, text='', fg='Red', font=("Helvetica", 26))
    label2.pack()
    
    def update_price():
        """Update the price display"""
        try:
            response = requests.get(url, headers=headers, timeout=5)
            data = response.json()
            
            if currency in data:
                price = data[currency]['usd']
                
                # Update datetime
                label1.configure(text=f"{arrow.now().format('DD-MM-YYYY')}\n{arrow.now().format('HH:mm:ss A')}")
                # Update price
                label2.configure(text=f"{currency.title()}: ${price:,.2f}", justify=tk.LEFT)
            else:
                label2.configure(text=f"Currency '{currency}' not found")
            
            # Call again after 1000ms
            root.after(1000, update_price)
        
        except Exception as e:
            label2.configure(text=f"Error: {str(e)}")
            root.after(5000, update_price)  # Retry after 5 seconds
    
    # Start updating
    update_price()
    
    # Start GUI loop
    root.mainloop()

if __name__ == '__main__':
    # Examples:
    coin("bitcoin")          # Bitcoin price
    # coin("ethereum")       # Ethereum price
    # coin("dogecoin")       # Dogecoin price
    # coin("cardano")        # Cardano price