from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt_identity


from app.models import *
from schemas import MedicineSchema

blp = Blueprint("Medicine", __name__, url_prefix="/medicine", description="Operations on medicine")

BLOCKLIST = set()


@blp.route('/')
class EventsList(MethodView):
    @blp.response(200, MedicineSchema(many=True))
    def get(self):
        medicine = MedicineModel.query.all()
        return MedicineSchema(many=True).dump(medicine)

    @jwt_required()
    @blp.arguments(MedicineSchema)
    @blp.response(201, MedicineSchema)
    def post(self, new_data):
        user_id = get_jwt_identity()
        user = UserModel.query.get_or_404(user_id)
        datetime_object = datetime.strptime(new_data["date"], "%Y-%m-%dT%H:%M:%S")
        if not user:
            abort(404, message="User not found.")
        medicine = MedicineModel(name=new_data["name"], description=new_data["description"],
                                 quantity=new_data["quantity"], price=new_data["price"])
        db.session.add(medicine)
        db.session.commit()
        return MedicineSchema().dump(medicine), 201
