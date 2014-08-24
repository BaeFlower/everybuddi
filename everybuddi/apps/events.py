# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, render_template, Flask
from apps import app
from apps.forms import EventsForm


@app.route('/events/events_create', methods=['GET', 'POST'])
def events_create():
    form = EventsForm()


    return render_template('events/events_create.html', form=form)


@app.route('/events/events_list', methods=['GET'])
def events_list():
    return render_template('events/events.html')


@app.route('/events/events_update', methods=['GET', 'POST'])
def events_update():
    pass


@app.route('/events/events_delete', methods=['GET', 'POST'])
def events_delete():
    pass




