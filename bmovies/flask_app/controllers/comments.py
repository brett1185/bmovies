from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.movie import Movie
from flask_app.models.comment import Comment

@app.route('/add/comment/<int:id>')
def comment():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id':id
    }
    user_data={
        'id':session['user_id']
    }
    render_template('addComment.html', movie=Movie.get_one(data), user=User.get_by_id(user_data)  )


@app.route('/comment/add', methods=['POST'])
def add_comment():
    if 'user_id' not in session:
        return redirect('/')
    if not Comment.validate_comment(request.form):
        return redirect('add/comment')
    data={
        'comment': request.form['comment'],
        'user_id':session['user_id'],
        'movie_id': request.form['movie.id']
        
        }
    Comment.save(data)
    return redirect('movie.html')
    
    