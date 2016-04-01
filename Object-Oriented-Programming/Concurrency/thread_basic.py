# -*- coding: utf-8 -*-
from threading import Thread


class InputReader(Thread):

    def run(self):
        self.line_of_text = raw_input()


print("Enter some text and press enter: ")
thread = InputReader()  # it's the second thread besides the main thread
thread.start()  # run(), in the meantime, main thread continues executing.

count = result = 1
while thread.is_alive():
    result = count * count
    count += 1

print("calculated squares up to {0} * {0} = {1}".format(count, result))
print("while you typed '{}'".format(thread.line_of_text))
