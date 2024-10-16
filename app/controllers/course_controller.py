from flask import Blueprint, request, jsonify
from app import db
from app.models import Course

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses', methods=['GET'])
def get_courses():
    # Logic to retrieve and return course data
    courses = Course.query.all()
    course_data = [{'id': course.id, 'name': course.name, 'code': course.code} for course in courses]
    return jsonify(course_data)

@course_bp.route('/courses', methods=['POST'])
def create_course():
    data = request.json
    course = Course(name=data['name'], code=data['code'])
    db.session.add(course)
    db.session.commit()
    return jsonify({'message': 'Course created successfully', 'id': course.id}), 201

@course_bp.route('/courses/<int:id>', methods=['PUT'])
def update_course(id):
    course = Course.query.get_or_404(id)
    data = request.json
    course.name = data['name']
    course.code = data['code']
    db.session.commit()
    return jsonify({'message': 'Course updated successfully'}), 200

@course_bp.route('/courses/<int:id>', methods=['DELETE'])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({'message': 'Course deleted successfully'}), 200    