from app import db

class Feedback(db.Model):
    __tablename__ = 'feedback'
    feedback_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    feedback_text = db.Column(db.String(255))
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.id'))

    # Define relationship with Student
    student = db.relationship('Student', backref=db.backref('feedbacks', lazy=True))

    def __repr__(self):
        return f'<Feedback {self.feedback_id}>'
