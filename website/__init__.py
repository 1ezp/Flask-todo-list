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
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vrkudzfbaohiop:43ce417124bbc86b0cac0eec7cf54387e3bb726ace32bcd9fa5716e3c708390a@ec2-52-73-155-171.compute-1.amazonaws.com:5432/ddrdi730dqfa65'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    
    
    
    from .models import User,List
    #create_database(app)

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