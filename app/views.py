from app import app
from flask import render_template, request, redirect, send_from_directory
import os

app.config["IMAGE_UPLOADS"] = "/Users/marco.gonzalezortiz/Documents/Rakuten_Mobile/Marco/Learning/rmtopo/app/static"

@app.route("/")
def index():
    return render_template("public/index.html")

#@app.route("/admin/dashboard")
#def admin_dashboard():
#    return render_template("admin/dashboard.html")

@app.route("/about")
def about():
    return "All about Flask"

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            print("Image saved")
            return redirect(request.url)
    return render_template("public/core.html")

#@app.route('/upload-image/<filename>')
#def send_image(filename):
#    return send_from_directory('images',filename)