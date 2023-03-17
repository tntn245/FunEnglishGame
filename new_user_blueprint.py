from flask import render_template, request, url_for, redirect, Blueprint
from datetime import datetime
from user import UserDTO
import db as app

new_user_blueprint = Blueprint('new_user_blueprint', __name__)

@new_user_blueprint.route('/new_user', methods=('GET', 'POST'))
def new_user():
    if request.method=='POST':
        new_user = request.form['new_user']
        user = UserDTO(new_user,False,'',datetime.now(),'',datetime.now())
        app.Users.insert_one(user.__dict__)
        return redirect(url_for('index_blueprint.index'))

    all_Users = list(app.Users.find())
    return render_template('index.html', Users=all_Users)