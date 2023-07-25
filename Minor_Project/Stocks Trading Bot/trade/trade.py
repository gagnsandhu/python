"""
trading view module
"""
import json
from tradingview_ta import TA_Handler
from auth.stock_buy import check_balance

def price_of_stock(stock):
    handler = TA_Handler(
                symbol=stock,
                exchange="NSE",
                screener="india",
                interval="6h",
            )
    analysis=handler.get_analysis().indicators
    low_price=analysis.get('low')
    return low_price
