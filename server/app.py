#!/usr/bin/env python3

from flask import Flask
#static route
app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Welcome to my page!</h1>"
#dynamic route
@app.route('/<string:username>')
def user_profile(username):
    return f"<h1>Welcome {username}!</h1>"

#run application as a script
if __name__ == '__main__':
    app.run(port=5555, debug=True)