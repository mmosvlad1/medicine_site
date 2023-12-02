import connexion
from flask import Flask
from flask_restful import Api
from app.models import db
from app.urls import initialize_routes
from connexion.resolver import RestyResolver


app = connexion.App(__name__, specification_dir='swagger/')
app.add_api('pharmacy_api.yaml', resolver=RestyResolver('api'))

# Ініціалізуємо Flask та встановлюємо параметри для бази даних
flask_app = app.app
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Ініціалізуємо SQLAlchemy та Api
db.init_app(flask_app)
api = Api(flask_app)

# Ініціалізуємо маршрути
initialize_routes(api)

if __name__ == '__main__':
    app.run()
