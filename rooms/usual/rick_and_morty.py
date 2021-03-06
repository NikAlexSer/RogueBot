import random
from constants import *

READY = 'Подойти ближе'
ESCAPE = 'Уйти'
HELLO = 'Поздороваться'
FIGHT = 'Атаковать'

name = 'Портал'

def enter(user, reply):
	msg = (
		'Какой-то зеленый портал, похожий на воронку, находящийся прямо на стене.\n'
		'Рядом лежит пустая бутылка из-под виски. Наверное, какая-то фигня.'
	)
	reply(msg)
	user.set_room_temp('question', 'first')

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == READY:
			reply('Ты подошел ближе, и к тебе вышли:\nКакой-то мужик в халате и с синими волосами и мальчуган лет 14 в желтой футболке.')
			user.set_room_temp('question', 'action')
		elif text == ESCAPE:
			reply('Ты услышал отрыжку и закрыл за собой дверь')
			user.leave(reply)
	elif question == 'action':
		if text == HELLO:
			reply('Вы слышите, как они начинают переговариваться между собой')
			reply(
				'—Рик, нам... нам надо отсюда убираться, Рик... Это свидетель, Рик, он нас сдаст, Рик\n'
				'—М-Морти... Хватит психовать, все будет нормаль *отрыжка* нормально, Морти... Пошли домой'
			)
			reply('Они прыгнули в портал и он исчезли')
			reply('На полу вы нашли полную флягу какого-то крепкого напитка.')

			user.add_item('special', 'whisky')
			user.leave(reply)

			reply('Из-за запаха алкоголя за тобой пошел какой-то бомж')
		else:
			reply('Мужик одним ловким движением достал пистолет и... заморозил тебя')
			reply('Приходи через 2 годика, может, уже и оттаешь')

			user.reborn(reply, 'Еще чуть-чуть и оттаешь!')

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ READY, ESCAPE ]
	elif question == 'action':
		ans = [ HELLO, FIGHT ]

	random.shuffle(ans)

	return ans