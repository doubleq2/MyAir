from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton('О нас', callback_data='about_us'),
            InlineKeyboardButton('Контакты', callback_data='contacts'),
        ],
        [
            InlineKeyboardButton('Авторизация', callback_data='authorization'),
            InlineKeyboardButton('Регистрация', callback_data='registration'),
            InlineKeyboardButton('Мои билеты', callback_data='my_tickets'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        text=f'Привет! Я бот MyAir, который поможет тебе найти самый лучший вариант перелета. '
             'Выбери нужный тебе вариант ниже.',
        reply_markup=reply_markup
    )

async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton('Главное меню', callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.answer()
    await query.edit_message_text(
        text='Наши контакты: \n'
             'Телефон: +79999999999 \n'
             'Email: abobys@enc.ru \n'
             'Telegram: @vipkazakh002, @qq2y2',
        reply_markup=reply_markup
    )

async def about_us(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton('Главное меню', callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.answer()
    await query.edit_message_text(
        text='Мы команда, которая поможет вам найти лучший вариант перелета.',
        reply_markup=reply_markup
    )

async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    keyboard = [
        [
            InlineKeyboardButton('О нас', callback_data='about_us'),
            InlineKeyboardButton('Контакты', callback_data='contacts'),
        ],
        [
            InlineKeyboardButton('Авторизация', callback_data='authorization'),
            InlineKeyboardButton('Регистрация', callback_data='registration'),
            InlineKeyboardButton('Мои билеты', callback_data='my_tickets'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.answer()
    await query.edit_message_text(
        text=f'Привет! Я бот MyAir, который поможет тебе найти самый лучший вариант перелета. '
             'Выбери нужный тебе вариант ниже.',
        reply_markup=reply_markup
    )
