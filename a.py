from coinbase.wallet.client import Client
import sys
if "-p" in sys.argv:
    try:
        print("Example: BTC-USD")
        while True:
            a = input("Pair:")
            b = a.split("-")
            client = Client("uKTLqtLprAtbNo96", "234SwoWOcpjquq0D5Ipg6xuBASn11z58", api_version='YYYY-MM-DD')
            price = client.get_buy_price(currency_pair=a)
            print('Current %s price in %s: %s' % (b[0], b[1], price.amount))
    except:
        print("Pair not found")
if len(sys.argv)==1:
    try:
        print("Example: BTC")
        print("Prices in USD")
        while True:
            a = input("Currency name:")
            client = Client("uKTLqtLprAtbNo96", "234SwoWOcpjquq0D5Ipg6xuBASn11z58", api_version='YYYY-MM-DD')
            currency_code = '-USD'
            price = client.get_buy_price(currency_pair=a + currency_code)
            print('Current %s price in %s: %s' % (a, "USD", price.amount))
    except:
        print("Pair not found")

