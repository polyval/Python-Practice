# -*- coding: utf-8 -*-
# with ZipProcessor, it's much easier to write other classes
# that operate on files in a ZIP archive, and we can change
# only the one ZipProcessor base class to improve or bug fix
# the zip functionality
from zip_processor import ZipProcessor
import sys
import os


class ZipReplace(ZipProcessor):

    def __init__(self, filename, search_string, replace_string):
    	super(ZipReplace, self).__init__(filename)
    	self.search_string = search_string
    	self.replace_string = replace_string

    def process_files(self):
    	"""
    	Perform a search and replace on all files in the temporary directory
    	"""
    	for filename in self.temp_directory.iterdir():
    		with filename.open() as file:
    			contents = file.read()
    		contents = contents.replace(self.search_string, self.replace_string)
    		with filename.open("w") as file:
    			file.write(contents)

if __name__ == '__main__':
	ZipReplace(*sys.argv[1:4]).process_zip()
