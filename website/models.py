from flask import Flask
from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin



class List(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))
    lists = db.relationship('List')
    

