# access_control.py

from flask import Blueprint, render_template

access_control_bp = Blueprint('access_control', __name__)

@access_control_bp.route('/access_control')
def access_control():
    return render_template('access_control.html')
