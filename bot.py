from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = 8964906050:AAFdIOH0yQ1HC_xMUT8AcIfjcHJKZh5GTFM
	
WELCOME = """
⚽ Bienvenue sur 1XBET FIFA BOT ⚽

🎮 Pronostics FIFA
📊 Analyse des matchs
🔥 Matchs fiables du jour
💰 Tickets VIP

Choisis une option :

1️⃣ Match du jour
2️⃣ Ticket VIP
3️⃣ Résultats
4️⃣ Support
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "1":
        await update.message.reply_text(
            "🔥 MATCH FIFA DISPONIBLE 🔥\n\n"
            "✅ Over 1.5\n"
            "✅ BTTS\n"
            "✅ But en première mi-temps"
        )

    elif text == "2":
        await update.message.reply_text(
            "💰 ACCÈS VIP DISPONIBLE\n\n"
            "📩 Contacte l’admin WhatsApp"
        )

    elif text == "3":
        await update.message.reply_text(
            "✅ Résultats gagnants publiés aujourd’hui"
        )

    elif text == "4":
        await update.message.reply_text(
            "📲 Support disponible 24h/24"
        )

    else:
        await update.message.reply_text(
            "❌ Option invalide.\n\nEnvoie : 1, 2, 3 ou 4."
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("Bot lancé...")
    app.run_polling()

if __name__ == "__main__":
    main()
