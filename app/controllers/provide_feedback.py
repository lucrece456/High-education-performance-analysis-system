# Import necessary modules and classes
from flask import Blueprint, render_template, session
from app.models.student import Student
from app.models.feedback import Feedback
import sys

# Create a Blueprint for providing feedback
provide_feedback_bp = Blueprint('provide_feedback', __name__)

# Define route for providing feedback
@provide_feedback_bp.route('/provide_feedback')
def provide_feedback():
    # Retrieve student_id from the session
    student_id = session.get('student_id')
    
    # Check if student_id exists in the session
    if student_id:
        # Query the database for the student
        student = Student.query.get(student_id)
        print('We are in line 20')
        sys.stdout.write('We are in line 21')
        
        # Check if student exists
        if student:
            # Query the database for feedback associated with the student
            feedback = Feedback.query.filter_by(student_id=student_id).all()
            print('We are in line 27')
            sys.stdout.write('We are in line 28')
            # Render the template with student and feedback data
            return render_template('provide_feedback.html', student=student, feedback=feedback)
        else:
            # Render an error template if student is not found
            print('We are in line 33')
            sys.stdout.write('We are in line 34')
            return render_template('error.html', error_message="Student not found")
    else:
        # Render an error template if student_id is not found in the session
        return render_template('error.html', error_message="Student ID not found in session")
        print('We are in line 39')
        sys.stdout.write('We are in line 40')
        
