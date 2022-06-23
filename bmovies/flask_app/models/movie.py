from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Movie:
    db='Bmovies'
    @staticmethod
    def validate_movie(movie):
        is_valid=True
        if len(movie['title']) <2:
            flash('Title must be at least two characters long!')
            is_valid=False
        if len(movie['date_released'])<1900:
            flash('Movies can be old, but not that old!')
            is_valid=False
        if len(movie['summary']) < 10:
            flash('Please write reasonable summary of the movie')
            is_valid=False
        return is_valid

    def __init__(self, data):
        self.id=data['id']
        self.title=data['title']
        self.date_released=data['date_released']
        self.summary=data['summary']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']

    @classmethod
    def save(cls, data):
        query='insert into movies(title, date_released, summary, user_id) values (%(title)s, %(date_released)s, %(summary)s, %(user_id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all_movies(cls):
        query='select * from movies;'
        results= connectToMySQL(cls.db).query_db(query)
        movie_list=[]
        for i in results:
            movie_list.append(cls(i))
        return movie_list

    @classmethod
    def get_one(cls, data):
        query='select * from movies where id=%(id)s;'
        results=connectToMySQL(cls.db).query_db(query, data)
        return (cls(results[0]))

    @classmethod
    def update_movie(cls, data):
        query = 'update moviets set title=%(title)s, date_released=%(date_released)s, summary=%(summary)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete_movie(cls, data):
        query = 'delete from movies where id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
