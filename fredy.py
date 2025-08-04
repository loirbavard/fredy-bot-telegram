from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8380142036:AAECByAZfHCR4tbnCsFMDIlpGWjvCUo2x14"  # Mets ton token ici

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut ! Ton bot fonctionne parfaitement 🚀")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in AUTHORIZED_USERS:
        await update.message.reply_text("Tu n'es pas autorisé à utiliser ce bot.")
        return
    await update.message.reply_text("Bienvenue !")
