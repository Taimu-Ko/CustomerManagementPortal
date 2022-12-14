from flask import Flask, session, g
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user
from datetime import timedelta
import logging

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'KitsuneGrimm94'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
    db.init_app(app)
    
    logging.basicConfig(filename='app-debug.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s : %(message)s')
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    @app.before_request
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = app.config['PERMANENT_SESSION_LIFETIME']
        session.modified = True
        g.user = current_user
    
    @app.after_request
    def add_Security_headers(response):
        response.headers['Content-Security-Policy']='default-src \'self\'; style-src \'self\' https://fonts.googleapis.com \'unsafe-inline\'; font-src \'self\' https://ka-f.fontawesome.com; script-src \'self\' \'unsafe-inline\' https://kit.fontawesome.com; object-src \'self\'; connect-src \'self\' https://ka-f.fontawesome.com'
        return response
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created database')

