from flask import Blueprint, render_template, session, redirect, url_for
from app.models.grade import Grade
from app.models.assignment import Assignment
from app import db

view_grades_bp = Blueprint('view_grades', __name__)

@view_grades_bp.route('/view_grades')
def view_grades():
    # Retrieve the user ID from the session
    user_id = session.get('user_id')

    # Check if the user is logged in
    if user_id:
        # Query grades for the logged-in student
        grades = Grade.query.filter_by(student_id=user_id).all()

        # Retrieve assignment titles from the database
        assignments = Assignment.query.all()
        assignment_titles = {assignment.id: assignment.title for assignment in assignments}

        # Calculate average grade
        total_grades = sum(float(grade.grade) for grade in grades)
        average_grade = total_grades / len(grades) if len(grades) > 0 else 0

        # Generate suggestions based on average grade
        if average_grade >= 90:
            suggestion = "Excellent performance! Keep up the good work."
        elif 70 <= average_grade < 90:
            suggestion = "Good job! Maintain your efforts for consistent performance."
        elif average_grade < 70:
            suggestion = "Focus on areas where improvement is needed to enhance performance."
        else:
            suggestion = ""

        # Calculate overall performance
        assignment_scores = {}
        for grade in grades:
            assignment_scores.setdefault(grade.assignment_id, []).append(float(grade.grade))

        overall_performance = {}
        for assignment_id, scores in assignment_scores.items():
            title = assignment_titles.get(assignment_id)
            if title:
                overall_performance[title] = sum(scores) / len(scores)

        return render_template('view_grades.html', grades=grades, overall_performance=overall_performance, assignment_titles=assignment_titles, average_grade=average_grade, suggestion=suggestion)
    else:
        # Redirect to login page if user is not logged in
        return redirect(url_for('login'))
