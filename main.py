

import telegram.ext

with open('token.txt', 'r') as f:
    TOKEN=f.read()

def start(update, context):
    update.message.reply_text("Hello! Welcome ")

def help(update, context):
    update.message.reply_text("""
    سلام  به همه این ربات تک استایل هست 
    راهنمای شما در خرید
    
    """)

def content(update , context):
    update.message.reply_text("takk styli sho!!")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))

updater.start_polling()
updater.idle()