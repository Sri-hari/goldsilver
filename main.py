import requests
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def get_metal_prices(api_key, metals):
    url = f"https://metals-api.com/api/latest?access_key={api_key}&base=USD&symbols={','.join(metals)}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for HTTP codes 4xx/5xx
        data = response.json()

        # Check for API-specific error
        if 'error' in data:
            print(f"API Error: {data['error']['info']}")
            return {}
        
        # Ensure 'rates' is present in the response
        if 'rates' not in data:
            print("Error: 'rates' field not found in API response.")
            return {}

        return data['rates']

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Output HTTP error
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # Output request error
    except Exception as e:
        print(f"An unknown error occurred: {e}")  # Catch-all for any other errors

    return {}

def visualize_prices(prices):
    df = pd.DataFrame(prices.items(), columns=['Metal', 'Price (USD per Ounce)'])
    plt.figure(figsize=(10, 5))
    plt.bar(df['Metal'], df['Price (USD per Ounce)'], color=['gold', 'silver'])
    plt.title(f"Gold and Silver Prices as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    plt.ylabel('Price (USD per Ounce)')
    plt.show()

if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    metals = ['XAU', 'XAG']  # XAU: Gold, XAG: Silver
    
    prices = get_metal_prices(api_key, metals)
    
    if prices:
        print("Current metal prices (USD per ounce):")
        for metal, price in prices.items():
            print(f"{metal}: ${price}")
        
        # Visualize prices
        visualize_prices(prices)
