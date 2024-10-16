from flask import Blueprint, render_template, session, redirect, url_for



# Administrator Dashboard Blueprint
administrator_dashboard_bp = Blueprint('administrator_dashboard', __name__, url_prefix='/admin')

@administrator_dashboard_bp.route('/dashboard')
def dashboard():
    if session.get('role') == 'administrator':
        first_name = session.get('first_name')
        return render_template('dashboard/administrator_dashboard.html', first_name=first_name)
    else:
        return redirect(url_for('login.login'))