from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models.course import Course
from app.models.grade import Grade
from app.models.student import Student
from app.models.module import Module
from app.models.assignment import Assignment  # Import Assignment model
from app import db

input_grades_bp = Blueprint('input_grades', __name__)

@input_grades_bp.route('/input_grades', methods=['GET', 'POST'])
def input_grades():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        course_id = request.form.get('course_id')
        module_id = request.form.get('module_id')
        assignment_id = request.form.get('assignment_id')  # Get assignment_id from form
        grade = request.form.get('grade')

        new_grade = Grade(student_id=student_id, module_id=module_id, assignment_id=assignment_id, grade=grade)

        try:
            db.session.add(new_grade)
            db.session.commit()
            flash('Grade added successfully.', 'success')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            db.session.rollback()

        return redirect(url_for('input_grades.input_grades'))

    students = Student.query.all()
    courses = Course.query.all()
    selected_course_id = request.args.get('course_id')
    if selected_course_id:
        modules = Module.query.filter_by(course_id=selected_course_id).all()
    else:
        modules = []
    
    # Fetch assignments from the database using a scoped session
    with db.session() as session:
        assignments = session.query(Assignment).all()

    return render_template('input_grades.html', students=students, courses=courses, modules=modules, assignments=assignments)
