import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from .db_init import create_database

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'This is my very secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ.get('DB_USERNAME')}:{os.environ.get('DB_PASSWORD')}@localhost/{os.environ.get('DB_NAME')}"

    from .create_db import User, Note

    db.init_app(app)
    create_database()
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


