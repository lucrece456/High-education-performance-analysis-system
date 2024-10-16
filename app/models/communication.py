from app import db
from sqlalchemy.orm import relationship

class Communication(db.Model):
    __tablename__ = 'communication'
    communication_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    receiver_id = db.Column(db.Integer, nullable=False)
    receiver_type = db.Column(db.String(10), nullable=False)  # 'teacher' or 'administrator'
    date = db.Column(db.Date)
    message = db.Column(db.String(70))

    sender = relationship("Student", foreign_keys=[sender_id])
    receiver_teacher = relationship("Teacher", foreign_keys=[receiver_id], backref="received_messages", primaryjoin="and_(Communication.receiver_id == Teacher.teacher_id, Communication.receiver_type == 'teacher')", uselist=False)
    receiver_administrator = relationship("Administrator", foreign_keys=[receiver_id], backref="received_messages", primaryjoin="and_(Communication.receiver_id == Administrator.id, Communication.receiver_type == 'administrator')", uselist=False)
