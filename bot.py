#########################################################
from config import bot
import config
from time import sleep
import re
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
    sleep(1)

    response = (
        "Estos son los comandos y órdenes disponibles:\n"
        "\n"
        "*/start* - Inicia la interacción con el bot\n"
        "*/help* - Muestra este mensaje de ayuda\n"
        "*sumar {valor1} y {valor2}* - Calcula la suma de dos valores\n"
        "*restar {valor1} y {valor2}* - Calcula la resta de dos valores\n"
        "*multiplicar {valor1} y {valor2}* - Calcula la multiplicación de dos valores\n"
        "*dividir {valor1} y {valor2}* - Calcula la división de dos valores\n"
    )
    bot.send_message(
    message.chat.id,
    response,
    parse_mode="Markdown") 

# SUMAR:
@bot.message_handler(regexp=r"^sumar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
def on_add(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    parts = re.match(
        r"^sumar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$",
    message.text,
    re.IGNORECASE)
    # print (parts.groups())
    oper1 = float(parts[1])
    oper2 = float(parts[3])
    result = oper1 + oper2
    bot.reply_to(
        message,
        f"\U0001F522 Resultado: {result}")

# Restar
@bot.message_handler(regexp=r"^restar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
def on_substract(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    parts = re.match(
        r"^restar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$",
    message.text,
    re.IGNORECASE)
    # print (parts.groups())
    oper1 = float(parts[1])
    oper2 = float(parts[3])
    result = oper1 - oper2
    bot.reply_to(
        message,
        f"\U0001F522 Resultado: {result}")

# Multiplicar
@bot.message_handler(regexp=r"^multiplicar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
def on_multiply(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    parts = re.match(
        r"^multiplicar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$",
    message.text,
    re.IGNORECASE)
    # print (parts.groups())  
    oper1 = float(parts[1])
    oper2 = float(parts[3])
    result = oper1 * oper2
    bot.reply_to(
        message,
        f"\U0001F522 Resultado: {result}")


#Dividir:
@bot.message_handler(regexp=r"^dividir ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
def on_divide(message):
    bot.send_chat_action(message.chat.id, 'typing')
    
    parts = re.match(
        r"^dividir ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$",
        message.text,
        re.IGNORECASE)
    # print (parts.groups())  
    oper1 = float(parts[1])
    oper2 = float(parts[3])

    if oper2 == 0:
        bot.reply_to(
            message,
            f"\U0000274C Imposible realizar la operación, el denominador no puede ser cero.")
        return
    result = oper1 / oper2
    bot.reply_to(
        message,
        f"\U0001F522 Resultado: {result}")
# Aqui


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