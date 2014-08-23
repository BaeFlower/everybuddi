"""
models.py

"""

from apps import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    region = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(255), nullable=False)
    orgin_school = db.Column(db.String(255), nullable=False)
    korea_school = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(255))
    intro = db.Column(db.Text())
    hobby = db.Column(db.Text())
    like = db.Column(db.Text())
    state = db.Column(db.String(20))
    checkcode = db.Column(db.Integer)


class Language(db.Model):
    __tablename__ = 'language'
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(255), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.ForeignKey('user.id'))
    user_language = db.relationship('User', backref=db.backref('user_language', cascase='all, delete-orphan', lazy='dynamic'))
