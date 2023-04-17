# # import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# user = 'root'
# password = ''
# host = '127.0.0.1'
# port = 3306
# database = 'Library'

# # create a new instance of Flask and store it in app
# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
#     user, password, host, port, database)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:password@host/database_name"
# app.config['SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://' + getenv('MYSQL_USER') + ':' + getenv('MYSQL_PASSWORD') + '@' + getenv('MYSQL_HOST') + '/' + getenv('MYSQL_DB'))
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


# # link our app to the persistence layer
# db = SQLAlchemy(app)