#!/usr/bin/env python3


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__=='__main__':
    app.run(port=5555, debug=True)
    
# Environment Variables to run Flask App

# 1. Go into server folder
# 2. Either run 'flask run' or 'python app.py' these commands look for an app.py file
# and make sure the code above is within the app.py file in order to execute.