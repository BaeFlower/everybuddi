

from flask import request, redirect, url_for, render_template, Flask
from apps import app


@app.route('/events')
def events():
    return render_template('events/events.html')