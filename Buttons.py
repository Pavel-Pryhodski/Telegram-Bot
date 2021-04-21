from telebot import types


keyboard_step1 = types.InlineKeyboardMarkup()
btn_1 = types.InlineKeyboardButton(text='Регистрация новой команды', callback_data='btn_1')
btn_2 = types.InlineKeyboardButton(text='Помощь', callback_data='btn_2')
btn_7 = types.InlineKeyboardButton(text='Просмотреть мною созданные команды', callback_data='btn_7')
keyboard_step1.add(btn_1).add(btn_7).add(btn_2)

keyboard_step7_1 = types.InlineKeyboardMarkup()
def create_btn_teams(team):
    if len(team) == 0:
        btn = types.InlineKeyboardButton(text='У Вас 0 команд ;-(   ...... НАЖМИТЕ НА КНОПКУ НИЖЕ',
                                         callback_data='0000000000000')
        keyboard_step7_1.add(btn).add(btn_1).add(btn_7).add(btn_2)
    else:
        for i in team:
            btn = types.InlineKeyboardButton(text=i.upper(), callback_data='btn_7_1_' + str(i))
            keyboard_step7_1.add(btn)


keyboard_step2 = types.InlineKeyboardMarkup()
btn_3 = types.InlineKeyboardButton(text='Подтверждаю название', callback_data='btn_3')
keyboard_step2.add(btn_3)

keyboard_step3 = types.InlineKeyboardMarkup()
btn_4 = types.InlineKeyboardButton(text='Утверждаю спортсмена', callback_data='btn_4')
keyboard_step3.add(btn_4)

keyboard_step4 = types.InlineKeyboardMarkup()
btn_5 = types.InlineKeyboardButton(text='Добавить следуещего спортсмена', callback_data='btn_5')
btn_6 = types.InlineKeyboardButton(text='Завершить заполнение команды', callback_data='btn_6')
keyboard_step4.add(btn_5).add(btn_6)

keyboard_step5 = types.InlineKeyboardMarkup()
keyboard_step5.add(btn_1).add(btn_7)

