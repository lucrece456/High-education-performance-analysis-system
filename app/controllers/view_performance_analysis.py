# app/controllers/view_performance_analysis.py
from flask import Blueprint, render_template
from app.models.grade import Grade
from app.models.student import Student
from app import db
import plotly.graph_objs as go
import json

view_performance_analysis_bp = Blueprint('view_performance_analysis', __name__)

@view_performance_analysis_bp.route('/view_performance_analysis')
def view_performance_analysis():
    students = Student.query.all()
    student_data = []

    for student in students:
        grades = Grade.query.filter_by(student_id=student.student_id).all()
        performance_level = calculate_performance_level(grades)
        student_data.append({
            'name': f"{student.first_name} {student.last_name}",
            'performance_level': performance_level
        })

    performance_level_chart_data = create_performance_level_chart(student_data)
    performance_level_chart_json_str = json.dumps(performance_level_chart_data)

    return render_template('view_performance_analysis.html', performance_level_chart_json=performance_level_chart_json_str)

def calculate_performance_level(grades):
    if not grades:
        return 'No grades available'

    average_grade = sum(int(grade.grade) for grade in grades) / len(grades)
    if average_grade >= 90:
        return 'Excellent'
    elif average_grade >= 80:
        return 'Good'
    elif average_grade >= 70:
        return 'Average'
    else:
        return 'Below Average'

def create_performance_level_chart(student_data):
    x_values = [student['name'] for student in student_data]
    y_values = [student['performance_level'] for student in student_data]

    return {'x': x_values, 'y': y_values}
