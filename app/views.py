from app import app
from flask import render_template, request, redirect, send_from_directory, Flask
import os

#app.config["IMAGE_UPLOADS"] = "/Users/marco.gonzalezortiz/Documents/Rakuten_Mobile/Marco/Learning/rmtopo/app/static"

@app.route("/")
def index():
         return render_template("public/index.html")

# @app.route("/admin/dashboard")
# def admin_dashboard():
#    return render_template("admin/dashboard.html")


# @app.route("/upload-image", methods=["GET , POST"])
# def upload_image():
#     if request.method == "POST":
#         if request.files:
#             image = request.files["image"]
#             image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
#             print("Image saved")
#             return redirect(request.url)
#     return render_template("public/core.html")

# #@app.route('/upload-image/<filename>')
# #def send_image(filename):
# #    return send_from_directory('images',filename)

# #if __name__ == "__main__":
# #    app.run(debug=True)


# import os
# from flask import Flask, render_template, request

# __author__ = 'ibininja'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    #return render_template("public/core.html")

# if __name__ == "__main__":
#     app.run(debug=True)