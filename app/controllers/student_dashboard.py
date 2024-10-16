# Student Dashboard Blueprint
from flask import Blueprint, render_template, session, redirect, url_for

student_dashboard_bp = Blueprint('student_dashboard', __name__)

@student_dashboard_bp.route('/student/dashboard')
def dashboard():
    if session.get('role') == 'student':
        first_name = session.get('first_name')
        return render_template('dashboard/student_dashboard.html', first_name=first_name)
    else:
        return redirect(url_for('login.login'))