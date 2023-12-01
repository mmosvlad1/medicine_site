from flask import Flask
from flask_restful import Api

# from app.models import *
from app.models import db
from app.urls import initialize_routes


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)


initialize_routes(api)

#
# @app.route('/')
# def hello_world():
#     return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
