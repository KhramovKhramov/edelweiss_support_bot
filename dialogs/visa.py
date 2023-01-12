from telegram import ReplyKeyboardMarkup
from telegram.error import BadRequest
from telegram.ext import ConversationHandler

import settings
from utils import main_keyboard


def visa_start(update, context):
    context.user_data['dialog'] = {'service': update.message.text}
    reply_keyboard = [['Гражданство'], ['Виза'], ['Emirates ID']]
    update.message.reply_text(
        'Пожалуйста, выберите услугу:',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True)
    )

    return 'next_service'


def next_service_citizenship(update, context):
    context.user_data['dialog']['second_service'] = update.message.text
    reply_keyboard = [['ЕС'], ['Израиль'], ['Киргизия'], ['Мексика']]
    update.message.reply_text(
        'Пожалуйста, выберите территорию:',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True)
    )

    return 'visa_contacts'


def next_service_visa(update, context):
    context.user_data['dialog']['second_service'] = update.message.text
    reply_keyboard = [['Карта АТЭС'], ['Виза']]
    update.message.reply_text(
        'Пожалуйста, выберите услугу:',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True)
    )

    return 'visa_contacts'


def visa_contacts(update, context):
    context.user_data['dialog']['third_service'] = update.message.text
    message = 'Пожалуйста, оставьте нам свои контакты, чтобы мы могли с Вами связаться. Номер телефона либо никнейм Telegram в формате @nickname:'
    update.message.reply_text(
        message
    )

    return 'visa_comment'


def next_service_emirates_id(update, context):
    context.user_data['dialog']['second_service'] = update.message.text
    message = 'Пожалуйста, оставьте нам свои контакты, чтобы мы могли с Вами связаться. Номер телефона либо никнейм Telegram в формате @nickname:'
    update.message.reply_text(
        message
    )

    return 'visa_comment'


def visa_comment(update, context):
    context.user_data['dialog']['contacts'] = update.message.text
    reply_keyboard = [['Комментария нет']]
    message = 'Мы можем помочь Вам чем-то еще? Напишите, что бы Вы хотели добавить или нажмите на «Комментария нет»'
    update.message.reply_text(
        message,
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True)
    )

    return 'visa_finish'


def visa_ending(update, context):
    context.user_data['dialog']['comment'] = update.message.text
    user = update.effective_user
    second_service = context.user_data['dialog']['second_service']
    if second_service == 'Emirates ID':
        message = (
            f'<b>Новый запрос от @{user.username}</b>\n'
            '\n'
            f'<b>Имя пользователя</b>: {user.first_name} {user.last_name}\n'
            f'<b>ID чата</b>: <code>{update.message.chat.id}</code>\n'
            f'<b>Услуга</b>: {context.user_data["dialog"]["service"]}\n'
            f'<b>Подвид услуги</b>: {context.user_data["dialog"]["second_service"]}\n'
            f'<b>Контакты</b>: {context.user_data["dialog"]["contacts"]}\n'
            f'<b>Комментарий</b>: {context.user_data["dialog"]["comment"]}\n'
        )
    else:
        message = (
            f'<b>Новый запрос от @{user.username}</b>\n'
            '\n'
            f'<b>Имя пользователя</b>: {user.first_name} {user.last_name}\n'
            f'<b>ID чата</b>: <code>{update.message.chat.id}</code>\n'
            f'<b>Услуга</b>: {context.user_data["dialog"]["service"]}\n'
            f'<b>Подвид услуги</b>: {context.user_data["dialog"]["second_service"]}; {context.user_data["dialog"]["third_service"]}\n'
            f'<b>Контакты</b>: {context.user_data["dialog"]["contacts"]}\n'
            f'<b>Комментарий</b>: {context.user_data["dialog"]["comment"]}\n'
        )
    try:
        context.bot.send_message(chat_id=int(settings.GROUP_ID),
                                 text=message,
                                 parse_mode='html')

        update.message.reply_text('Спасибо, скоро мы свяжемся с вами!',
                                  reply_markup=main_keyboard())

        return ConversationHandler.END

    except (BadRequest, ValueError):
        update.message.reply_text('Спасибо, скоро мы свяжемся с вами!',
                                  reply_markup=main_keyboard())

    return ConversationHandler.END
