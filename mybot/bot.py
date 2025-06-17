from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ضع التوكن الحقيقي مكان هذا التوكن التجريبي
TOKEN = "8097000772:AAFE99wBU-gf-7TLdOrZHJkliHwirSZUkJA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("المرحلة الأولى", callback_data='first')],
        [InlineKeyboardButton("المرحلة الثانية", callback_data='second')],
        [InlineKeyboardButton("المرحلة الثالثة", callback_data='third')],
        [InlineKeyboardButton("المرحلة الرابعة", callback_data='fourth')],
        [InlineKeyboardButton("المرحلة الخامسة", callback_data='fifth')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = "اهلا وسهلا بك في مكتبة هندسة البيئة الرقمية\nرضوان عبدالهادي"
    await update.message.reply_text(message, reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'first':
        await query.message.reply_document("https://t.me/env_mousl/398")
    elif query.data == 'second':
        await query.message.reply_text("سيتم إضافة ملفات المرحلة الثانية قريباً.")
    elif query.data == 'third':
        await query.message.reply_text("سيتم إضافة ملفات المرحلة الثالثة قريباً.")
    elif query.data == 'fourth':
        await query.message.reply_text("سيتم إضافة ملفات المرحلة الرابعة قريباً.")
    elif query.data == 'fifth':
        await query.message.reply_text("سيتم إضافة ملفات المرحلة الخامسة قريباً.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling(poll_interval=0.3, timeout=5)

if __name__ == '__main__':
    main()
