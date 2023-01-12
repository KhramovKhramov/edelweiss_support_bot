from utils import main_keyboard


def greet_user(update, context):
    user = update.effective_user
    message = f'Здравствуйте, <b>{user.first_name}</b>! Благодарим Вас за обращение в <b>Edelweiss Consulting</b>. Пока наш менеджер обрабатывает Вашу заявку, уточните, пожалуйста, какая именно услуга Вас интересует:'
    update.message.reply_text(
        message,
        parse_mode='html',
        reply_markup=main_keyboard())
