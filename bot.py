import telebot
import math
from telebot import types

token = '<your token>'
bot = telebot.TeleBot(token)
num_1 = None
num_2 = None
num_3 = None

@bot.message_handler(commands = ['start'])
def start_message(message):
	sqr_on = 1
	markup_inline = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item_sqrt = types.KeyboardButton('Корень из числа')
	item_stepen = types.KeyboardButton('Возвести в степень')
	item_urav = types.KeyboardButton('Квадратное уравнение')
	markup_inline.add(item_sqrt, item_stepen, item_urav)
	bot.send_message(message.chat.id, "Это бот калькулятор, чтобы начать вычисления введите выражение. \n \n /sqrt  -  Корень из числа \n /stepen  -  Число в степень \n /kvadr  -  Квадратное уравнение \n /autor - Авторы", reply_markup = markup_inline)

@bot.message_handler(commands = ['sqrt'])
def sqrt(message) :
	msg_sqrt = bot.send_message(message.chat.id, "Введите число")
	bot.register_next_step_handler(msg_sqrt, sqrt_com)

@bot.message_handler(commands = ['stepen'])
def stepen(message):
	msg_stepen = bot.send_message(message.chat.id, "Введите число")
	bot.register_next_step_handler(msg_stepen, stepen_com)

@bot.message_handler(commands = ['autor'])
def autor(message):
	bot.send_message(message.chat.id, "Создатель и полноправный владелец сего программистического чуда - @risely")

@bot.message_handler(commands = ['kvadr'])
def kvadr_1(message):
	msg_kvadr = bot.send_message(message.chat.id, "Введите переменные уравнения ax^2 + bx + c = 0. \n\nПеременные вводятся по одному сообщению. Бот решает уравнения через дескриминант.")
	bot.register_next_step_handler(msg_kvadr, kvadr_1_num)

@bot.message_handler(content_types = ['text'])
def first_num(message):
	msg = None
	user_message = message.text.lower()
	if message.text.lower() == 'привет' : 
	 bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}! Чтобы начать пользоваться калькулятором, введи выражение")
	elif message.text.lower() == 'помощь' :
		bot.send_message(message.chat.id, "Все просто - введи выражение чтобы бот его вычислил")
	elif message.text == 'Корень из числа' :
		msg_sqrt = bot.send_message(message.chat.id, "Введите число")
		bot.register_next_step_handler(msg_sqrt, sqrt_com)
	elif message.text == 'Возвести в степень':
		msg_stepen = bot.send_message(message.chat.id, "Введите число")
		bot.register_next_step_handler(msg_stepen, stepen_com)
	elif message.text == 'Квадратное уравнение':
		bot.send_message(message.chat.id, "Чтобы решить квадратное уравнение, введите команду /kvadr")
	else:
		try:			
			answer = str(eval(user_message.replace(' ', '')))
			msg = bot.send_message(message.chat.id, user_message.replace(' ', '') + '=' + answer)
		except SyntaxError:
		    bot.send_message(message.chat.id, "SyntaxError")
		except NameError:
		 	bot.send_message(message.chat.id, "NameError")
		except TypeError:
		 	bot.send_message(message.chat.id, "TypeError")
		except ZeroDivisionError:
		 	bot.send_message(message.chat.id, "На ноль делить нельзя, хитрец)")
	print(sqr_on)

def sqrt_com(message) :
	num = message.text
	print(message.text)
	answer = math.sqrt(int(num))
	bot.send_message(message.chat.id, answer)

def stepen_com(message):
	num_stepen = int(message.text) * int(message.text)
	bot.send_message(message.chat.id, num_stepen)

def kvadr_1_num(message):
	global num_1
	num_1 = int(message.text.lower())
	kvadr_2_msg = bot.send_message(message.chat.id, "Введите вторую переменную")
	bot.register_next_step_handler(kvadr_2_msg, kvadr_2_num)
	print (num_1)

def kvadr_2_num(message):
	global num_2
	num_2 = int(message.text.lower())
	kvadr_3_msg = bot.send_message(message.chat.id, "Введите третью переменную")
	bot.register_next_step_handler(kvadr_3_msg, kvadr_3_num)
	print (num_1, num_2)

def kvadr_3_num(message):
	global num_3
	num_3 = int(message.text.lower())
	kvadr_message = bot.send_message(message.chat.id, "Напишите что-нибудь \n(костыль, потом поправлю)")
	bot.register_next_step_handler(kvadr_message, kvadr_final)

def kvadr_final(message):
	global num_1
	global num_2
	global num_3
	pre_D = (num_2 * num_2) - 4 * (num_1 * num_3)
	if int(pre_D) < 0:
		bot.send_message(message.chat.id, "Уравнение не имеет решений, так как дескриминант меньше 0")
	D = math.sqrt(int(pre_D))
	if D == 0:
		x1 = (0 - num_2)/2 * num_1
	elif D < 0:
		bot.send_message(message.chat.id, "Уравнение не имеет решений, так как дескриминант меньше 0")
	else:
		x1 = ((0 - num_2) - D)/2 * num_1

	if D > 0:
		x2 = ((0 - num_2) + D)/2 * num_1
	bot.send_message(message.chat.id, f"D = {D} \n X1 = {x1} \n X2 = {x2} ")


bot.infinity_polling()



