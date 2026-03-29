from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from parser import parse_with_gemma
from data import get_ohlcv
from analysis import find_levels
from chart import generate_chart
from formatter import format_output

import os
import asyncio

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not update.message or not update.message.text:
            return

        user_text = update.message.text

        parsed = await asyncio.to_thread(parse_with_gemma, user_text)

        symbol = parsed["symbol"]
        timeframes = parsed["timeframes"]

        for tf in timeframes:
            df = await asyncio.to_thread(get_ohlcv, symbol, tf)

            supports, resistances = await asyncio.to_thread(find_levels, df)

            chart_path = await asyncio.to_thread(
                generate_chart, df, supports, resistances, symbol, tf
            )

            text = format_output(symbol, tf, supports, resistances)

            with open(chart_path, 'rb') as img:
                await update.message.reply_photo(photo=img, caption=text)

    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")


app.add_handler(MessageHandler(filters.TEXT, handle))
