# -*- coding: utf-8 -*-
"""
	The iterable is an object with elements that can be looped
	over, the iterator represents a specific location in that
	iterable.
"""

class CapitalIterable:

    def __init__(self, string):
        self.string = string

    def __iter__(self):
    	return CapitalIterator(self.string)


class CapitalIterator:

	def __init__(self, string):
		self.words = [w.capitalize() for w in string.split()]
		self.index = 0
	# python 2.x in python 3.x it should be __next__
	def next(self):
		if self.index == len(self.words):
			raise StopIteration()

		word = self.words[self.index]
		self.index += 1
		return word

	def __iter__(self):
		return self

if __name__ == '__main__':
	iterable = CapitalIterable('the quick brown\
								fox jumps over the lazy dog')
	iterator = iter(iterable)
	while True:
		try:
			print(next(iterator))
		except StopIteration:
			break