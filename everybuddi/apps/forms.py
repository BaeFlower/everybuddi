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
        [validators.data_required(u'주제를 선택해주세요.')],
        description={'placeholder': u'theme'}
    )
    title = StringField(
        u'title',
        [validators.data_required(u'제목을 입력해주세요.')],
        description={'placeholder': u'title'}
    )
    content = TextAreaField(
        u'content',
        [validators.data_required(u'내용을 입력해주세요.')],
        description={'placeholder': u'content'}
    )
    place_school = StringField(
        u'place_school',
        description={'placeholder': u'school'}
    )
    event_date = DateField(
        u'date',
        description={'placeholder': u'date'}
    )
    contact = StringField(
        u'contact',
        description={'placeholder': u'contact(email/phone/facebook)'}
    )
    cost = StringField(
        u'cost',
        description={'placeholder': u'cost'}
    )


