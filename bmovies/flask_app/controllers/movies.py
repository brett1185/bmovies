from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.movie import Movie

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data= {
        'id':session['user_id']
    }
    return render_template('dashboard.html', user=User.get_by_id(data), movies=Movie.get_all_movies())

@app.route('/movie')
def movie_page():
    return render_template('addMovie.html')

@app.route('/movie/add', methods = ['POST'])
def add_movie():
    if 'user_id' not in session:
        return redirect('/')
    if not Movie.validate_movie(request.form):
        return redirect('/movie')
    data={
        'title': request.form['title'],
        'date_released': int(request.form['date_released']),
        'summary': request.form['summary'],
        'user_id':session['user_id']
        }
    Movie.save(data)
    return redirect('/dashboard')