
from flask import Blueprint,render_template,request,redirect

bp=Blueprint("auth",__name__)

@bp.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        role=request.form.get("role")
        if role=="admin":
            return redirect("/admin/dashboard")
        if role=="teacher":
            return redirect("/teacher/dashboard")
        if role=="student":
            return redirect("/student/dashboard")
    return render_template("auth/login.html")
