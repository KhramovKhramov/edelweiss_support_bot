import logging

from telegram.ext import CommandHandler, Updater

import settings
from dialogs.dialogs_handlers import (dialog_account, dialog_consulting,
                                      dialog_documents, dialog_visa,
                                      send_messages)
from handlers import greet_user

logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    mybot = Updater(settings.API_KEY)
    dp = mybot.dispatcher

    dp.add_handler(dialog_visa)
    dp.add_handler(dialog_consulting)
    dp.add_handler(dialog_documents)
    dp.add_handler(dialog_account)
    dp.add_handler(send_messages)
    dp.add_handler(CommandHandler("start", greet_user))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
