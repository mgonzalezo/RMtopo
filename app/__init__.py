from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

db = SQLAlchemy()
login_manager = LoginManager()

from app import views #Using this, we can import multiple python files into our Flask app 
from app import admin_views

def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth

        # Register Blueprints
        
        # app.register_blueprint(routes.main_bp)
        # app.register_blueprint(auth.auth_bp)

        # Create Database Models
        db.create_all()

        return app