import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot crypto aktif 🚀")

async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        data = requests.get(url).json()
        price = data["bitcoin"]["usd"]

        await update.message.reply_text(f"Harga BTC sekarang: ${price}")

    except Exception as e:
        await update.message.reply_text("Gagal mengambil harga BTC")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("btc", btc))

print("Bot berjalan...")

app.run_polling()