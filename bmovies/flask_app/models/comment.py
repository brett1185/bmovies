from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Comment:
    db='Bmovies'
    @staticmethod
    def validate_comment(comment):
        is_valid=True
        if len(comment['comment']) < 3:
            flash('Please write a full comment')
            is_valid=False
        return is_valid

    def __init__(self, data):
        self.idcomments=data['idcomments']
        self.comment=data['comment']
        self.user_id=data['user_id']
        self.movie_id=data['user_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save(cls, data):
        query='insert into comments (comment, user_id, movie_id) values (%(comment)s, %(user_id)s, %(movie_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all_comments(cls):
        query='select * from comments left join movies on movies.id = comments.movie_id'
        results = connectToMySQL(cls.db).query_db(query)
        all_comments=[]
        for i in results:
            all_comments.append(cls(i))
        return all_comments




        
        
