from app import app
from flask import render_template, request, redirect, send_from_directory, Flask

@app.route("/admin/dashboard")
def admin_dashboard():
   return render_template("admin/dashboard.html")