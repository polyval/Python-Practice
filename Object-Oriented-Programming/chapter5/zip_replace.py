# -*- coding: utf-8 -*-
# this example is used to demonstrate the use of Manager objects

import sys
import shutil
import zipfile
from pathlib import Path
# pathlib is standard library in Python 3.4, but not in Python 2
# install pathlib via pip


class ZipReplace:

	def __init__(self, filename, search_string, replace_string):
		self.filename = filename
		self.search_string = search_string
		self.replace_string = replace_string
		self.temp_directory = Path("unzipped-{}".format(filename))

	def zip_find_replace(self):
		"""
		The delegation method
		"""
		self.unzip_files()
		self.find_replace()
		self.zip_files()

	def unzip_files(self):
		self.temp_directory.mkdir()
		with zipfile.ZipFile(self.filename) as zip:
			zip.extractall(str(self.temp_directory))

	def find_replace(self):
		for filename in self.temp_directory.iterdir():
			with filename.open() as file:
				contents = file.read()
			contents = contents.replace(
	        		self.search_string, self.replace_string)
			with filename.open("w") as file:
				file.write(contents)

	def zip_files(self):
		with zipfile.ZipFile(self.filename, 'w') as file:
			for filename in self.temp_directory.iterdir():
				file.write(str(filename), filename.name)
		shutil.rmtree(self.temp_directory)

if __name__ == "__main__":
	# run from the command line
	# python zipsearch.py hello.zip hello hi
    ZipReplace(*sys.argv[1:4]).zip_find_replace()