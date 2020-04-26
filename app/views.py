from app import app
from flask import render_template, request, redirect, send_from_directory, Flask,url_for, jsonify,make_response
from werkzeug.utils import secure_filename
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

@app.route("/")
def index():
    return render_template("public/index.html")

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
    images_path = []
    images_name = []
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    for filename in os.listdir(target):
        path = os.path.join(target, filename).replace("\\","/")
        if os.path.isfile(path):
            images_path.append(path + filename)
            images_name.append(filename)
    print(target)
    print(path)
    zipbObj = zip(images_name, images_path)
    dictOimages = dict(zipbObj)
    headers = {"Image_Name": "Image_path"}
    return make_response(jsonify(dictOimages), 200, headers)

if __name__ == "__main__":
    app.run(debug=True)