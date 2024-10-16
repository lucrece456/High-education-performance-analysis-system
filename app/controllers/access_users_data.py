# access_users_data.py

from flask import Blueprint, render_template

create_user_bp = Blueprint('create_user', __name__)

@create_user_bp.route('/create_user')
def create_user():
    return render_template('create_user.html')

edit_user_bp = Blueprint('edit_user', __name__)

@edit_user_bp.route('/edit_user')
def edit_user():
    return render_template('edit_user.html')

delete_user_bp = Blueprint('delete_user', __name__)

@delete_user_bp.route('/delete_user')
def delete_user():
    return render_template('delete_user.html')
