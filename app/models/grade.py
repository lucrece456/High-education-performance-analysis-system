from app import db

class Grade(db.Model):
    __tablename__ = 'grade'
    grade_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.module_id'), nullable=False)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.id'), nullable=False)
    grade = db.Column(db.String(5))

    # Define the relationship between Student and Grade
    student = db.relationship('Student', backref=db.backref('grades', lazy=True))
    assignment = db.relationship('Assignment', backref=db.backref('grades_list', lazy=True))

    def __repr__(self):
        return f'<Grade {self.grade_id}>'
