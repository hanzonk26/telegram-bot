import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot aktif 🚀")

async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        price = data["price"]

        await update.message.reply_text(f"Harga BTC sekarang: ${price}")

    except Exception as e:
        print(e)
        await update.message.reply_text("API harga BTC error")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("btc", btc))

print("Bot berjalan...")

app.run_polling()