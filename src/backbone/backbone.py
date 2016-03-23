#!/usr/bin/python

'''
File: backbone.py

Backend module to maintain the data analytics portion of Spinosaurus
'''

from math import acos, asin, degrees, sqrt, pi, atan2
from os.path import abspath, dirname, join


CHART_RANGE = 29.0

def Brainstem():

	'''
	Imports data
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


def FunnyBone():

	'''
	Manages data
	Input: None
	Output: a lot
	'''


	text = Brainstem().split('\n')[:-1]

	domain = text[-1], text[0], len(text) - 2

	Cerebellum(domain)

	del text[0]
	del text[-1]

	for i in text:
		Slouch( float(i.split()[0]), float(i.split()[1]), float(i.split()[2]) )



def Cerebellum(domain):

	'''
	Manages the time duration of the sensor's use
	Input: tuple of the 2 endpoints of the range of time
	Output: time domain evenly divided for a linear chart
	'''

	upper = domain[0].split()[3].split(':')
	lower = domain[1].split()[3].split(':')
	intervals = domain[2]

	hours = float( float(upper[0]) - float(lower[0]) )
	minutes = float( ( float(upper[1]) - float(lower[1]) ) + ( hours * 60 ) )
	seconds = float( ( float(upper[2]) - float(lower[2]) ) + ( minutes * 60 ) )
	# intervals = float( seconds / intervals * CHART_RANGE )

	print seconds, intervals


def Slouch(x, y, z):


	# angle = float( ( x / sqrt( x**2 + y**2 + z**2 ) ) )

	x = int( (x * 100) + 0.5 ) / 100.0
	y = int( (y * 100) + 0.5 ) / 100.0
	z = int( (z * 100) + 0.5 ) / 100.0

	# print angle

	# minVal = 265;
	# maxVal = 402;

	# PI = pi

	# xAng = map(x, minVal, maxVal, -90, 90);
	# yAng = map(y, minVal, maxVal, -90, 90);
	# zAng = map(z, minVal, maxVal, -90, 90);

	# x = degrees(atan2(-yAng, -zAng) + PI);
	# y = degrees(atan2(-xAng, -zAng) + PI);
	# z = degrees(atan2(-yAng, -xAng) + PI);


	if ( x < 90):
		print "SLOUCH", x, y, z

	# if (angle < 90 or angle > 135):
	# 	print "NOT SLOUCH", angle

	# determine what a slouching angle would be;
	# 'ideal' degrees are between >90 - 135
	# need calc 3 notes




FunnyBone()