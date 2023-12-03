from marshmallow import Schema, fields, validate


class RegisterUserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    psw = fields.Str(required=True, validate=validate.Length(min=8))
    date = fields.DateTime(dump_only=True)


class CreateProfileSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=50))
    surname = fields.Str(required=True, validate=validate.Length(max=50))
    address = fields.Str(required=True, validate=validate.Length(max=500))
    user_id = fields.Int()


class LoginUserSchema(Schema):
    email = fields.Email(required=True)
    psw = fields.Str(required=True)


class MedicineSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=100))
    description = fields.Str(required=True, validate=validate.Length(max=500))
    quantity = fields.Int(required=True)
    price = fields.Decimal(required=True, as_string=True)
#
#
# class PurchaseItemSchema(Schema):
#     id = fields.Int(dump_only=True)
#     purchase_id = fields.Int()
#     medicine_id = fields.Int()
#     quantity = fields.Int(required=True)
#     price = fields.Decimal(required=True, as_string=True)
#
#
# class PurchaseSchema(Schema):
#     id = fields.Int(dump_only=True)
#     profile_id = fields.Int()
#     total_amount = fields.Decimal(required=True, as_string=True)
#     purchase_date = fields.DateTime(dump_only=True)
#     items = fields.Nested(PurchaseItemSchema(), many=True)
#
#
# class DemandSchema(Schema):
#     id = fields.Int(dump_only=True)
#     medicine_id = fields.Int()
#     quantity = fields.Int(required=True)
