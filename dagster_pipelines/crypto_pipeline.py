from dagster import op, job, RunRequest
import requests
from datetime import datetime
from dagster import DefaultRunLauncher

@op
def fetch_crypto_prices(context):
    """Fetch real-time prices for Bitcoin and Ethereum from CoinGecko."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if the request fails
    data = response.json()
    prices = [
        {"coin_id": "bitcoin", "price_usd": data["bitcoin"]["usd"], "timestamp": datetime.utcnow()},
        {"coin_id": "ethereum", "price_usd": data["ethereum"]["usd"], "timestamp": datetime.utcnow()}
    ]
    context.log.info(f"Fetched prices: {prices}")
    return prices

@op
def log_prices(context, prices):
    """Log the prices for now (we’ll add DB storage later)."""
    for price in prices:
        context.log.info(f"Coin: {price['coin_id']}, Price: {price['price_usd']}, Time: {price['timestamp']}")

@job
def crypto_ingestion_job():
    """Pipeline to fetch and log crypto prices."""
    log_prices(fetch_crypto_prices())