# -*- coding: utf-8 -*-

import random
import string
import pickle
import datetime

def random_psw(length = 4):
	chars = string.letters + string.digits
	s = [random.choice(chars) for i in range(length)]
	date = datetime.date.today()
	dic = {'date': date, 'psw': s}
	with open('psw.pickle', 'wb') as p:
		pickle.dump(dic, p)

if __name__ == '__main__':
	random_psw()