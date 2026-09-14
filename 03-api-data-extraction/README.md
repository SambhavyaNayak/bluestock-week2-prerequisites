# REST APIs & JSON — API Data Extraction Assignment

**Objective:** Understand how APIs work, inspect JSON responses, and convert live API data into a structured CSV file for analysis.

---

## Concepts Covered

- **What is an API?** — An interface that lets one application request data or services from another over HTTP.
- **HTTP Methods** — `GET` (retrieve data) and `POST` (send data) were used/tested.
- **JSON Format** — The API response structure, inspected as key–value pairs and nested objects/arrays.
- **API Documentation** — Read to understand available endpoints, parameters, and response schema.
- **Query Parameters** — Used to filter and shape the returned dataset (e.g., currency, number of results, page).
- **Authentication Basics** — Reviewed how APIs handle access (API keys, headers, rate limits), even where the endpoint used is public/keyless.

---

##  API Used

**CoinGecko API** — a free, public cryptocurrency market data API.
Endpoint used: `/coins/markets` (returns live market data for cryptocurrencies, including price, market cap, volume, and 24h change).

---

##  Tools

- **Postman** — used to manually send a `GET` request to the CoinGecko endpoint, inspect the raw JSON response, headers, and status code before writing any code.
- **Python** (`requests`, `pandas`, `csv`) — used to programmatically call the API and convert the JSON response into a CSV file.

---

## Files in This Folder

| File | Description |
|---|---|
| `postman_request.jpeg` | Screenshot of the API request and JSON response inspected in Postman. |
| `fetch_coingecko_to_csv.py` | Python script that calls the CoinGecko API and writes the response to a CSV file. |
| `crypto_market_data_20260915_00....csv` | Output CSV containing the extracted market data. |

---

## ⚙️ How It Works

1. **Inspect in Postman** — Sent a `GET` request to the CoinGecko markets endpoint with query parameters (e.g., `vs_currency=usd`, `order=market_cap_desc`, `per_page`, `page`). Reviewed the JSON response structure and field names.
2. **Fetch programmatically** — `fetch_coingecko_to_csv.py` sends the same `GET` request using Python's `requests` library.
3. **Parse JSON** — The JSON response (a list of coin objects) is parsed and relevant fields are selected (e.g., name, symbol, current price, market cap, 24h volume, price change %).
4. **Convert to CSV** — The parsed data is loaded into a `pandas` DataFrame and exported as a timestamped CSV file for downstream analysis.

### Run it yourself

```bash
pip install requests pandas
python fetch_coingecko_to_csv.py
```

This generates a new `crypto_market_data_<timestamp>.csv` file in the same folder.

---

##  Outcome

- Successfully called a public REST API and understood its request/response cycle.
- Inspected a real-world JSON payload structure end-to-end.
- Converted live API data into a clean, analysis-ready CSV file — a core step in any data analyst's workflow when working with FinTech or market data sources.