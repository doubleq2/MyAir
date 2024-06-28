import os
import logging
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, filters

from bot_messages import about_us, contacts, main_menu, start
from auth import CHOOSE_METHOD, FINISH, LOGIN, PASSWORD, auth_start, choose_method, finish, login, password


os.chdir(os.path.join(os.path.dirname(__file__), '../../../'))
print("Current working directory:", os.getcwd())
TELEGRAM_BOT_TOKEN = os.getenv('TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME')
print(TELEGRAM_BOT_TOKEN, BOT_USERNAME) 


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

if __name__ == '__main__':
    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(auth_start, pattern='authorization')],
        states={
            CHOOSE_METHOD: [CallbackQueryHandler(choose_method)],
            LOGIN: [MessageHandler(filters.TEXT & ~filters.COMMAND, login)],
            PASSWORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, password)],
            FINISH: [MessageHandler(filters.TEXT & ~filters.COMMAND, finish)]
        },
        fallbacks=[CallbackQueryHandler(main_menu, pattern='main_menu')],
    )
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(about_us, pattern='about_us'))
    app.add_handler(CallbackQueryHandler(main_menu, pattern='main_menu'))
    app.add_handler(CallbackQueryHandler(contacts, pattern='contacts'))
    app.add_handler(conv_handler)

    app.run_polling()
