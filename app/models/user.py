# app/models/user.py

from app.extensions import db  # Assuming you have a db instance in your app setup

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date)  # Add this line for date of birth field

    password_hash = db.Column(db.String(128), nullable=False)


    administrators = db.relationship('Administrator', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

    # Additional fields and methods as needed
