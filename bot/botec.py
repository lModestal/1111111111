import telebot as tb
from telebot import types as tp
import tok
import parametr as pm
bot = tb.TeleBot(tok.tk)
kolvo = []

@bot.message_handler(commands=['start'])

def send_mes(message):
    kolvo.append(message.from_user.username)
    bot.send_message(message.chat.id, pm.welcome)
    klava(message)

@bot.message_handler(commands=['kolvo'])
def uchastniki(message):
    lol = len(set(kolvo))
    bot.send_message(message.chat.id, f'{pm.numbers} {lol}' )

def klava(message):
    klava = tp.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
    answ12 = tp.KeyboardButton(text=pm.registr)
    answ2 = tp.KeyboardButton(text='Расписание мероприятий')
    klava.add(answ2, answ12)
    bot.send_message(message.chat.id, '555', reply_markup=klava)
    bot.send_message(1756196334, message.from_user.username)

@bot.message_handler(func= lambda message: 'Регистрация' in message.text)
def spisok_registr(message):
    klava = tp.ReplyKeyboardMarkup(resize_keyboard= True, row_width= 2)
    answ1 = tp.KeyboardButton(text= pm.mp1)
    answ2 = tp.KeyboardButton(text=pm.mp2)
    answ3 = tp.KeyboardButton(text=pm.mp3)
    beck = tp.KeyboardButton(text=pm.back)
    klava.add(answ1, answ2, answ3, beck)
    bot.send_message(message.chat.id, pm.spisok, reply_markup=klava)

    @bot.message_handler(func= lambda message: message.text == pm.mp1)
    
    def registr(message):
        if message.text == pm.mp1:
            s = bot.send_message(message.chat.id, pm.dlya_registr )
            bot.register_next_step_handler(s, reg)

def reg(message):
    l =[] 
    l.append(message.text.split())
    bot.send_message(message.chat.id, pm.blagodar )
    print(l)



@bot.message_handler(func= lambda message: pm.back in message.text)
def back(message):
    bot.send_message(message.chat.id, pm.menyu)
    klava(message)
    	

bot.infinity_polling()
