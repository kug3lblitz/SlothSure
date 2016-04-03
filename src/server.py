#!/usr/bin/python

'''
File: server.py

Server management for the data analytics portion of Spinosaurus
'''

from json import dumps, load

from flask import Flask, render_template, request
from reader.tacocat import Tacocat

app = Flask(__name__)


@app.route('/')
def home():
	# tacocat_obj = Tacocat()
	#
	# tacocat_obj.racecar()

	return render_template('home.html')


@app.route('/success', methods=['GET', 'POST'])
def get_info():
	if request.method == 'GET':
		with open('data.json') as data_file:
			data = load(data_file)

		# json_obj = dumps(data)

		return render_template('anotherplot.html', data=data)


@app.route('/sloth')
def sloth():
	return render_template('sloth.html')


# ----------------------------- main ----------------------------- #

if __name__ == "__main__":
	app.run(debug=True)
