from app import app
from flask import render_template, request, redirect, send_from_directory, Flask,url_for
from werkzeug.utils import secure_filename
import os

#app.config["IMAGE_UPLOADS"] = "/Users/marco.gonzalezortiz/Documents/Rakuten_Mobile/Marco/Learning/rmtopo/app/static"

@app.route("/")
def index():
         return render_template("public/index.html")

@app.route("/about")
def about():
    return "All about Flask"

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
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

def allowed_image(filename):
    
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

def allowed_image_filesize(filesize):
    
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                print("No filename")
                #return redirect(request.url)
                return redirect(url_for('index'))

            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                image.save(os.path.join(target, filename))
                print("Image saved")
                return redirect(url_for('index'))
            else:
                print("That file extension is not allowed")
                return redirect(url_for('index'))

    return render_template("public/index.html")
    
if __name__ == "__main__":
    app.run(debug=True)