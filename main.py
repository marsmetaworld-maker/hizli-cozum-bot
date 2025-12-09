import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "👋 Merhaba, ben Hızlı Çözüm Botu\n\n"
        "📘 PDF – fotoğraf – ekran görüntüsü gönderebilirsin.\n"
        "✅ İlk 1 görsel ÜCRETSİZ\n"
        "✅ KPSS – LGS – Ehliyet – TYT – AYT\n\n"
        "📤 Şimdi dosyanı gönder."
    )
    await update.message.reply_text(msg)

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Ücretsiz deneme alındı.\n\n"
        "📄 Dosyanın tamamı için ücret: 30 TL\n"
        "💳 Ödeme: IBAN / Papara\n\n"
        "Ödemeden sonra tüm çözüm gönderilir."
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO, handle_file))

app.run_polling()
