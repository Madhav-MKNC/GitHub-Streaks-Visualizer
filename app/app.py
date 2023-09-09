#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: Madhav 
# github: https://github.com/Madhav-MKNC

import os
from dotenv import load_dotenv
load_dotenv()

from utils import *

from flask import Flask, jsonify, render_template
from waitress import serve
from flask_cors import CORS


# flask app
app = Flask(__name__)
CORS(app=app)


# # index
# @app.route('/')
# def index():
#     return jsonify({
#         "status": "Online",
#         "info": "For fetching github-streaks-visualization goto: /<username>"
#     })

# user chart
@app.route('/<username>', methods=['GET','POST'])
def index(username):
    # if valid username
    if is_valid(username):
        return render_template('index.html', username=username)
    
    return jsonify({
        "status": "Username not found!"
    })

# returns streaks data
@app.route('/graph/<username>', methods=['GET','POST'])
def get_graph_data(username):
    # if valid username
    if is_valid(username):
        streaks = get_user_streaks(username)
        return jsonify(streaks)
    
    return jsonify({
        "status": "Username not found!"
    })


# run server
def start_server():
    serve(app, host=HOST, port=PORT)

# main
if __name__ == '__main__':
    print(f"[+] Server Online at: {HOST}:{PORT}")
    start_server()