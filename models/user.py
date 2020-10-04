import sqlite3
from db import db

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def find_by_username(cls, username):

        # cls.query => returns the 'query builder' like so: SELECT * FROM users 
        # username= This is the table column name we are filtering by

        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_id(cls, _id):
        
        # id= This is the table column name we are filtering by

        return cls.query.filter_by(id=_id).first()
        