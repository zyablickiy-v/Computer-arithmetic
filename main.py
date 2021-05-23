import struct
import eel
from random import randint, random

from pairs import pairs
import example as ex
from config import config as CONFIG

eel.init('wgui')
eel.start('', block=False, size=CONFIG['WIN_SIZE'])

@eel.expose
def WindowClose():
	exit()

lastSentTest = [None]
name, group = '', ''

@eel.expose
def GetTime():
	return CONFIG['TIME']

@eel.expose
def GenTest(_name, _group, train, TN=None):
	global name, group
	name, group = _name, _group
	rs = []

	n1 = int(TN and TN[0] or CONFIG['TASKS_1'])
	n2 = int(TN and TN[1] or CONFIG['TASKS_2'])
	n3 = int(TN and TN[2] or CONFIG['TASKS_3'])

	for _ in range(n1):
		num = random() * 1000 * (1 if randint(0, 1) else -1)
		bin = binary(num)
		bin = bin[len(bin) - 32:len(bin)]
		t = {
			'answer': None,
			'question_': 'Введите представление следующего вещественного числа в ячейке памяти (32 бита):' + str(num),
			'question': {
				'text': 'Введите представление следующего вещественного числа в ячейке памяти (32 бита):',
				'expr': [num],
				'inputHints': ['Введите ответ']
			}, 
			'correctAnswer': bin
		}
		rs.append(t)
	def hoba():
		pass
	for _ in range(n2):
		nums = []
		for __ in range(2):
			num = random() * 1000 * (1 if randint(0, 1) else -1)
			bin = binary(num)
			bin = bin[len(bin) - 32:len(bin)]
			nums.append([num, bin])
		t = {
			'answer': None,
			'question_': f'Выполните в двоичной ячейке памяти: {nums[0]} + {nums[1]}',
			'question': {
				'text': 'Выполните в двоичной ячейке памяти: ',
				'inputHints': [
					'Введите двоичное представление первого числа',
					'Введите двоичное представление второго числа'
				],
				'expr': [nums[0][0], nums[1][0]]
			}, 
			'correctAnswer': nums[0][1] + nums[1][1]
		}
		rs.append(t)
	

	global lastSentTest
	lastSentTest = []
	for v in rs:
		lastSentTest.append(dict(v))
	if not train:
		for i in range(len(rs)):
			rs[i]['correctAnswer'] = None
	return rs


@eel.expose
def Judge(test, train):
	global lastSentTest
	total = len(lastSentTest)
	done = 0
	tasks = []
	for i in range(len(lastSentTest)):
		v = lastSentTest[i]
		ok = isinstance(test[i]['answer'], str) and test[i]['answer'].replace(' ', '') == v['correctAnswer'].replace(' ', '') #Корректность ответа
		lastSentTest[i]['answer'] = test[i]['answer']
		if ok:
			done += 1
		tasks.append({
			'answer': test[i]['answer'],
			'correctAnswer': v['correctAnswer'],
			'correct': ok
		})
	mark = done / total
	if not train:
		ex.SendToServer(CONFIG['IP'], name, group, mark, lastSentTest)
	vmark = 0
	for i, threshold in pairs(CONFIG['VRATES']):
		if mark * 100 >= threshold:
			vmark = 5 - i
			break
	return { 'tasks': tasks, 'mark': mark, 'vmark': vmark }
# https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex
def binary(num):
	return ''.join(bin(c).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))

while True:
	eel.sleep(10)
