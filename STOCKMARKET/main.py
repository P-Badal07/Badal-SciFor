from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

ALPHA_VANTAGE_API_KEY = 'OEDJDXHATRLVCXHG'


@app.get("/stock/{symbol}")
async def get_stock_info(symbol: str):
    """
    Get real-time stock quote for a given symbol.
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "Global Quote" in data:
            return data["Global Quote"]
        else:
            raise HTTPException(status_code=404, detail="Symbol not found")
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from Alpha Vantage")


@app.get("/stock/{symbol}/history")
async def get_stock_history(symbol: str):
    """
    Get historical stock data for a given symbol.
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "Time Series (Daily)" in data:
            return data["Time Series (Daily)"]
        else:
            raise HTTPException(status_code=404, detail="Historical data not available")
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from Alpha Vantage")


@app.get("/stock/{symbol}/company")
async def get_company_info(symbol: str):
    """
    Get company information for a given symbol.
    """
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from Alpha Vantage")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
