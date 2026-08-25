# bot_telegram.py
# Conector: traduce entre Telegram y el cerebro del bot.

import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

from cerebro import responder

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")


async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Recibe un mensaje de Telegram y contesta con lo que diga el cerebro."""
    entrada = update.message.text
    usuario = update.message.from_user.first_name

    texto, tema = responder(entrada)
    await update.message.reply_text(texto)

    if tema == "desconocido":
        print(f"[AVISO] {usuario} preguntó: {entrada}")


if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

    print("Bot corriendo. Ctrl+C para detener.")
    app.run_polling()