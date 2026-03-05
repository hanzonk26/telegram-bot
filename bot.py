import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8545465161:AAGcrHJovwyPQ4f_aFCifE_tdV9ErAjmikU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot trading aktif 🚀")

async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        data = requests.get(url).json()
        price = data["price"]
        await update.message.reply_text(f"Harga BTC sekarang: ${price}")
    except:
        await update.message.reply_text("Gagal mengambil harga BTC")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("btc", btc))

print("Bot berjalan...")

app.run_polling()
