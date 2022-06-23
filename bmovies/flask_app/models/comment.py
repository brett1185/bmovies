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
    


        
        
