from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from app.models.module import Module
from app.models.course import Course


module_bp = Blueprint('module', __name__)

@module_bp.route('/modules', methods=['GET'])
def get_modules():
    modules = Module.query.all()
    courses = Course.query.all()
    return render_template('module.html', modules=modules, courses=courses)

@module_bp.route('/modules/<int:module_id>/create_assignment', methods=['GET', 'POST'])
def create_assignment(module_id):
    # Logic to fetch the module with the specified ID
    module = Module.query.get(module_id)
    
    # Check if the module exists
    if not module:
        # Handle the case where the module does not exist (optional)
        return render_template('module_not_found.html')

    # Render the create_assignment template and pass the module_id
    return render_template('create_assignment.html', module=module)
