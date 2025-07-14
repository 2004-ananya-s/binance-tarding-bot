from binance.client import Client
import logging

# ========== Step 1: Setup CSV-Style Logging ==========
logging.basicConfig(
    filename='bot.csv',
    level=logging.INFO,
    format='%(asctime)s,%(levelname)s,%(message)s'
)

# ========== Step 2: Create the Trading Bot Class ==========
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
        try:
            # Simulated order structure
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

        except Exception as e:
            print("❌ Error placing order:", e)
            logging.error(f"Order failed: {e}")

# ========== Step 3: Enter Your Binance API Keys ==========
API_KEY = "your_api_key"
API_SECRET = "your_sceret_key"

# ========== Step 4: Create Bot Instance ==========
bot = BasicBot(API_KEY, API_SECRET)
bot.check_balance()

# ========== Step 5: Get User Inputs and Place Order ==========
try:
    symbol = input("🔹 Enter trading pair (e.g., BTCUSDT): ").strip().upper()
    side = input("🔹 Enter order side (BUY or SELL): ").strip().upper()
    order_type = input("🔹 Enter order type (MARKET or LIMIT): ").strip().upper()
    quantity = float(input("🔹 Enter quantity: "))

    price = None
    if order_type == "LIMIT":
        price = input("🔹 Enter limit price: ").strip()

    bot.place_order(symbol, side, quantity, order_type, price)

except Exception as e:
    print("❌ Invalid input:", e)
    logging.error(f"Input error: {e}")

       


