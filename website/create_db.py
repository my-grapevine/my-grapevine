from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired



Base = declarative_base()

class Note(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(1000))
    author = db.Column(db.String(255))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    slug = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class NoteForm(FlaskForm):
    title = StringField ("Title", validators=[DataRequired()])
    content = StringField("Content", validators=[DataRequired()])
    slug = StringField ("Slug", validators=[DataRequired()])
    submit = StringField ("Submit")


class User(db.Model, UserMixin, Base):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


class UserEvent(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

