import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot crypto aktif 🚀")

async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        import aiohttp

        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:

                if resp.status != 200:
                    await update.message.reply_text("API Binance error")
                    return

                data = await resp.json()

        price = data.get("price")

        if not price:
            await update.message.reply_text("Data harga tidak ditemukan")
            return

        await update.message.reply_text(f"Harga BTC sekarang: ${price}")

    except Exception as e:
        print("ERROR API:", e)
        await update.message.reply_text("Gagal mengambil harga BTC")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("btc", btc))

print("Bot berjalan...")

app.run_polling()