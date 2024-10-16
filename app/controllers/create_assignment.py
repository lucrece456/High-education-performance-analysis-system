## app/controllers/create_assignment.py
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models.assignment import Assignment
from app.models.module import Module  # Import Module model
from app import db

create_assignment_bp = Blueprint('create_assignment', __name__)

@create_assignment_bp.route('/create_assignment', methods=['GET', 'POST'])
def create_assignment():
    if request.method == 'POST':
        # Get assignment details from the form
        module_id = request.form.get('module')  # Assuming the value of the selected option is the module ID
        title = request.form.get('title')
        schedule = request.form.get('schedule')
        students = request.form.get('students')
        grading = request.form.get('grading')
        due_date = request.form.get('due_date')
        description = request.form.get('description')
        attachment = request.files.get('attachment')


         # Retrieve the selected module object from the database
        module = Module.query.get(module_id)

        # Create an Assignment object and save it to the database
        assignment = Assignment(
            module_name=modules.module_name,
            title=title,
            schedule=schedule,
            students=students,
            grading=grading,
            due_date=due_date,
            description=description,
            attachment=attachment.filename if attachment else None
        )

        try:
            # Save the assignment details to the database
            db.session.add(assignment)
            db.session.commit()
            flash('Assignment created successfully.', 'success')
            return redirect(url_for('create_assignment.create_assignment'))
        except Exception as e:
            flash(f'Error creating assignment: {str(e)}', 'error')
            db.session.rollback()

    # If request method is GET, render the create assignment form
    modules = Module.query.all()  # Fetch all modules from the database
    return render_template('create_assignment.html', modules=modules)
