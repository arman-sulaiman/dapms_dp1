
from flask import Flask
from .routes.auth import bp as auth_bp
from .routes.admin import bp as admin_bp
from .routes.teacher import bp as teacher_bp
from .routes.student import bp as student_bp

def create_app():
    app=Flask(__name__)
    app.secret_key="123"
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp,url_prefix="/admin")
    app.register_blueprint(teacher_bp,url_prefix="/teacher")
    app.register_blueprint(student_bp,url_prefix="/student")
    return app
