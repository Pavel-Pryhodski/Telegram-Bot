from telebot import TeleBot, types

import Addition, Buttons

file = open('TOKEN.txt', 'r')
token = file.read()
bot = TeleBot(token)
done = None


@bot.message_handler(commands=['start'])
def start_messages(message):

	first_name = message.from_user.first_name
	if first_name != None:
		first_name = ', ' + first_name + '!'
	else:
		first_name = '!'
	bot.send_message(message.chat.id, 'Добро пожаловать' + first_name + ' Выберите ваши дальнейшие действия',
					 reply_markup=Buttons.keyboard_step1)


# /help
@bot.message_handler(commands=['help'])
def help_message(message):
	bot.send_message(message.from_user.id, 'Создатель бота ППП. Спасибо')


@bot.message_handler(content_types=['text'])
def get_text(message):
	global done, msg
	if done == 'btn_1':
		msg = message
	elif done == 'btn_3' or 'btn_5':
		msg = message


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
	global done, msg
	done = call.data
	if call.data == 'btn_1':
		answer = 'Начнем регистрацию команды с ввода названия. Наберите имя команды и, ' \
				 'когда будете уверены, подтвердите нажатием на кнопку'
		bot.send_message(call.message.chat.id, answer, reply_markup=Buttons.keyboard_step2)

	elif call.data == 'btn_2':
		answer = 'Получите помощь :-)'
		bot.send_message(call.message.chat.id, answer, reply_markup=Buttons.keyboard_step1)

	elif call.data == 'btn_7':
		answer = 'Вы зарегестрировали вот эти команды. Выберите одну из команд, чтобы увидеть состав этой команды'
		Buttons.create_btn_teams(Addition.find_my_teams(call))
		bot.send_message(call.message.chat.id, answer, reply_markup=Buttons.keyboard_step7_1)
		Buttons.keyboard_step7_1 = types.InlineKeyboardMarkup()

	elif call.data == 'btn_3':
		Addition.create_team(msg)
		answer = 'Название команды подтверждено. Приступим к наполнению команды спорстменами. ' \
				 'Введите ФИО и дату рождения в формате дд.мм.гггг ' \
				 'Дальше подтвердите нажатием на кнопку "Утверждаю спортсмена"'
		bot.send_message(call.message.chat.id, answer, reply_markup=Buttons.keyboard_step3)

	elif call.data == 'btn_4':
		Addition.add_members(msg)
		answer = 'Что будем делать дальше?'
		bot.send_message(call.message.chat.id, answer, reply_markup=Buttons.keyboard_step4)

	elif call.data == 'btn_5':
		answer = 'Введите ФИО и дату рождения в формате дд.мм.гггг ' \
				 'Дальше подтвердите нажатием на кнопку "Утверждаю спортсмена"'
		bot.send_message(call.message.chat.id, answer, reply_markup=Buttons.keyboard_step3)

	elif call.data == 'btn_6':
		Addition.members_team(msg)
		answer = 'Что дальше?'
		bot.send_message(call.message.chat.id, answer, reply_markup=Buttons.keyboard_step5)

	elif call.data.startswith('btn_7_1_'):
		Addition.members_team(call)










if __name__ == '__main__':
	bot.polling()
