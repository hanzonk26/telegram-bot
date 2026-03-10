import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8545465161:AAHiROdY6iVQNcttKAm0pJ2V9YHjjUc9dp4"
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

async def eth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        import aiohttp

        url = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:

                data = await resp.json()
                price = data.get("price")

                await update.message.reply_text(f"Harga ETH sekarang: ${price}")

    except Exception as e:
        print("ERROR API:", e)
        await update.message.reply_text("Gagal mengambil harga ETH")     

async def top(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        import requests

        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"

        data = requests.get(url).json()

        text = "Top 10 Crypto Market:\n\n"

        for coin in data:
            text += f"{coin['name']} : ${coin['current_price']}\n"

        await update.message.reply_text(text)

    except Exception as e:
        print(e)
        await update.message.reply_text("Gagal mengambil data market")

async def fear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        import requests

        url = "https://api.alternative.me/fng/"
        data = requests.get(url).json()

        value = data["data"][0]["value"]
        status = data["data"][0]["value_classification"]

        await update.message.reply_text(
            f"Fear & Greed Index\n\nScore : {value}\nStatus : {status}"
        )

    except Exception as e:
        print(e)
        await update.message.reply_text("Gagal mengambil data sentiment")



app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("btc", btc))
app.add_handler(CommandHandler("eth", eth))
app.add_handler(CommandHandler("top", top))
app.add_handler(CommandHandler("fear", fear))
print("Bot berjalan...")

app.run_polling()
