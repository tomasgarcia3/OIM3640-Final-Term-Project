# OIM3640-Final-Term-Project

## Crypto Trading Bot 💰

This crypto trading bot is 100% python. It uses the CCXT library to get information about ticker, used TA-LIB library for the analysis matrics, and Gemini Sanbox exchnage to place order. 

## Exchange API
**Gemini Sandbox API Needed:**
- https://exchange.sandbox.gemini.com/
- You need to create an account and then an API.
- The you will need to change the API in bot.py

```bash
#Update API
api = gemini.PrivateClient("EXAMPLE_PUBLIC_KEY", "EXAMPLE_PRIVATE_KEY", sandbox=True)
```

Gemini sandbox is a paper trading account created by Gemini which allows you to play around with fake money so you dont have to play with your own.

## Project Information and Instrucitons:
Refer to `project_webstite.html`

## Dependencies to Install:

**CCXT Library:**
- 'pip install ccxt'
- https://docs.ccxt.com/en/latest/manual.html

**TA-Lib Library:**
- 'pip install TA-Lib'
- https://pypi.org/project/TA-Lib/

If that does not work try this:
- https://www.youtube.com/watch?v=hZIZMMcTQ8c
- https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib

**Gemini:**
- 'pip install gemini_python'
- https://github.com/mtusman/gemini-python

**Pandas:**
- 'pip install pandas'
- https://pypi.org/project/pandas/

**DateTime:**
- 'pip install DateTime'
- https://pypi.org/project/DateTime/

**Time:**
- 'pip install times'
- https://pypi.org/project/times/

## Attributions
**CCXT functionalities:**
- https://docs.ccxt.com/en/latest/manual.html

**TAlib Indicators:**
- https://hexdocs.pm/talib/TAlib.Indicators.RSI.html

**Gemini API commands:**
- https://docs.gemini.com/rest-api/#get-notional-balances

**Time:**
- https://www.tutorialspoint.com/python/time_sleep.htm

**Projects:**
- https://medium.com/geekculture/building-a-basic-crypto-trading-bot-in-python-4f272693c375
- https://github.com/MaciejSzelest/Cryptocurrency-bot-Binance---API-/blob/main/main_bot.py
- https://github.com/pirate/crypto-trader/blob/master/README.md
- https://github.com/mtusman/gemini-python

## This bot can make/or lose money, Good luck!
