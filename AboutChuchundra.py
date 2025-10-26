import telebot


New_Bot = telebot.TeleBot("8201987153:AAGr_DRbzcLiGzsgTcOVP7ZkNI-5EgqxTo4", parse_mode=None)
Target_User_ID = 5684920523

@New_Bot.message_handler(commands=['start', 'help'])
def Start(message):
    New_Bot.send_message(message.chat.id, "=== список комманд ===\n\n/info - Слегка обо мне\n/print - Можете отправить мне сообщение\n/start и /help - Показывает это сообщение")

@New_Bot.message_handler(commands=['info'])
def info(message):
    New_Bot.send_message(message.chat.id, "Немного обо мне...\nЯ занимаюсь программированием, рисованием и люблю поиграть в игрушки :0\n\nGithub: TheChundraOffical\nusername: @Ow0ll\nname: 15CV\nOur Squad: t.me/SquadOfPseudoProgrammers")

@New_Bot.message_handler(commands=['print'])
def info(message):
    NewMessage = f"Message From: @{message.from_user.username}\n\n"
    NewMessage += message.text.replace('/print', '').strip()

    try:
        New_Bot.send_message(Target_User_ID, NewMessage)
        New_Bot.reply_to(message, "Сообщение отправленно!")
    except Exception as e:
        New_Bot.reply_to("Ошибка: Ошибка при отправке сообщения :(")


New_Bot.infinity_polling()

