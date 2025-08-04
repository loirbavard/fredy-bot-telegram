import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import sys
import os
import time
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8380142036:AAECByAZfHCR4tbnCsFMDIlpGWjvCUo2x14"

class TelegramBotService(win32serviceutil.ServiceFramework):
    _svc_name_ = "TelegramBotService"
    _svc_display_name_ = "Telegram Bot Service"
    _svc_description_ = "Service pour le bot Telegram Fredy"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.bot_thread = None

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        self.bot_thread = threading.Thread(target=self.run_bot)
        self.bot_thread.start()
        win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)

    def run_bot(self):
        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
            await update.message.reply_text("Salut ! Ton bot fonctionne parfaitement 🚀")

        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        
        try:
            app.run_polling()
        except Exception as e:
            print(f"Erreur dans le bot: {e}")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(TelegramBotService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(TelegramBotService) 