from fastapi_plotly.helpers import parse_datetime as p_d
import requests
import datetime
from config import settings
from fastapi import APIRouter

router = APIRouter()


@router.get("/api/fh/candles/")
async def finnhub_candle(ticker: str, resolution: str):
    token = settings.fh_key
    date_time = datetime.datetime.now()
    end = str(p_d.convert_to_unix(date_time))
    start = str(p_d.convert_to_unix(p_d.subtract_date(date_time, 364)))
    params = {
        "token": token,
        "from": start,
        "to": end,
        "resolution": resolution.upper(),
        "symbol": ticker.upper(),
    }
    r = requests.get("https://finnhub.io/api/v1/stock/candle", params=params)
    r_json = r.json()
    dates = map(lambda x: p_d.format_time(x), r_json['t'])
    response = {
        "status": r_json['s'],
        "ticker": ticker,
        "resolution": resolution,
        "time": list(dates),
        "open": r_json['o'],
        "high": r_json['h'],
        "low": r_json['l'],
        "close": r_json['c'],
        "volume": r_json['v']
    }

    return response  # json.dumps(response) - fastAPI default is json anyway
