from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.movie import Movie

@app.route('/dashboard')
def dashboard():
    if not User.validate_user(request.form):
        return redirect('/')
    data= {
        'id':session['user_id']
    }
    return render_template('dashboard.html', user=User.get_by_id(data), movies=Movie.get_all_movies())