from flask import Blueprint, render_template

assignment_submission_bp = Blueprint('assignment_submission', __name__)

@assignment_submission_bp.route('/assignment_submission')
def assignment_submission():
    return render_template('assignment_submission.html')
