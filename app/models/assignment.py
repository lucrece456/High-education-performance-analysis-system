# app/models/assignment.py
from app import db

class Assignment(db.Model):
    __tablename__ = 'assignment'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.module_id'), nullable=False)
    schedule = db.Column(db.DateTime, nullable=False)
    students = db.Column(db.String(50), nullable=False)
    grading = db.Column(db.String(50), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text, nullable=False)
    attachment = db.Column(db.String(100), nullable=True)

    # Define backref to access module from assignment
    module = db.relationship('Module', backref='assignments_list')

    def __repr__(self):
        return f'<Assignment {self.id} - {self.title}>'
