import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask

# Récupérer le token depuis les variables d'environnement
TOKEN = os.getenv('TELEGRAM_TOKEN', "8380142036:AAECByAZfHCR4tbnCsFMDIlpGWjvCUo2x14")

# Créer l'application Flask pour Render
app = Flask(__name__)

# Créer l'application Telegram
telegram_app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut ! Je suis le bot de Fredy, ravi de te rencontrer ! 😊")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Voici les commandes disponibles:\n/start - Démarrer le bot\n/help - Afficher l'aide\n/cc - Dire cc lm")

async def cc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("cc lm ! 👋")

# Ajouter les handlers
telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("help", help_command))
telegram_app.add_handler(CommandHandler("cc", cc_command))

@app.route('/')
def home():
    return "Bot Telegram Fredy - Fonctionne parfaitement sur Render ! 🚀"

def run_bot():
    """Fonction pour démarrer le bot en arrière-plan"""
    print("Bot démarré sur Render...")
    telegram_app.run_polling()

if __name__ == '__main__':
    # Démarrer le bot dans un thread séparé
    import threading
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Démarrer Flask pour Render
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port) 