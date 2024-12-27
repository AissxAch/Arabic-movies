from info import *
from reply import *
from botcmd import *

@bot.message_handler(commands=['start'])
def cmd(m):
        myCmd(m)
@bot.message_handler(func=lambda m: True)
def rm(m):
        reply_mg(m)


bot.infinity_polling()