from flask import Blueprint, redirect, url_for, render_template, request, session, flash
from app.models.student import Student
from app.models.teacher import Teacher
from app.models.administrator import Administrator
from app import db

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query the database for the user based on the provided username
        student = Student.query.filter_by(username=username, password=password).first()
        teacher = Teacher.query.filter_by(username=username, password=password).first()
        administrator = Administrator.query.filter_by(username=username, password=password).first()

        if student:
            # Authentication successful for student
            session['user_id'] = student.student_id
            session['username'] = student.username
            session['role'] = 'student'
            session['first_name'] = student.first_name
            session['last_name'] = student.last_name  # Assign last name to session


            # Redirect to the student dashboard
            return redirect(url_for('student_dashboard.dashboard'))
        elif teacher:
            # Authentication successful for teacher
            session['teacher_id'] = teacher.teacher_id  # Set teacher_id session variable
            session['username'] = teacher.username
            session['role'] = 'teacher'
            session['first_name'] = teacher.first_name
            session['last_name'] = teacher.last_name  # Assign last name to session


            # Redirect to the teacher dashboard
            return redirect(url_for('teacher_dashboard.teacher_dashboard'))
        elif administrator:
            # Authentication successful for administrator
            session['administrator_id'] = administrator.id  # Set administrator_id session variable
            session['username'] = administrator.username
            session['role'] = 'administrator'
            session['first_name'] = administrator.first_name
            session['last_name'] = administrator.last_name  # Assign last name to session


            # Redirect to the administrator dashboard
            return redirect(url_for('administrator_dashboard.dashboard'))
        else:
            # Invalid credentials, render login form with error message
            flash('Invalid username or password. Please try again.', 'error')
            return render_template('authentication/login.html')
    else:
        # If request method is GET, render the login form
        return render_template('authentication/login.html')
