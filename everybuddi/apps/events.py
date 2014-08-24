

from flask import request, redirect, url_for, render_template, Flask
from apps import app


@app.route('/events/events_create', methods=['GET', 'POST'])
def events_create():
    return render_template('events/events_create.html')


@app.route('/events/events_list', methods=['GET'])
def events_list():
    return render_template('events/events.html')


@app.route('/events/events_update', methods=['GET', 'POST'])
def events_update():
    pass


@app.route('/events/events_delete', methods=['GET', 'POST'])
def events_delete():
    pass




