#!/usr/bin/python

"""
File: backbone.py

Backend module to maintain the data analytics portion of Spinosaurus
"""


from math import degrees, pi, atan2
from os.path import abspath, dirname, join


UPPER_READ = 402.0  # the maximum value of the accelerometer, 1 g
LOWER_READ = 265.0  # the minimum value of the accelerometer, 0 g

BASEDIR = dirname(abspath(__file__))  # base path


def brainstem():
    """Imports data

    Input:None
    Output: text -> data as string
    """

    text = ""
    fileName = "testData"

    # Dir is hardcoded
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


def funnyBone():
    """Manages data

    Input: None
    Output: TBD
    """

    text = brainstem().split('\n')[:-1]

    domain = text[-1], text[0], len(text) - 2

    cerebellum(domain)

    del text[0]
    del text[-1]

    for i in text:
        slouch(float(i.split()[0]), float(i.split()[1]), float(i.split()[2]))


def cerebellum(domain):
    """Manages the time duration of the sensor's use

    Input: tuple of the 2 endpoints of the range of time
    Output: time domain evenly divided for a linear chart
    """

    upper = domain[0].split()[3].split(':')
    lower = domain[1].split()[3].split(':')
    intervals = domain[2]

    hours = float(float(upper[0]) - float(lower[0]))
    minutes = float((float(upper[1]) - float(lower[1])) + (hours * 60))
    seconds = float((float(upper[2]) - float(lower[2])) + (minutes * 60))
    # intervals = float( seconds / intervals * CHART_RANGE )

    print seconds, intervals


def scale(value):
    """Scales the value to a different range;
    for use by atan2 - changing from -90 to 90 to 0 - 360 degrees

    Input: axis value
    Output: the scaled value
    """

    return (value - LOWER_READ) * 180 / (UPPER_READ - LOWER_READ) - 90


def round_angle(value):
    """
    Rounds the value up to the nearest hundredth

    Input: degree of axis
    Output: the angle rounded up
    """

    return int((value * 100) + 0.5) / 100.0


def slouch(x, y, z):
    """Determines if the input values suggest a slouch

    Input: axis values
    Output: alerts if a slouch occurs
    """

    x = round_angle(degrees(atan2(-scale(y), -scale(z)) + pi))
    y = round_angle(degrees(atan2(-scale(x), -scale(z)) + pi))
    z = round_angle(degrees(atan2(-scale(y), -scale(x)) + pi))

    # only one axis should be observed
    # currently testing
    if (x < 80):
        print "SLOUCH", x, y, z


funnyBone()
