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
        data = requests.get(url).json()
        price = data["price"]

        await update.message.reply_text("Harga BTC: $" + price)

    except:
        await update.message.reply_text("Gagal mengambil harga BTC")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("btc", btc))

print("Bot berjalan...")

app.run_polling()