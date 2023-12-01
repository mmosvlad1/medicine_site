from app.views import MedicinesResource, MedicineResource, DemandsResource, UserPurchasesResource, PurchaseResource, PurchaseItemResource


def initialize_routes(api):
    api.add_resource(MedicinesResource, '/medicines')
    api.add_resource(MedicineResource, '/medicines/<int:medicineId>')
    api.add_resource(DemandsResource, '/demands')
    api.add_resource(UserPurchasesResource, '/users/<int:userId>/purchases')
    api.add_resource(PurchaseResource, '/purchase')
    api.add_resource(PurchaseItemResource, '/purchase/<int:purchaseId>/items/<int:itemId>')
