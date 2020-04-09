from flask import render_template, request, redirect
from werkzeug.utils import secure_filename
from flask import Flask
import os

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/Upload_File", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            print(image)

            return redirect(request.url)


    return render_template("index.html")



#Execute Code
app.run()