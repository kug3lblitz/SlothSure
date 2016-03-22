#!/usr/bin/python

'''
File: server.py

Server management for the data analytics portion of Spinosaurus
'''


from json import dumps, load

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/success', methods=['GET', 'POST'])
def get_json_information():

    if request.method == 'GET':

        with open('graph.json') as data_file:
            data = load(data_file)

        json_obj = dumps(data)

        return render_template('success.html', data=json_obj)


################################### main ###################################

if __name__ == "__main__":
    app.run(debug = True)