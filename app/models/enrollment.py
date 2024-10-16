from app import db

class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), nullable=False)  # Fix typo in table name
    enrollment_date = db.Column(db.Date)

    # Define the relationship with Student
    student = db.relationship('Student', backref=db.backref('enrollments', lazy=True))
    # Define the relationship with Course
    course = db.relationship('Course', backref=db.backref('enrollments', lazy=True))

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id}, enrollment_date={self.enrollment_date})>"
