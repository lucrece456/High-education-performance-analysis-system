 # app/controllers/manage_modules.py

from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.models.module import Module
from app.models.course import Course
from app import db

manage_modules_bp = Blueprint('manage_modules', __name__)

@manage_modules_bp.route('/modules', methods=['GET'])
def get_modules():
    modules = Module.query.all()
    return render_template('manage_modules.html', modules=modules)

@manage_modules_bp.route('/modules/add', methods=['POST'])
def add_module():
    module_name = request.form['module_name']
    course_id = request.form['course_id']
    module_code = request.form['module_code']

    course = Course.query.get(course_id)
    if not course:
        flash('Invalid course ID. Module could not be added.')
        return redirect(url_for('manage_modules.get_modules'))

    module = Module(module_name=module_name, course_id=course_id, module_code=module_code)
    db.session.add(module)
    db.session.commit()

    flash('Module added successfully.')
    return redirect(url_for('manage_modules.get_modules'))

@manage_modules_bp.route('/modules/edit/<int:module_id>', methods=['GET', 'POST'])
def edit_module(module_id):
    module = Module.query.get(module_id)
    if not module:
        flash('Module not found.')
        return redirect(url_for('manage_modules.get_modules'))

    if request.method == 'POST':
        module_name = request.form['module_name']
        course_id = request.form['course_id']
        module_code = request.form['module_code']

        course = Course.query.get(course_id)
        if not course:
            flash('Invalid course ID. Module could not be updated.')
            return redirect(url_for('manage_modules.get_modules'))

        module.module_name = module_name
        module.course_id = course_id
        module.module_code = module_code

        db.session.commit()
        flash('Module updated successfully.')
        return redirect(url_for('manage_modules.get_modules'))

    return render_template('edit_module.html', module=module)

@manage_modules_bp.route('/modules/delete/<int:module_id>', methods=['POST'])
def delete_module(module_id):
    module = Module.query.get(module_id)
    if not module:
        flash('Module not found.')
        return redirect(url_for('manage_modules.get_modules'))

    db.session.delete(module)
    db.session.commit()
    flash('Module deleted successfully.')
    return redirect(url_for('manage_modules.get_modules'))

@manage_modules_bp.route('/modules/search', methods=['GET'])
def search_modules():
    query = request.args.get('query')
    modules = Module.query.filter(Module.module_name.ilike(f'%{query}%')).all()
    return render_template('manage_modules.html', modules=modules)
