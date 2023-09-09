#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: Madhav 
# github: https://github.com/Madhav-MKNC

import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify, render_template
from waitress import serve
from flask_cors import CORS


# flask app
app = Flask(__name__)
CORS(app=app)

# server address
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

# Sample streaks data
streaks = [
    {'date': '2023-08-22', 'streak': 5},
    {'date': '2023-08-23', 'streak': 6},
    {'date': '2023-08-24', 'streak': 7},
    {'date': '2023-08-25', 'streak': 8},
    {'date': '2023-08-26', 'streak': 9}
]

# index
@app.route('/<username>', methods=['GET'])
def index(username):
    return render_template('index.html', username=username)

# returns streaks data
@app.route('/user/<username>', methods=['GET'])
def get_graph_data():
    return jsonify(streaks)


# run server
def start_server():
    serve(app, host=HOST, port=PORT)

# main
if __name__ == '__main__':
    print(f"[+] Server Online at: {HOST}:{PORT}")
    start_server()