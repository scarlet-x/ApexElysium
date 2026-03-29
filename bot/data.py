import ccxt
import pandas as pd

exchange = ccxt.binance()

def get_ohlcv(symbol, timeframe):
    bars = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=150)

    df = pd.DataFrame(bars, columns=[
        "time","open","high","low","close","volume"
    ])

    return df
