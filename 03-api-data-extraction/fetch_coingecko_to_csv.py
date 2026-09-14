"""
Week 2 Task - REST APIs & JSON
Fetches live cryptocurrency market data from the public CoinGecko API,
inspects the JSON response, and converts it into a CSV file for analysis.

API used: CoinGecko /coins/markets endpoint (no API key required)
Docs: https://docs.coingecko.com/reference/coins-markets
"""

import requests
import pandas as pd
from datetime import datetime

# ---------------------------------------------------------
# STEP 1: Define the API endpoint and query parameters
# ---------------------------------------------------------
BASE_URL = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "inr",        # get prices in Indian Rupees
    "order": "market_cap_desc",  # sort by biggest market cap first
    "per_page": 20,               # top 20 coins
    "page": 1,
    "sparkline": False
}

# ---------------------------------------------------------
# STEP 2: Call the API (GET request)
# ---------------------------------------------------------
print("Calling CoinGecko API...")
response = requests.get(BASE_URL, params=params)

# Always check the status code before trusting the response
print(f"Status Code: {response.status_code}")

if response.status_code != 200:
    raise Exception(f"API call failed: {response.status_code} - {response.text}")

# ---------------------------------------------------------
# STEP 3: Inspect the JSON response
# ---------------------------------------------------------
data = response.json()  # convert raw response text into a Python list/dict

print(f"\nNumber of records received: {len(data)}")
print("\nSample record (first coin):")
print(data[0])  # look at the structure of a single record

# ---------------------------------------------------------
# STEP 4: Select only the useful fields for analysis
# ---------------------------------------------------------
selected_fields = [
    "id",
    "symbol",
    "name",
    "current_price",
    "market_cap",
    "market_cap_rank",
    "total_volume",
    "high_24h",
    "low_24h",
    "price_change_percentage_24h",
    "circulating_supply",
]

cleaned_data = []
for coin in data:
    row = {field: coin.get(field) for field in selected_fields}
    cleaned_data.append(row)

# ---------------------------------------------------------
# STEP 5: Convert to a DataFrame and save as CSV
# ---------------------------------------------------------
df = pd.DataFrame(cleaned_data)

# Fix scientific notation issue for large numbers (e.g. circulating_supply)
# Formats to 3 decimal places as a plain string so Excel doesn't auto-convert
# large values into scientific notation (e.g. 1.22E+08).
df["circulating_supply"] = df["circulating_supply"].apply(
    lambda x: f"{x:.3f}" if pd.notnull(x) else ""
)

timestamp = datetime.now().strftime("%Y%m%d_%H%M")
output_file = f"crypto_market_data_{timestamp}.csv"
df.to_csv(output_file, index=False)

print(f"\nCSV saved successfully as: {output_file}")
print("\nPreview of the data:")
print(df.head(10))
