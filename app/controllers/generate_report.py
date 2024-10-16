from flask import Blueprint, render_template

generate_report_bp = Blueprint('generate-report', __name__)

@generate_report_bp.route('/generate_report')
def generate_report():
    # Logic to retrieve and display user profile
    return render_template('generate_report.html')
