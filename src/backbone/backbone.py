#!/usr/bin/python

'''
File: backbone.py

Backend module to maintain the data analytics portion of Spinosaurus
'''

from os.path import abspath, dirname, join


def FileIO():

	'''
	Imports parsed PDF text.
	Input:None
	Output: text -> data as string
	'''

	text = ""
	fileName = "testData"

	# Dir is hardcoded
	BASEDIR = dirname(abspath(__file__))
	path = join(BASEDIR, str(fileName) + ".txt")

	# Avoids issues with bytecodes
	try:
		with open(path, 'r') as inputFile:
			for i in range(sum(1 for line in open(path, 'r'))):
				lines = str(inputFile.readline())
				text += lines

	except IOError:
		exit(str(fileName) + ".txt does not exist.")

	return text


# def Slouch(x, y, z):

	# determine what a slouching angle would be