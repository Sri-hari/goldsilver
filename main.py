import requests
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Function to get metal prices from the API
def get_metal_prices(api_key, metals):
    url = f"https://metals-api.com/api/latest?access_key={api_key}&base=USD&symbols={','.join(metals)}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200 or 'rates' not in data:
        print("Failed to fetch data:", data.get("error", {}).get("info", "Unknown error"))
        return {}
    
    return data['rates']

# Function to visualize the metal prices
def visualize_prices(prices):
    # Convert data to pandas DataFrame
    df = pd.DataFrame(prices.items(), columns=['Metal', 'Price (USD per Ounce)'])
    
    # Plot the prices using a bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(df['Metal'], df['Price (USD per Ounce)'], color=['gold', 'silver'])
    plt.title(f"Gold and Silver Prices as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    plt.ylabel('Price (USD per Ounce)')
    plt.show()

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual API key from Metals-API
    api_key = 'YOUR_API_KEY'
    metals = ['XAU', 'XAG']  # XAU: Gold, XAG: Silver
    
    # Fetch prices
    prices = get_metal_prices(api_key, metals)
    
    if prices:
        print("Current metal prices (USD per ounce):")
        for metal, price in prices.items():
            print(f"{metal}: ${price}")
        
        # Visualize prices
        visualize_prices(prices)
