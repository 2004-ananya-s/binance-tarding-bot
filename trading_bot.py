from binance.client import Client
import logging

# ========== Step 1: Setup Logging ==========
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# ========== Step 2: Create Bot Class ==========
class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.API_URL = 'https://testnet.binancefuture.com/fapi'
        print("✅ Connected to Binance Futures Testnet")

    def check_balance(self):
        try:
            balance = self.client.futures_account_balance()
            for asset in balance:
                if asset['asset'] == 'USDT':
                    print(f"💰 USDT Balance: {asset['balance']}")
            logging.info("Fetched account balance")
        except Exception as e:
            print("❌ Failed to fetch balance:", e)
            logging.error(f"Balance error: {e}")

    def place_order(self, symbol, side, quantity, order_type, price=None):
        order_data = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity
        }

        if order_type == "LIMIT":
            order_data['price'] = price
            order_data['timeInForce'] = 'GTC'

        # Simulated order response (Testnet errors avoided)
        order = {
            'orderId': 123456,
            'status': 'FILLED',
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'price': price or 'Market Price',
            'quantity': quantity
        }

        print(f"✅ SIMULATED Order placed: {order}")
        logging.info(f"Simulated order: {order}")

# ========== Step 3: Enter Your API Keys ==========
API_KEY = "965d3ab6858efebcd5131dffd93669773c9f6bad7039d0cd57401435ed1d96ae"
API_SECRET = "09c2d9bc4f9a54caabc5399181e357b1cb1ee030202b09d5caa379019cf6e2f4"

# ========== Step 4: Create Bot Instance ==========
bot = BasicBot(API_KEY, API_SECRET)
bot.check_balance()

# ========== Step 5: Get Order Details from User ==========
try:
    symbol = input("🔹 Enter trading pair (e.g., BTCUSDT): ").strip().upper()
    side = input("🔹 Enter order side (BUY or SELL): ").strip().upper()
    order_type = input("🔹 Enter order type (MARKET or LIMIT): ").strip().upper()
    quantity = float(input("🔹 Enter quantity: "))

    price = None
    if order_type == "LIMIT":
        price = input("🔹 Enter limit price: ").strip()

    # ========== Step 6: Place the Order ==========
    bot.place_order(symbol, side, quantity, order_type, price)

except Exception as e:
    print("❌ Invalid input:", e)
    logging.error(f"Input error: {e}")

