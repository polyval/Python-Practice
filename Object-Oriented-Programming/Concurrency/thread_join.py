# -*- coding: utf-8 -*-

from threading import Thread
import json
from urllib2 import urlopen
import time

CITIES = [
    'Edmonton', 'Victoria', 'Winnipeg',
    'Fredericton', 'Regina']

class TempGetter(Thread):

	def __init__(self, city):
		super(TempGetter, self).__init__()
		self.city = city

	def run(self):
		url_template = ('http://api.openweathermap.org/data/2.5/'
						'weather?q={},CA&units=metric') # need a valid APPID
		response = urlopen(url_template.format(self.city))
		data = json.loads(response.read().decode())
		self.temperature = data['main']['temp']

threads = [TempGetter(c) for c in CITIES]
start = time.time()
for thread in threads:
	thread.start()

for thread in threads:
	thread.join() # wait for the thread to complete before doing anything

for thread in threads:
	print(
		"it is{0.temperature:.0f} in {0.city}".format(thread)
		)
	print(
		"Got {} temps in {} seconds".format(len(threads), time.time()-start)
		)
