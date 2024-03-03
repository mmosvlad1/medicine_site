from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models import *
from schemas import UserGetSchema

blp = Blueprint("User", __name__, url_prefix="/api/users", description="User operations")


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
        user = UserModel.query.get_or_404(user_id)
        if not user:
            abort(404, message="User not found.")
        return UserGetSchema().dump(user)

    @blp.arguments(UserGetSchema)
    @blp.response(200, UserGetSchema)
    @jwt_required()
    def put(self, update_data, user_id):
        current_user_id = get_jwt_identity()
        current_user = UserModel.query.get_or_404(current_user_id)
        if not current_user or current_user.role_id != 2:
            abort(403, message="Permission denied.")

        for key, value in update_data.items():
            setattr(current_user, key, value)

        db.session.add(current_user)
        db.session.commit()
        return UserGetSchema().dump(current_user)

    @jwt_required()
    @blp.response(204)
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        if not user:
            abort(404, message="User not found.")
        db.session.delete(user)
        db.session.commit()
        return '', 204