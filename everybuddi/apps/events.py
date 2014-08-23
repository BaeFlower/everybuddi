"""
    events.py
"""

from flask import render_template
from apps import app


@app.route('/events/create')
def events():
    return render_template('events/events.html')


@app.route('/events/read', methods=['GET', 'POST'])
def events_create():
    pass


@app.route('/events/update', methods=['GET', 'POST'])
def events_upgrade():
    pass


@app.route('/events/delete', methods=['GET', 'POST'])
def events_delete():
    pass

