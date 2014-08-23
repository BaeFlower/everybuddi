from flask import request, redirect, url_for, render_template, Flask
from apps import app
# app -> Flask()


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


