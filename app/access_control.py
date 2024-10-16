# access_control.py

from flask import abort, session

# Define a decorator to check user roles
def role_required(role):
    def decorator(view_func):
        def wrapper(*args, **kwargs):
            # Check if the user has the required role
            if session.get('role') != role:
                # If not, abort with 403 Forbidden error
                abort(403)
            # If the user has the required role, proceed with the view function
            return view_func(*args, **kwargs)
        return wrapper
    return decorator
