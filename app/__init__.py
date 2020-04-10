from flask import Flask

app = Flask(__name__)

from app import views #Using this, we can import multiple python files into our Flask app 
from app import admin_views
