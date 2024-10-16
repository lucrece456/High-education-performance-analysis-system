from flask import Blueprint, request, render_template
from app.models.student import Student

# Create a Blueprint for the search routes
search_bp = Blueprint('search', __name__)

# Define the route for searching students
@search_bp.route('/search', methods=['GET'])
def search_students():
    query = request.args.get('query')  # Get the search query from the request

    if query:
        # Construct a database query to filter students based on the search query
        students = Student.query.filter(
            (Student.username.ilike(f'%{query}%')) |  # Filter by username
            (Student.email.ilike(f'%{query}%'))  # Filter by email (add more filters as needed)
        ).all()

        # Render the search results template with the filtered students
        return render_template('search_results.html', students=students)
    else:
        # Handle case where no search query is provided
        return render_template('search_results.html', students=[])

