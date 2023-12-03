from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256

from app.models import *
from schemas import RegisterUserSchema, LoginUserSchema

blp = Blueprint("Auth", __name__, url_prefix="/auth", description="Authentication operations")

BLOCKLIST = set()


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(RegisterUserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.email == user_data["email"]).first():
            abort(409, message="A user with that email already exists.")

        user = UserModel(
            email=user_data["email"],
            psw=pbkdf2_sha256.hash(user_data["psw"])
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(LoginUserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.email == user_data["email"]).first()

        if user and pbkdf2_sha256.verify(user_data["psw"], user.psw):
            access_token = create_access_token(identity=user.id, fresh=True)
            return {"access_token": access_token}, 200

        abort(401, message="Invalid credentials.")

