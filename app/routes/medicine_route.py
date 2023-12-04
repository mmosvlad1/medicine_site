from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt_identity


from app.models import *
from schemas import MedicineSchema, DemandGetSchema, MakePurchaseSchema

blp = Blueprint("Medicine", __name__, url_prefix="/medicine", description="Operations on medicine")

BLOCKLIST = set()


@blp.route('/')
class MedicineList(MethodView):
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
        if not user:
            abort(404, message="User not found.")

        medicine = MedicineModel(name=new_data["name"],
                                 description=new_data["description"],
                                 quantity=new_data["quantity"],
                                 price=new_data["price"])

        db.session.add(medicine)
        db.session.commit()
        return MedicineSchema().dump(medicine)


@blp.route('/<int:medicine_id>')
class MedicineResource(MethodView):
    # @jwt_required()
    @blp.response(200, MedicineSchema)
    def get(self, medicine_id):
        medicine = MedicineModel.query.get_or_404(medicine_id)
        if not medicine:
            abort(404, message="Medicine not found.")
        return MedicineSchema().dump(medicine)

    @blp.arguments(MedicineSchema)
    @blp.response(200, MedicineSchema)
    @jwt_required()
    def put(self, update_data, medicine_id):
        medicine = MedicineModel.query.get_or_404(medicine_id)
        if not medicine:
            abort(404, message="Medicine not found.")

        for key, value in update_data.items():
            setattr(medicine, key, value)
        db.session.add(medicine)
        db.session.commit()
        return MedicineSchema().dump(medicine)

    @jwt_required()
    @blp.response(204)
    def delete(self, medicine_id):
        medicine = MedicineModel.query.get_or_404(medicine_id)
        if not medicine:
            abort(404, message="Medicine not found.")
        db.session.delete(medicine)
        db.session.commit()
        return '', 204


@blp.route('/<int:medicine_id>/demand')
class DemandResource(MethodView):
    # @jwt_required()
    @blp.response(200, DemandGetSchema)
    def get(self, medicine_id):
        medicine = MedicineModel.query.get_or_404(medicine_id)
        if not medicine:
            abort(404, message="Medicine not found.")
        get_demand = medicine.demand

        return DemandGetSchema().dump({"demand": get_demand})

    @blp.response(200, DemandGetSchema)
    @jwt_required()
    def put(self, medicine_id):
        medicine = MedicineModel.query.get_or_404(medicine_id)
        if not medicine:
            abort(404, message="Medicine not found.")

        medicine.demand += 1
        get_demand = medicine.demand

        db.session.add(medicine)
        db.session.commit()
        return DemandGetSchema().dump({"demand": get_demand})

    @jwt_required()
    @blp.response(204, DemandGetSchema)
    def delete(self, medicine_id):
        medicine = MedicineModel.query.get_or_404(medicine_id)
        if not medicine:
            abort(404, message="Medicine not found.")

        medicine.demand -= 1
        get_demand = medicine.demand

        db.session.add(medicine)
        db.session.commit()
        return DemandGetSchema().dump({"demand": get_demand})


@blp.route('/<int:medicine_id>/purchase')
class MedicineList(MethodView):
    @jwt_required()
    @blp.arguments(MakePurchaseSchema)
    @blp.response(201, MakePurchaseSchema)
    def post(self, new_data, medicine_id):
        user_id = get_jwt_identity()
        user = UserModel.query.get_or_404(user_id)
        if not user:
            abort(404, message="User not found.")

        medicine = MedicineModel.query.get_or_404(medicine_id)
        if not medicine:
            abort(404, message="Medicine not found.")

        purchase = PurchaseModel(user_id=user.id,
                                 medicine_id=medicine.id,
                                 quantity=new_data["quantity"],
                                 total_amount=new_data["total_amount"])

        db.session.add(purchase)
        db.session.commit()
        return MakePurchaseSchema().dump(purchase)
