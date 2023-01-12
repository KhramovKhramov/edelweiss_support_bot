from telegram.ext import ConversationHandler, Filters, MessageHandler

from dialogs.account import account_comment, account_finish, account_start
from dialogs.consulting import (consulting_comment, consulting_contacts,
                                consulting_ending, consulting_start)
from dialogs.documents import (documents_comment, documents_contacts,
                               documents_ending, documents_start)
from dialogs.send_messages import get_chat_id, get_text_message, send_message
from dialogs.visa import (next_service_citizenship, next_service_emirates_id,
                          next_service_visa, visa_comment, visa_contacts,
                          visa_ending, visa_start)
from utils import dialog_error

dialog_visa = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex(
            '^(Гражданство/Виза)$'), visa_start)],
        states={'next_service': [
            MessageHandler(Filters.regex('^(Гражданство)$'),
                           next_service_citizenship),
            MessageHandler(Filters.regex('^(Виза)$'), next_service_visa),
            MessageHandler(Filters.regex('^(Emirates ID)$'),
                           next_service_emirates_id)
        ],
            'visa_contacts': [MessageHandler(Filters.regex(
                            '^(ЕС|Израиль|Киргизия|Мексика|Карта АТЭС|Виза)$'),
                                             visa_contacts)],
            'visa_comment': [MessageHandler(Filters.text, visa_comment)],
            'visa_finish': [MessageHandler(Filters.text, visa_ending)]},
        fallbacks=[MessageHandler(Filters.video |
                   Filters.photo | Filters.document |
                   Filters.location | Filters.attachment, dialog_error)]
    )

dialog_consulting = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex(
            '^(Фин.консалтинг)$'), consulting_start)],
        states={'contacts': [MessageHandler(Filters.regex(
            '^(ОАЭ|Сингапур|Гонконг|Швейцария)$'),
                                            consulting_contacts)],
                'comment': [MessageHandler(Filters.text, consulting_comment)],
                'ending': [MessageHandler(Filters.text, consulting_ending)]},
        fallbacks=[MessageHandler(Filters.video |
                   Filters.photo | Filters.document |
                   Filters.location | Filters.attachment, dialog_error)]
    )

dialog_documents = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex(
            '^(Документы)$'), documents_start)],
        states={'doc_contacts': [MessageHandler(Filters.regex(
            '^(Замена паспорта РФ|Замена загранпаспорта)$'),
            documents_contacts)],
                'doc_comment': [MessageHandler(Filters.text,
                                               documents_comment)],
                'doc_ending': [MessageHandler(Filters.text,
                                              documents_ending)]},
        fallbacks=[MessageHandler(Filters.video |
                   Filters.photo | Filters.document |
                   Filters.location | Filters.attachment, dialog_error)]
    )

dialog_account = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex(
        '^(Открытие счета)$'), account_start)],
    states={'account_comment': [MessageHandler(Filters.text, account_comment)],
            'account_finish': [MessageHandler(Filters.text, account_finish)]},
    fallbacks=[MessageHandler(Filters.video | Filters.photo |
                              Filters.document | Filters.location |
                              Filters.attachment, dialog_error)]
    )

send_messages = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex(
            '^(Осьминог|осьминог)$'), get_chat_id)],
        states={'text': [MessageHandler(Filters.text, get_text_message)],
                'message': [MessageHandler(Filters.text, send_message)]},
        fallbacks=[MessageHandler(Filters.text | Filters.video |
                   Filters.photo | Filters.document |
                   Filters.location | Filters.attachment, dialog_error)]
        )
