from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import plot
import jinja2
import requests
from fastapi_plotly.helpers import parse_datetime as p_d
import datetime
from config import settings

router = APIRouter()

templates = Jinja2Templates(directory="fastapi_plotly/templates")
loader = jinja2.FileSystemLoader('fastapi_plotly/templates')


@router.get("/ohlcv", response_class=HTMLResponse)
async def ohlcv(request: Request, ticker: str, resolution: str, title="OHLCV"):
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
    data = {
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
    fig_p = go.Figure(data=go.Scatter(x=data['time'], y=data['close'], mode='lines'))
    fig_v = go.Figure(data=go.Bar(x=data['time'], y=data['volume']))
    fig_p.update_xaxes(spikemode="across+toaxis", spikedash='solid', spikethickness=2, spikecolor="lightblue")
    fig_p.update_layout(hovermode="x")
    fig_v.update_layout(hovermode="x")
    fig_pv = make_subplots(specs=[[{"secondary_y": True}]])
    fig_pv.add_trace(
        go.Scatter(
            x=data['time'], y=data['close'], name="price"
        ),
        secondary_y=False
    )
    fig_pv.add_trace(
        go.Bar(
            x=data['time'], y=data['volume'], name="volume"
        ),
        secondary_y=True,
    )
    fig_pv.update_yaxes(title_text="<b>Price</b>", secondary_y=False)
    fig_pv.update_yaxes(title_text="<b>Volume</b>", secondary_y=True)
    fig_pv.update_layout(hovermode="x")
    fig_pv.update_xaxes(spikemode="across+toaxis", spikedash='solid', spikethickness=1, spikecolor="lightblue")
    fig_div_price = plot(fig_p, output_type='div', include_plotlyjs=False, show_link=False, link_text="")
    fig_div_volume = plot(fig_v, output_type='div', include_plotlyjs=False, show_link=False, link_text="")
    fig_div_pv = plot(fig_pv, output_type='div', include_plotlyjs=False, show_link=False, link_text="")
    return templates.TemplateResponse(
        "ohlcv.html",
        {
            "request": request,
            "id": id,
            "fig_div_price": fig_div_price,
            "fig_div_volume": fig_div_volume,
            "fig_div_pv": fig_div_pv,
            "title": title}
        )
