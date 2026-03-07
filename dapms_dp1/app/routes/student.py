
from flask import Blueprint,render_template
bp=Blueprint("student",__name__)

@bp.route("/dashboard")
def dashboard():
    return render_template("student/dashboard.html")
