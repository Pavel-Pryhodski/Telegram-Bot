import os

global name_file


def create_team(message):
	global name_file
	name_file = 'Команды/' + message.text + '_' + str(message.from_user.id) + '.team'
	file = open(name_file, 'w')
	file.write('НАЗВАНИЕ КОМАНДЫ:      ' + message.text + '\n\n' +
			   'СОСТАВ КОМАНДЫ:' + '\n')
	file.close()


def add_members(message):
	global name_file
	file_members = open(name_file, 'a')
	file_members.write(message.text + '\n')
	file_members.close()


def find_my_teams(call):
	list_my_teams = []
	for file in os.listdir('Команды'):
		if file.split('_')[1] == (str(call.message.chat.id) + '.team'):
			list_my_teams.append(file.split('_')[0])
	return list_my_teams


def members_team(call):
	list_team_members = []
	for file in os.listdir('Команды'):
		if file.split('_')[1] == (str(call.message.chat.id) + '.team'):
			f = open('Команды/' + file, 'r')
			text_file = f.read()
			text_file = text_file.split('\n')
			for line, obj in enumerate(text_file):
				if line > 2:
					list_team_members.append(obj)
			f.close()
	print(list_team_members)
	return list_team_members


