import pandas
import time

# Exchange used for trading
import gemini

# TA-LIB is a technical analysis library
import talib

#CCXT library
import ccxt
exchange = ccxt.binance()

#Collect Data
def collect_data(ticker):
    ticker_data = None
    bars = exchange.fetch_ohlcv(ticker, timeframe="1m", limit=100)

    ticker_data = pandas.DataFrame(
        bars[:-1], columns=["at", "open", "high", "low", "close", "vol"]
    )
    ticker_data["symbol"] = ticker

    return ticker_data

# print(collect_data("ETH/USDT")) ## Test Function

# Trading strategy
def trade_signal(ticker_data):
    # Ta-lib module parameters
    RSI_PERIOD = 14
    RSI_OVERBOUGHT = 60
    RSI_OVERSOLD = 30
    signal = "WAIT"
    # BUY or SELL based RSI value
    rsi = talib.RSI(ticker_data["close"], RSI_PERIOD)
    final_rsi = rsi.iloc[-1]
    print(f"RSI: {final_rsi}")
    if final_rsi <= RSI_OVERSOLD:
        signal = "BUY"
    elif final_rsi >= RSI_OVERBOUGHT:
        signal = "SELL"
    return signal

# print(trade_signal(collect_data("ETH/USDT"))) ## Test function

#Update API
api = gemini.PrivateClient("EXAMPLE_PUBLIC_KEY", "EXAMPLE_PRIVATE_KEY", sandbox=True)

# Place order
def place_order(recommendation, gemini_ticker):
    global api, holding
    order_placed = False
    signal = "buy" if (recommendation == "BUY") else "sell"
    ticker_info = api.get_ticker(gemini_ticker)
    price = float(ticker_info["last"])

    quantity = (
        round(100 / price, 5) if recommendation == "BUY" else holding
    )
    print(
        f"Placing order: "
        f"{gemini_ticker}, {signal}, {price}, {quantity}, {int(time.time() * 1000)} "
    )
    order = api.new_order(
        str(gemini_ticker), str(quantity), str(price), str(signal)
    )
    print(f"Order response: {order}")

    holding = quantity if recommendation == "BUY" else holding
    order_placed = True

    return order_placed

# print(place_order("BUY", "ETHUSD")) ## Test function

#Putting everything together
def run_bot(ccxt_ticker, gemini_ticker):
    currently_holding = False
    while True:
        # Collect data
        ticker_data = collect_data(ccxt_ticker)
        # Tarding strategy
        recommendation = trade_signal(ticker_data)
        print(f'Trading Recommendation: {recommendation}')
        # Place Order
        if (recommendation == 'BUY' and not currently_holding) or \
            (recommendation == 'SELL' and currently_holding):
            print(f'Placing {recommendation} order')
            trade_successful = place_order(recommendation,gemini_ticker)
            currently_holding = not currently_holding if trade_successful else currently_holding
        # Bot sleeps before repeating
        time.sleep(60)
            

ccxt_ticker = 'ETH/USDT'
gemini_ticker = 'ETHUSD'

if __name__ == "__main__":
    run_bot(ccxt_ticker,gemini_ticker)
