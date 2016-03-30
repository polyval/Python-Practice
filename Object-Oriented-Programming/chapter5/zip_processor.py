# -*- coding: utf-8 -*-
# modify origin ZipReplace class into a superclass for
# processing generic ZIP files

import os
import sys
import shutil
import zipfile
from pathlib import Path
# pathlib is standard library in Python 3.4, but not in Python 2
# install pathlib via pip


class ZipProcessor:

	def __init__(self, zipname):
		self.zipname = zipname
		self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))

	def process_zip(self):
		"""
		The delegation method
		"""
		self.unzip_files()
		self.process_files() # this method is handled in subclass
		self.zip_files()

	def unzip_files(self):
		self.temp_directory.mkdir()
		with zipfile.ZipFile(self.zipname) as zip:
			zip.extractall(str(self.temp_directory))

	def zip_files(self):
		with zipfile.ZipFile(self.zipname, 'w') as file:
			for filename in self.temp_directory.iterdir():
				file.write(str(filename), filename.name)
		shutil.rmtree(self.temp_directory)