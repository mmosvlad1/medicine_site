class Config:
    API_TITLE = "Pharmacy REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    JWT_SECRET_KEY = "vlad"
    SECRET_KEY = "zH81h7C0JOytvq26_hw1P3VsSTCKm7zdu6hc-woHNnk"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    JWT_SECRET_KEY = "vlad"
    SECRET_KEY = "zH81h7C0JOytvq26_hw1P3VsSTCKm7zdu6hc-woHNnk"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
