from flask import Flask
from app.extensions import db
from flask_migrate import Migrate


from .controllers.home import home_bp
from .controllers.login import login_bp
from .controllers.administrator import administrator_dashboard_bp
from .controllers.student_dashboard import student_dashboard_bp
from .controllers.teacher_dashboard import teacher_dashboard_bp
from .controllers.view_grades import view_grades_bp
from .controllers.access_course_materials import access_course_materials_bp
from .controllers.view_attendance import view_attendance_bp
from .controllers.provide_feedback import provide_feedback_bp
from .controllers.view_performance_analysis import view_performance_analysis_bp
from .controllers.view_profile import view_profile_bp
from .controllers.create_assignment import create_assignment_bp
from .controllers.attendance_tracking import attendance_tracking_bp
from .controllers.input_grades import input_grades_bp
from .controllers.give_feedback import give_feedback_bp
from .controllers.generate_report import generate_report_bp
from .controllers.communication import communication_bp
from .controllers.view_performance_analysis import view_performance_analysis_bp
from .controllers.access_control import access_control_bp
from .controllers.access_users_data import create_user_bp, edit_user_bp, delete_user_bp
from .controllers.manage_students import manage_students_bp
from .controllers.manage_courses import manage_courses_bp
from .controllers.manage_modules import manage_modules_bp
from .controllers.search_controller import search_bp
from .controllers.assignment import assignment_bp
from .controllers.module_controller import module_bp
from .controllers.grade_controller import grade_bp
from .controllers.enrollment import enrollment_bp
from .controllers.admin import admin_bp






def create_app():
    app = Flask(__name__, template_folder='views/templates', static_folder='views/static')
    app.secret_key = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite'

    # Initialize SQLAlchemy with the Flask application
    db.init_app(app)
    migrate = Migrate(app, db)



    # Register Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(administrator_dashboard_bp)
    app.register_blueprint(student_dashboard_bp)
    app.register_blueprint(teacher_dashboard_bp)
    app.register_blueprint(view_grades_bp)
    app.register_blueprint(access_course_materials_bp)
    app.register_blueprint(view_attendance_bp)
    app.register_blueprint(provide_feedback_bp)
    app.register_blueprint(view_performance_analysis_bp)
    app.register_blueprint(view_profile_bp)
    app.register_blueprint(create_assignment_bp)
    app.register_blueprint(attendance_tracking_bp)
    app.register_blueprint(input_grades_bp)
    app.register_blueprint(give_feedback_bp)
    app.register_blueprint(generate_report_bp)
    app.register_blueprint(communication_bp)
    app.register_blueprint(access_control_bp)
    app.register_blueprint(create_user_bp)
    app.register_blueprint(edit_user_bp)
    app.register_blueprint(delete_user_bp)
    app.register_blueprint(manage_students_bp)
    app.register_blueprint(manage_courses_bp)
    app.register_blueprint(manage_modules_bp, url_prefix="/admin")
    app.register_blueprint(search_bp)
    app.register_blueprint(assignment_bp)
    app.register_blueprint(module_bp)
    app.register_blueprint(grade_bp)
    app.register_blueprint(enrollment_bp)
    app.register_blueprint(admin_bp)



    with app.app_context():
        db.create_all()



    return app
