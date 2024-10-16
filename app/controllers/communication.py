# app/controllers/communication.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models.teacher import Teacher
from app.models.administrator import Administrator
from app.models.student import Student
from app.models.communication import Communication
from app import db
from datetime import datetime

communication_bp = Blueprint('communication', __name__)

@communication_bp.route('/communications', methods=['GET'])
def get_communications():
    # Query the database to get teacher and administrator usernames
    teachers = Teacher.query.all()
    administrators = Administrator.query.all()

    # Extract usernames from the teacher and administrator objects
    teacher_usernames = [teacher.username for teacher in teachers]
    administrator_usernames = [administrator.username for administrator in administrators]

    return render_template('communication.html', teacher_usernames=teacher_usernames, administrator_usernames=administrator_usernames)

@communication_bp.route('/send_message', methods=['GET', 'POST'])
def send_message():
    sender_id = session.get('user_id')  # Corrected to use 'user_id' session variable
    recipient = request.form.get('recipient')
    message = request.form.get('message')

    # Determine the receiver type and ID
    if Teacher.query.filter_by(username=recipient).first():
        receiver_type = 'teacher'
        receiver_id = Teacher.query.filter_by(username=recipient).first().teacher_id
    elif Administrator.query.filter_by(username=recipient).first():
        receiver_type = 'administrator'
        receiver_id = Administrator.query.filter_by(username=recipient).first().id
    else:
        # Handle case when recipient is not found
        return redirect(url_for('communication.get_communications'))

    # Store the message in the database
    new_message = Communication(sender_id=sender_id, receiver_id=receiver_id, receiver_type=receiver_type, date=datetime.now(), message=message)
    db.session.add(new_message)
    db.session.commit()

    return redirect(url_for('communication.get_communications'))


@communication_bp.route('/teacher_messages', methods=['GET', 'POST'])
def teacher_messages():
    # Get the current teacher's ID (you need to implement session handling for teachers)
    teacher_id = session.get('teacher_id')

    # Query the database for messages where the teacher is the recipient
    messages = Communication.query.filter_by(receiver_id=teacher_id, receiver_type='teacher').all()

    print(messages)  # Add this line for debugging purposes

    return render_template('teacher_messages.html', messages=messages)

@communication_bp.route('/administrator_messages', methods=['GET', 'POST'])
def administrator_messages():
    # Get the current administrator's ID (you need to implement session handling for administrators)
    administrator_id = session.get('administrator_id')

    # Query the database for messages where the administrator is the recipient
    messages = Communication.query.filter_by(receiver_id=administrator_id, receiver_type='administrator').all()

    print(messages)  # Add this line for debugging purposes

    return render_template('administrator_messages.html', messages=messages)