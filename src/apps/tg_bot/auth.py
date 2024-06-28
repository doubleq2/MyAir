from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, ConversationHandler

# Определение состояний разговора
CHOOSE_METHOD, LOGIN, PASSWORD, FINISH = range(4)

async def auth_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton('Авторизоваться через логин и пароль', callback_data='login_password')],
        [InlineKeyboardButton('Главное меню', callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.answer()
    await query.edit_message_text(text='Выберите способ авторизации:', reply_markup=reply_markup)
    return CHOOSE_METHOD

async def choose_method(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if query.data == 'login_password':
        await query.edit_message_text('Вы выбрали авторизацию через логин и пароль. Введите ваш логин:')
        return LOGIN
    else:
        await query.edit_message_text('Выберите способ авторизации')
        return CHOOSE_METHOD

async def login(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['login'] = update.message.text
    await update.message.reply_text('Введите ваш пароль:')
    return PASSWORD

async def password(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['password'] = update.message.text
    await update.message.reply_text('Авторизация успешно завершена!')
    return FINISH

async def finish(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Вы вернулись в главное меню.')
    return ConversationHandler.END
