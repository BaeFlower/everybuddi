# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField,
    DateField,
    SelectField
)
from wtforms import validators
from wtforms.fields.html5 import EmailField


class EventsForm(Form):
    theme = SelectField(
        u'theme',
        choices=[(u'study', u'study'), (u'party', u'party'), (u'travel', u'travel'), (u'eating', u'eating')
                        , (u'movie', u'movie'), (u'etc', u'etc')],
        description={'placeholder': u'theme', 'class': u'form-control'}
    )
    title = StringField(
        u'title',
        [validators.data_required(u'제목을 입력해주세요.')],
        description={'placeholder': u'title', 'class': u'form-control'}
    )
    content = TextAreaField(
        u'content',
        [validators.data_required(u'내용을 입력해주세요.')],
        description={'placeholder': u'content', 'class': u'form-control'}
    )
    place_school = StringField(
        u'place_school',
        [validators.data_required(u'내용을 입력해주세요.')],
        description={'placeholder': u'school', 'class': u'form-control'}
    )
    event_date = DateField(
        u'date',
        [validators.data_required(u'내용을 입력해주세요.')],
        description={'placeholder': u'date', 'class': u'form-control'}
    )
    contact = StringField(
        u'contact',
        [validators.data_required(u'내용을 입력해주세요.')],
        description={'placeholder': u'contact(email/phone/facebook)', 'class': u'form-control'}
    )
    cost = StringField(
        u'cost',
        [validators.data_required(u'내용을 입력해주세요.')],
        description={'placeholder': u'cost', 'class': u'form-control'}
    )


