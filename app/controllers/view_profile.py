from flask import Blueprint, render_template, session
from app.models.student import Student
from app.models.teacher import Teacher
from app.models.administrator import Administrator

view_profile_bp = Blueprint('view_profile', __name__)

@view_profile_bp.route('/view_profile')
def view_profile():
    # Get the user's role and ID from the session
    role = session.get('role')
    user_id = session.get('user_id')

    # Retrieve user profile based on role
    if role == 'student':
        user = Student.query.get(user_id)
    elif role == 'teacher':
        user = Teacher.query.get(user_id)
    elif role == 'administrator':
        user = Administrator.query.get(user_id)
    else:
        # Handle unknown roles
        return "Unknown user role"

    # Render the view profile template with user information
    return render_template('view_profile.html', user=user)
