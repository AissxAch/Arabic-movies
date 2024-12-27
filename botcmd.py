from info import *
from telebot import types

def myCmd(m):
    if m.text == '/start':
        bot.reply_to(m,"Hi, "+str(m.from_user.first_name))
        bot.send_message(m.chat.id," هذا البوت مخصص للبحث عن الأفلام فقط و ليس المسلسلات \n اكتب اسم الفيلم الذي تريد البحث عنه\n ان كنت تستخدم الحاسوب نزل هذه الاضافة لمنع الاعلانات \nhttps://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm")