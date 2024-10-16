# app/controllers/admin.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash
from app.models.student import Student
from app.models.teacher import Teacher
from app.models.administrator import Administrator
from app import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if 'role' not in session or session['role'] != 'administrator':
        flash('You do not have permission to access this page.', 'error')
        return redirect(url_for('login.login'))

    if request.method == 'POST':
        user_type = request.form['user_type']
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        hashed_password = generate_password_hash(password)

        if user_type == 'student':
            date_of_birth = request.form['date_of_birth']
            address = request.form['address']
            level = request.form['level']
            new_user = Student(username=username, password=hashed_password, first_name=first_name, last_name=last_name, email=email, date_of_birth=date_of_birth, address=address, level=level)
        elif user_type == 'teacher':
            specialization = request.form['specialization']
            new_user = Teacher(username=username, password=hashed_password, first_name=first_name, last_name=last_name, email=email, specialization=specialization)
        elif user_type == 'administrator':
            new_user = Administrator(username=username, password=hashed_password, first_name=first_name, email=email)
        else:
            flash('Invalid user type specified.', 'error')
            return redirect(url_for('admin.add_user'))

        db.session.add(new_user)
        db.session.commit()

        flash(f'New {user_type} added successfully!', 'success')
        return redirect(url_for('admin.add_user'))

    return render_template('admin/add_user.html')
