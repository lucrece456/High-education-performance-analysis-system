from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models.student import Student
from app import db
from sqlalchemy.sql.expression import or_
from datetime import datetime

# Create a Blueprint for managing students
manage_students_bp = Blueprint('manage_students', __name__)

# Define the route for managing students
@manage_students_bp.route('/students')
def manage_students():
    students = Student.query.all()
    return render_template('manage_students.html', students=students)

# Route for adding a new student
@manage_students_bp.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date_of_birth_str = request.form['date_of_birth']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']

        # Validate date_of_birth format
        try:
            date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d')
        except ValueError:
            flash('Invalid date format. Please enter the date in YYYY-MM-DD format.', 'error')
            return redirect(url_for('manage_students.manage_students'))

        # Create a new student instance
        new_student = Student(first_name=first_name, last_name=last_name, email=email,
                              date_of_birth=date_of_birth, address=address, username=username,
                              password=password)

        # Add the new student to the database session
        db.session.add(new_student)
        db.session.commit()

        # Flash message for success
        flash('Student added successfully!', 'success')

        # Redirect to the manage_students page
        return redirect(url_for('manage_students.manage_students'))











# Route for searching students
@manage_students_bp.route('/search_students', methods=['GET'])
def search_students():
    query = request.args.get('query')

    # Query the database for students with matching names or other relevant fields
    students = Student.query.filter(
        (Student.first_name.ilike(f'%{query}%')) |
        (Student.last_name.ilike(f'%{query}%'))
    ).all()

    if not students:
        flash('No students found with the provided search query.', 'info')

    return render_template('manage_students.html', students=students)





# Route for deleting a student
@manage_students_bp.route('/students/delete', methods=['POST'])
def delete_student():
    username = request.form.get('username')
    student = Student.query.filter_by(username=username).first()

    if student:
        db.session.delete(student)
        db.session.commit()
        flash('Student deleted successfully!', 'success')
    else:
        flash('Student not found.', 'error')

    return redirect(url_for('manage_students.manage_students'))

# Route for editing a student
@manage_students_bp.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    # Fetch the student from the database
    student = Student.query.get(student_id)

    if student is None:
        flash('Student not found.', 'error')
        return redirect(url_for('manage_students.manage_students_page'))

    if request.method == 'POST':
        # Update student details based on the form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']  # Retrieve email from form data
        date_of_birth_str  = request.form['date_of_birth']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']



        # Convert string representation of date to Python date object
        date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d')

 # Check if any changes have been made
        changes_made = False

        # Update student fields if changes are detected
        if first_name and student.first_name != first_name:
            student.first_name = first_name
            changes_made = True
        if last_name and student.last_name != last_name:
            student.last_name = last_name
            changes_made = True
        if email and student.email != email:
            student.email = email
            changes_made = True
        if date_of_birth and student.date_of_birth != date_of_birth:
            student.date_of_birth = date_of_birth
            changes_made = True
        if address and student.address != address:
            student.address = address
            changes_made = True
        if username and student.username != username:
            student.username = username
            changes_made = True
        if password and student.password != password:
            student.password = password
            changes_made = True

        # If changes were made, commit the changes to the database and display a message
        if changes_made:
            db.session.commit()
            flash('Changes saved. Database updated.', 'success')
        else:
            flash('No changes made.', 'info')

        return redirect(url_for('manage_students.manage_students'))

    # Render the edit student form
    return render_template('edit_student.html', student=student)