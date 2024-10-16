from flask import Blueprint, request, render_template
from app.models import Student  # Assuming Student model is imported

search_student_bp = Blueprint('search_student', __name__)

@search_student_bp.route('/manage_students/search', methods=['GET'])
def search_students():
    query = request.args.get('query')

    # Perform a database query to retrieve students based on the search query
    students = Student.query.filter(Student.name.ilike(f'%{query}%')).all()

    # Render the template with the search results
    return render_template('manage_students.html', students=students)
