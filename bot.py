from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8825952597:AAG5N_b480jbQYLRP20kJ5gGVBwefTfcDsk"
APP_URL = "https://cyber-ali001.github.io/MoneyPlus"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🚀💲 Start Earning Now", url=APP_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome to MoneyPlu$ 💰\n\n"
        "The first and easiest money earning app inside Telegram!\n\n"
        "💰 Earning Ways:\n"
        "✅ Watch Ads = $0.20\n"
        "✅ Invite a Friend = $0.40\n"
        "✅ Complete Tasks = $0.05\n\n"
        "💳 Payment Methods:\n"
        "Crypto • PayPal • Mobile Topup\n\n"
        "🚀 Launch the app and earn your first money now! 👇",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
