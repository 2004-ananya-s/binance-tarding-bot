# Binance Futures Testnet Trading Bot (Simulation)

This is a simple Python trading bot built for the Binance **Futures Testnet**. It accepts user input from the terminal and simulates placing MARKET or LIMIT orders.

Due to API instability in the Testnet (error code -2015), this version simulates order placement instead of using the real API call. All logic and structure are implemented as if placing a real trade.

---

## ✅ Features

- Connects to Binance Futures Testnet
- Checks USDT balance
- Accepts CLI input for:
  - Trading pair
  - Order side (BUY/SELL)
  - Order type (MARKET/LIMIT)
  - Quantity
  - Price (if LIMIT order)
- Simulates successful order placement
- Logs order details using Python logging

---

## 🚀 How to Run

### 1. Install requirements:
```bash
pip install python-binance
### 2. Run the Script:
```bash
python trading_bot.py
### 3. Follow the prompts:
```scss
Enter trading pair (e.g., BTCUSDT)
Enter order side (BUY or SELL)
Enter order type (MARKET or LIMIT)
Enter quantity
