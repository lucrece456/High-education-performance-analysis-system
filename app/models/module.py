from app import db

class Module(db.Model):
    __tablename__ = 'modules'
    module_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    module_name = db.Column(db.String(30), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), nullable=False)
    module_code = db.Column(db.String(20))
    course_code = db.Column(db.String(20))  # Add course code attribute
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.teacher_id'), nullable=False)

    # Define relationships
    assignments = db.relationship('Assignment', backref='module_parent', lazy=True)
    teacher = db.relationship('Teacher', backref=db.backref('modules', lazy=True))


    def serialize(self):
        return {
            'module_id': self.module_id,
            'module_name': self.module_name,
            'course_id': self.course_id,
            'module_code': self.module_code
            # Include other attributes as needed
        }