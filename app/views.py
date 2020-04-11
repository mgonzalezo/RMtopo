from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return "All about Flask"

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")