from flask import Blueprint, render_template
from app.models.assignment import Assignment
from app.models.module import Module


access_course_materials_bp = Blueprint('access_course_materials', __name__)

@access_course_materials_bp.route('/access-course-materials')
def access_course_materials():
    modules = Module.query.all()
    assignments = Assignment.query.all()
    
    return render_template('access_course_materials.html', modules=modules, assignments=assignments)