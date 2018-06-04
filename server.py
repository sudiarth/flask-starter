from flask import Flask, flash, session, request, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hotel')
def hotel():
    return render_template('hotel.html')

@app.route('/plane')
def plane():
    return render_template('plane.html')

@app.route('/train')
def train():
    return render_template('train.html')

@app.route('/automobile')
def automobile():
    return render_template('automobile.html')

@app.route('/boat')
def boat():
    return render_template('boat.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

app.run(debug=True)