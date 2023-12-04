from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from app.models import *
from schemas import UserGetSchema

blp = Blueprint("User", __name__, url_prefix="/users", description="User operations")


@blp.route('/')
class UserList(MethodView):
    @blp.response(200, UserGetSchema(many=True))
    def get(self):
        users = UserModel.query.all()
        return UserGetSchema(many=True).dump(users)


@blp.route('/<int:user_id>')
class UserResource(MethodView):
    @blp.response(200, UserGetSchema)
    def get(self, user_id):
        medicine = UserModel.query.get_or_404(user_id)
        if not medicine:
            abort(404, message="User not found.")
        return UserGetSchema().dump(medicine)
