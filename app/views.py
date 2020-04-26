from app import app
from flask import render_template, request, redirect, send_from_directory, Flask,url_for, jsonify
# from sqlalquemy import create_engine
# from sqlalquemy.orm import scoped_session, sessionmaker
from werkzeug.utils import secure_filename
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

@app.route("/")
def index():
    target = os.path.join(APP_ROOT, 'images/')
    images = []
    for filename in os.listdir(target):
        path = os.path.join(target, filename)
        if os.path.isfile(path):
            images.append(target + filename)
    # list_images = [{'name': 'Home', 'url': 'https://example.com/1'},
    #                        {'name': 'About', 'url': 'https://example.com/2'},
    #                        {'name': 'Pics', 'url': 'https://example.com/3'}]
    return render_template("public/index.html", list_images=images)

@app.route("/about")
def about():
    return "All about Flask"

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
    
@app.route("/listimages", methods=['GET'])
def getimages():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if request.method == "GET":
        images = []
        for filename in os.listdir(target):
            path = os.path.join(target, filename)
            if os.path.isfile(path):
                images.append(filename)
        return jsonify(images)

    return render_template('public/index.html',
                           nav=images,
                           title="Jinja Demo Site",
                           description="Smarter page templates \
                                with Flask & Jinja.")

if __name__ == "__main__":
    app.run(debug=True)