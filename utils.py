from telegram import ReplyKeyboardMarkup


def main_keyboard():
    return ReplyKeyboardMarkup(
        [['Гражданство/Виза'],
         ['Открытие счета'],
         ['Фин.консалтинг'],
         ['Документы']]
    )


def dialog_error(update, context):
    message = 'Прошу прощения, кажется, вы прислали что-то не то'
    update.message.reply_text(message)
