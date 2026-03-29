from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from parser import parse_with_gemma
from data import get_ohlcv
from analysis import find_levels
from chart import generate_chart
from formatter import format_output

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

app = ApplicationBuilder().token(TOKEN).build()

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_text = update.message.text

        parsed = parse_with_gemma(user_text)

        symbol = parsed["symbol"]
        timeframes = parsed["timeframes"]

        for tf in timeframes:
            df = get_ohlcv(symbol, tf)

            supports, resistances = find_levels(df)

            chart_path = generate_chart(df, supports, resistances, symbol, tf)

            text = format_output(symbol, tf, supports, resistances)

            await update.message.reply_photo(photo=open(chart_path, 'rb'), caption=text)

    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

app.add_handler(MessageHandler(filters.TEXT, handle))
