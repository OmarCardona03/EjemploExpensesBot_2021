#########################################################
from config import bot
import config
from time import sleep
import re
import logic
import database.db as db
#########################################################

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
#########################################################

# Aquí vendrá la implementación de la lógica del bot 

# start
@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    bot.send_message(
    message.chat.id,
    "Hola, soy un \U0001F916, ¿cómo estás?",
    parse_mode="Markdown") 

# AYUDA
@bot.message_handler(commands=['help'])
def on_command_help(message):
    bot.send_chat_action(message.chat.id, 'typing')

    bot.send_message(
        message.chat.id,
        logic.get_about_this(config.VERSION), 
        parse_mode="Markdown")

#########################################################
@bot.message_handler(commands=['about'])
def on_command_about(message):
    bot.send_chat_action(message.chat.id, 'typing')

    bot.send_message(
        message.chat.id,
        logic.get_help_message(), 
        parse_mode="Markdown")

#########################################################
@bot.message_handler(regexp=r"^(gane|gané|g) ([+-]?([0-9]*[.])?[0-9]+)$")
def on_earn_money(message):
    pass

#########################################################
@bot.message_handler(regexp=r"^(gaste|gasté|gg) ([+-]?([0-9]*[.])?[0-9]+)$")
def on_spend_money(message):
    pass

#########################################################
@bot.message_handler(regexp=r"^(listar ganancias|lg) en ([0-9]{1,2}) de ([0-9]{4})$")
def on_list_earnings(message):
    pass

#########################################################
@bot.message_handler(regexp=r"^(listar gastos|lgg) en ([0-9]{1,2}) de ([0-9]{4})$")
def on_list_spendings(message):
    pass

#########################################################
@bot.message_handler(regexp=r"^(obtener saldo|s)$")
def on_get_balance(message):
    pass

#########################################################
@bot.message_handler(regexp=r"^(remover|r) (ganancia|g|gasto|gg) ([0-9]+)$")
def on_remove_record(message):
    pass


#########################################################
# Default cuando se ingresa un valor invalido:
@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    bot.reply_to(
    message,
    "\U0001F63F Ups, no entendí lo que me dijiste.")

#########################################################
if __name__ == '__main__':
    bot.polling(timeout=20)
#########################################################