from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db='Bmovies'
    @staticmethod
    def validate_user( user ):
        is_valid = True
        query='select * from users where email = %(email)s;'
        results=connectToMySQL(User.db).query_db(query, user)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'register')
            is_valid = False
        if len(user['f_name']) < 2:
            flash('First name must be at least 3 characters', 'register')
            is_valid=False
        if len(user['l_name']) < 2:
            flash('Last name must be at least 3 characters', 'register')
            is_valid = False
        if len(user['password']) < 8:
            flash ('Password must be at least 8 characters', 'register')
            is_valid=False
        if user['confirm_password'] != user['password']:
            flash('Passwords do not match', 'register')
            is_valid = False
        return is_valid
        
    def __init__(self,data):
        self.id=data['id']
        self.f_name=data['f_name']
        self.l_name=data['l_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save(cls, data):
        query='insert into users (f_name, l_name, email, password) values (%(f_name)s, %(l_name)s, %(email)s, %(password)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query='select * from users'
        results=connectToMySQL(cls.db).query_db(query)
        users=[]
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_email(cls, data):
        query='select *  from users where email = %(email)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query='select * from users where id = %(id)s;'
        results =connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    




