from stocks import schemas
from fastapi import status, HTTPException
import time
import requests

STOCK_GET = "https://priceapi.moneycontrol.com/techCharts/intra?symbol=<name>&resolution=1&from=<ptime>&to=<ctime>"

def show(stockId):
    current_time = int(time.time())
    current_time_one_ago = current_time - 100
    replacements = {
        "<name>": stockId,
        "<ptime>": str(current_time_one_ago),
        "<ctime>": str(current_time)
    }
    url = STOCK_GET
    for k,v in replacements.items():
        url = url.replace(k, v)
    response = requests.get(url)
    json_response = response.json()
    if json_response.get('data'):
        stockPrice = json_response['data'][0]['value']
        stockName = stockId
        return schemas.ShowStock(name = stockName, price = stockPrice)
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Stock with {stockId} not available')