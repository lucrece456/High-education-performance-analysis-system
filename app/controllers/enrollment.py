from flask import Blueprint, request, render_template, jsonify
from app.models.enrollment import Enrollment
from app.models.student import Student
from app.models.course import Course
from datetime import date
from app import db

enrollment_bp = Blueprint('enrollment', __name__)

@enrollment_bp.route('/enroll', methods=['GET', 'POST'])
def enroll_student():
    if request.method == 'POST':
        # Process POST request for enrolling student
        data = request.form
        student_id = data.get('student_id')
        course_id = data.get('course_id')

        # Validate student_id and course_id
        if not student_id or not course_id:
            return jsonify({'message': 'Invalid student_id or course_id'}), 400

        # Check if the student is already enrolled in the course
        if Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first():
            return jsonify({'message': 'Student is already enrolled in the course'}), 400

        # Create a new enrollment record
        enrollment = Enrollment(student_id=student_id, course_id=course_id, enrollment_date=date.today())
        db.session.add(enrollment)
        db.session.commit()

        return jsonify({'message': 'Enrollment successful'}), 201

    # If the request method is GET, render the enrollment form
    students = Student.query.all()  # Fetch students from the database
    courses = Course.query.all()   # Fetch courses from the database
    return render_template('enrollment_form.html', students=students, courses=courses)