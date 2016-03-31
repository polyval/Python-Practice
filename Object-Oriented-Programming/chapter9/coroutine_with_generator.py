# -*- coding: utf-8 -*-

def tally():
	score = 0
	while True:
		increment = yield score
		score += increment
# send() method acts like next()
# it also allows to pass in a value from
# outside of the generator

# white = tally()
# blue = tally()
# next(white)
# 0
# next(blue)
# 0
# white.send(3)
# 3
# bule.send(2)
# 2
# white.send(2)
# 5
# blue.send(2)
# 6