import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
import asyncio
import threading

# Récupérer le token depuis les variables d'environnement
TOKEN = os.getenv('TELEGRAM_TOKEN', "8380142036:AAECByAZfHCR4tbnCsFMDIlpGWjvCUo2x14")

# Créer l'application Flask pour Render
app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Commande /start reçue de {update.effective_user.id}")
    await update.message.reply_text("Salut ! Je suis le bot de Fredy, ravi de te rencontrer ! 😊")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Commande /help reçue de {update.effective_user.id}")
    await update.message.reply_text("Voici les commandes disponibles:\n/start - Démarrer le bot\n/help - Afficher l'aide\n/cc - Dire cc lm")

async def cc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Commande /cc reçue de {update.effective_user.id}")
    await update.message.reply_text("cc lm ! 👋")

@app.route('/')
def home():
    return "Bot Telegram Fredy - Fonctionne parfaitement sur Render ! 🚀"

@app.route('/health')
def health():
    return "Bot en ligne ! ✅"

def run_bot():
    """Fonction pour démarrer le bot"""
    print("🚀 Démarrage du bot Telegram...")
    
    async def bot_main():
        try:
            # Créer l'application Telegram
            application = Application.builder().token(TOKEN).build()
            
            # Ajouter les handlers
            application.add_handler(CommandHandler("start", start))
            application.add_handler(CommandHandler("help", help_command))
            application.add_handler(CommandHandler("cc", cc_command))
            
            print("✅ Bot configuré avec succès")
            print("🔄 Démarrage du polling...")
            
            # Démarrer le bot
            await application.run_polling(allowed_updates=Update.ALL_TYPES)
            
        except Exception as e:
            print(f"❌ Erreur lors du démarrage du bot: {e}")
    
    # Démarrer le bot avec asyncio
    asyncio.run(bot_main())

if __name__ == '__main__':
    print("🎯 Démarrage de l'application...")
    
    # Démarrer le bot dans un thread séparé
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    print("🌐 Démarrage du serveur Flask...")
    
    # Démarrer Flask pour Render
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False) 
