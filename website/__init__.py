from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'to do flask app'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://epiz_33297024:m0G8cGJpkai9@sql109.epizy.com/epiz_33297024_flasktodolist4'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    
    
    
    from .models import User,List
    create_database(app)

    login_manger = LoginManager()
    login_manger.login_view = 'auth.login'
    login_manger.init_app(app)
        
    @login_manger.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app
    
def create_database(app):
    db.create_all(app=app)
    print('Created Database!')

