from app import db

# Define the association table
course_module = db.Table('course_module',
    db.Column('course_id', db.Integer, db.ForeignKey('courses.course_id')),
    db.Column('module_id', db.Integer, db.ForeignKey('modules.module_id'))
)

class Course(db.Model):
    __tablename__ = 'courses'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String(30), nullable=False)
    course_code = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(62))

    # Define the relationship with modules
    modules = db.relationship('Module', secondary=course_module, backref='courses')
    

    def serialize(self):
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            # Include other attributes as needed
        }