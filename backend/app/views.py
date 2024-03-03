from flask import request
from flask_restful import Resource

from app.models import Medicine, db, Demand, User, Purchase, PurchaseItem


class MedicinesResource(Resource):
    def get(self):
        medicines = Medicine.query.all()
        return [medicine.serialize() for medicine in medicines], 200

    def post(self):
        data = request.json
        new_medicine = Medicine(**data)
        db.session.add(new_medicine)
        db.session.commit()
        return new_medicine.serialize(), 201


class MedicineResource(Resource):
    def get(self, medicineId):
        medicine = Medicine.query.get(medicineId)
        if not medicine:
            return {'error': 'Medicine not found'}, 404
        return medicine.serialize(), 200

    def put(self, medicineId):
        medicine = Medicine.query.get(medicineId)
        if not medicine:
            return {'error': 'Medicine not found'}, 404

        data = request.json
        for key, value in data.items():
            setattr(medicine, key, value)

        db.session.commit()
        return medicine.serialize(), 200

    def delete(self, medicineId):
        medicine = Medicine.query.get(medicineId)
        if not medicine:
            return {'error': 'Medicine not found'}, 404

        db.session.delete(medicine)
        db.session.commit()
        return '', 204


class DemandsResource(Resource):
    def post(self):
        data = request.json
        demand = Demand(**data)
        db.session.add(demand)
        db.session.commit()
        return demand.serialize(), 201


class UserPurchasesResource(Resource):
    def get(self, userId):
        user = User.query.get(userId)
        if not user:
            return {'error': 'User not found'}, 404

        purchases = Purchase.query.filter_by(profile_id=user.profile.id).all()
        return [purchase.serialize() for purchase in purchases], 200


class PurchaseResource(Resource):
    def post(self):
        data = request.json
        purchase = Purchase(profile_id=data['profile_id'], total_amount=data['total_amount'])

        for item_data in data['items']:
            item = PurchaseItem(**item_data)
            purchase.items.append(item)

        db.session.add(purchase)
        db.session.commit()
        return purchase.serialize(), 201


class PurchaseItemResource(Resource):
    def get(self, purchaseId, itemId):
        item = PurchaseItem.query.filter_by(purchase_id=purchaseId, id=itemId).first()
        if not item:
            return {'error': 'Purchase item not found'}, 404
        return item.serialize(), 200

    def put(self, purchaseId, itemId):
        item = PurchaseItem.query.filter_by(purchase_id=purchaseId, id=itemId).first()
        if not item:
            return {'error': 'Purchase item not found'}, 404

        data = request.json
        for key, value in data.items():
            setattr(item, key, value)

        db.session.commit()
        return item.serialize(), 200

    def delete(self, purchaseId, itemId):
        item = PurchaseItem.query.filter_by(purchase_id=purchaseId, id=itemId).first()
        if not item:
            return {'error': 'Purchase item not found'}, 404

        db.session.delete(item)
        db.session.commit()
        return '', 204
