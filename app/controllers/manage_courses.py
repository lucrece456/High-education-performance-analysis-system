from flask import Blueprint, request, render_template, redirect, url_for
from app.models.course import Course
from app import db 

manage_courses_bp = Blueprint('manage_courses', __name__)

@manage_courses_bp.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return render_template('manage_courses.html', courses=courses)

@manage_courses_bp.route('/courses/add', methods=['POST'])
def add_course():
    course_name = request.form['course_name']
    course_code = request.form['course_code']
    description = request.form['description']
    # Add other course details as needed
    course = Course(course_name=course_name, course_code=course_code, description=description)
    db.session.add(course)
    db.session.commit()
    return redirect(url_for('manage_courses.get_courses'))

@manage_courses_bp.route('/manage_courses')
def manage_courses():
    # Logic to retrieve and display courses
    courses = Course.query.all()
    return render_template('manage_courses.html', courses=courses)

@manage_courses_bp.route('/edit_course/<int:course_id>', methods=['GET'])
def edit_course(course_id):
    # Retrieve the course from the database
    course = Course.query.get(course_id)

    # Check if the course exists
    if course:
        # Render the edit_course.html template with the course details
        return render_template('edit_course.html', course=course)
    else:
        # If the course does not exist, render an error template or redirect to an error page
        return render_template('course_not_found.html', course_id=course_id), 404

@manage_courses_bp.route('/courses/delete/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    # Logic to delete the course with the specified course_id
    return redirect(url_for('manage_courses.get_courses'))

@manage_courses_bp.route('/courses/search', methods=['GET'])
def search_courses():
    query = request.args.get('query')
    # Logic to search for courses in the database based on the query
    courses = Course.query.filter(Course.course_name.ilike(f'%{query}%')).all()
    return render_template('manage_courses.html', courses=courses)

@manage_courses_bp.route('/courses/update/<int:course_id>', methods=['POST'])
def update_course(course_id):
    # Retrieve the course from the database
    course = Course.query.get(course_id)

    if not course:
        return "Course not found", 404

    # Update course details based on the form submission
    course.course_name = request.form['course_name']
    course.course_code = request.form['course_code']
    course.description = request.form['description']

    # Commit the changes to the database
    db.session.commit()

    # Redirect back to the course list page
    return redirect(url_for('manage_courses.get_courses'))
