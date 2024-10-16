# Teacher Dashboard Blueprint
from flask import Blueprint, render_template, session, redirect, url_for

teacher_dashboard_bp = Blueprint('teacher_dashboard', __name__)

@teacher_dashboard_bp.route('/teacher/dashboard')
def teacher_dashboard():
    if session.get('role') == 'teacher':
        first_name = session.get('first_name')
        return render_template('dashboard/teacher_dashboard.html', first_name=first_name)
    else:
        return redirect(url_for('login.login'))