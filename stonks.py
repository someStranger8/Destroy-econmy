
# imports
from robin_stocks import robinhood as rs
import random, os, datetime
import yfinance as yf
import numpy as np

# envirormental varibles
robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")

rs.login(username=robin_user, password=robin_pass, by_sms=True)

# stocks
stonks = ["GOOGL", "F", "AAPL", "BTC", "ETH-USD", "TWTR", "SBUX", "DOGE-USD", "MSFT", "AMZN", "TSLA", "NVDA", "WMT", "MA", "BAC", "CVX", "HD", "KO", "COST", "TM", "DIS", "PEP", "ADBE", "VZ", "NKE", "INTC", "WFC", "MCD", "UPS", "T", "TMUS", "TXN", "PYPL", "SONY", "SHOP", "V", "PFE", "BA", "FB", "MO", "TGT", "ABNB", "PGR", "UBER", "NGG", "GME", "CAT", "WISH", "MDLZ"]
bought_stocks = []
start = (datetime.date.today() - datetime.timedelta(365) )
end = datetime.datetime.today()

while True:
  if len(stonks) == 0:
    break

  else:
    rand = random.choice(stonks)
    stock_data = yf.download(rand, start=start, end=end, interval="1d")
    df = stock_data["Open"]
    df = df.values.tolist()

    if np.mean(df) > df[len(df) - 1]:
      rs.orders.order_buy_fractional_by_limit(rand, 5, 450, timeInForce='gtc', extendedHours=False)
      stonks.remove(rand)

    else:
      bought_stocks.append(rand)
      stonks.remove(rand)

rs.logout()
print(f"[*] the AI bought these stocks: {bought_stocks}\n")
print(f"[*] out of {len(stonks)} stocks")
