import requests
from config import settings
from fastapi import APIRouter

router = APIRouter()


@router.get("/api/fh/earnings/")
async def finnhub_earnings(ticker: str):
    token = settings.fh_key
    params = {"token": token, "symbol": ticker.upper(), "limit": 4}
    r = requests.get("https://finnhub.io/api/v1/stock/earnings", params=params)
    r_json = r.json()
    response = {
        "ticker": ticker,
        "actual": [x["actual"] for x in r_json],
        "estimate": [x["estimate"] for x in r_json],
        "period": [x["period"] for x in r_json],
    }

    return response  # json.dumps(response) - fastAPI default is json anyway
