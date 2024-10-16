from flask import Blueprint, render_template

attendance_tracking_bp = Blueprint('attendance_tracking', __name__)

@attendance_tracking_bp.route('/attendance_tracking')
def attendance_tracking():
    # Logic to retrieve and display user profile
    return render_template('attendance_tracking.html')
