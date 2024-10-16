from flask import Blueprint, render_template, session
from app.models.attendance import Attendance  # Import the Attendance model

view_attendance_bp = Blueprint('view_attendance', __name__)


@view_attendance_bp.route('/view-attendance')
def view_attendance():
    # Retrieve the user ID from the session
    user_id = session.get('user_id')

    # Check if the user is logged in
    if user_id:
        # Query attendance data for the logged-in student
        student_attendance = Attendance.query.filter_by(student_id=user_id).all()

        return render_template('view_attendance.html', student_attendance=student_attendance)
    else:
        # Redirect to login page if user is not logged in
        return redirect(url_for('login'))  # Adjust 'login' to your actual login route