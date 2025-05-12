from time import sleep
from info import *
from search import *


def reply_mg(m):
    list = search1(m.text.strip())
    for poster in list['posters']:
        keyboard = types.InlineKeyboardMarkup()
        i = 1
        for poster in list['posters']:
            n = poster['title']
            idd = poster['id']
            title = poster['title']
            # Ensure callback_data is within the 64-byte limit
            callback_data = f'{idd};{title}'
            btn = types.InlineKeyboardButton(f'[{i}] [ Name : {n} ] [ ID : {idd} ]', callback_data=callback_data)
            i += 1
            keyboard.add(btn)
    try:
        bot.send_message(m.chat.id, 'اختر الفيلم الذي تريده', reply_markup=keyboard)
    except:
        bot.send_message(m.chat.id, 'لم يتم العثور على الفيلم الذي تبحث عنه🚫')

    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        idd = call.data.split(';')[0]
        title = call.data.split(';')[1]
        list = search1(title)
        i=1
        for poster in list['posters']:
            idd = int(idd)
            if poster["id"] == idd:
                bot.send_message(call.message.chat.id, f'الاسم : {title}\nالوصف : {poster["description"]} \n التصنيف : {poster["classification"]} \n السنة : {poster["year"]} \n التقييم : {poster["rating"]}/5 \n الوقت : {poster["duration"]}')
                image_url = poster["image"]
                bot.send_photo(call.message.chat.id, image_url)
                break
        list2 = search2(idd)
        size=len(list2)
        if list2 == []:
            bot.send_message(call.message.chat.id, 'لم يتم العثور على الروابط او قمت بإختيار مسلسل و ليس فيلم🚫')
            return
        else:
            bot.send_message(call.message.chat.id, 'تم العثور على الروابط التالية✔')
        for l in list2:
                bot.send_message(call.message.chat.id, f'[{i}] Link : {l["url"]}')
                i+=1
                if i == 6:
                    break
                    
