from flask import Blueprint
from app import db
from app.models.attendance import Attendance

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/attendance')
def get_attendance():
    # Retrieve attendance data from the database
    attendance_data = Attendance.query.all()

    # Format the data as needed (example: converting dates to strings)
    formatted_data = []
    for attendance in attendance_data:
        formatted_data.append({
            'attendance_id': attendance.attendance_id,
            'student_id': attendance.student_id,
            'date': attendance.date.strftime('%Y-%m-%d'),
            'status': attendance.status
        })
@attendance_bp.route('/attendance/<int:student_id>')
def view_attendance(student_id):
    # Retrieve attendance data for the specified student ID
    attendance_data = models.Attendance.query.filter_by(student_id=student_id).all()

    # Pass the attendance data to the template
    return render_template('attendance.html', attendance_data=attendance_data)

    # Return the formatted data as JSON
    return jsonify(formatted_data)

@attendance_bp.route('/insert-attendance')
def insert_attendance():
    # Insert sample data into the attendance table
    # For demonstration purposes, you can insert hardcoded data
    # Replace this with actual data from your application logic
    sample_attendance = Attendance(student_id=1, date=datetime.now().date(), status='Present')
    db.session.add(sample_attendance)
    db.session.commit()

    return 'Sample attendance data inserted successfully'
