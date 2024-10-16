from flask import Blueprint, render_template
from datetime import datetime
from app.models.assignment import Assignment  # Import the Assignment model

assignment_bp = Blueprint('assignment', __name__)

@assignment_bp.route('/Assignments')
def assignments():  # Rename the function to match the route
    assignments = Assignment.query.all()  # Correct the model name to Assignment
    return render_template('Assignments.html', assignments=assignments)

def parse_datetime(datetime_str):
    try:
        # Specify the expected datetime format for SQLite (YYYY-MM-DD HH:MM:SS)
        expected_format = '%Y-%m-%d %H:%M:%S'
        
        # Parse the datetime string using the expected format
        parsed_datetime = datetime.strptime(datetime_str, expected_format)
        return parsed_datetime
    except ValueError as e:
        # Handle parsing errors by providing feedback or logging
        print(f"Error parsing datetime string '{datetime_str}': {e}")
        return None

