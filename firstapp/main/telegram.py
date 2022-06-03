import telepot

token = '5239076080:AAFCncumYGACzTLXqVM_dJ2YfHLb2pr_A3E'
my_id = -1001607126850
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(my_id, text, parse_mode="Markdown")