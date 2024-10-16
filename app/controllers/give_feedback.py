from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.assignment import Assignment
from app.models.feedback import Feedback
from app.models.student import Student

from app import db

give_feedback_bp = Blueprint('give_feedback', __name__)

@give_feedback_bp.route('/give-feedback', methods=['GET', 'POST'])
def give_feedback():
    if request.method == 'POST':
        # Get feedback data from form
        assignment_id = request.form.get('assignment_id')
        student_id = request.form.get('student_id')
        feedback_text = request.form.get('feedback_text')

        # Create new feedback instance
        feedback = Feedback(assignment_id=assignment_id, student_id=student_id, feedback_text=feedback_text)

        # Add feedback to the database
        db.session.add(feedback)
        db.session.commit()

        flash('Feedback submitted successfully.', 'success')
        return redirect(url_for('give_feedback.give_feedback'))

    else:
        # Retrieve assignments and students for the form
        assignments = Assignment.query.all()
        students = Student.query.all()

        return render_template('give_feedback.html', assignments=assignments, students=students)
