# app/models/assignment_submission.py
from app import db
from datetime import datetime
from .assignment import Assignment  # Import Assignment model

class AssignmentSubmission(db.Model):
    __tablename__ = 'assignment_submission'
    id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)  # Corrected foreign key column
    submission_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # Add any other fields you need for the assignment submission, such as file_path for uploaded files
    
    # Define relationships
    assignment = db.relationship('Assignment', backref='submissions')
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
