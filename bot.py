from telegram.ext import Application, MessageHandler, filters

TOKEN = "8962022434:AAHKpYQ_CiqC_qwasBJC8iFKS71I1nmfRx4"
GROUP_ID = "-1004419121375"

async def send_to_group(update, context):
    if str(update.message.chat.id) == GROUP_ID:
        return
    await context.bot.send_message(chat_id=GROUP_ID, text=update.message.text)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_to_group))
app.run_polling()
print("✅ ربات روشن شد!")
