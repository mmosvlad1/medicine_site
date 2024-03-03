from marshmallow import Schema, fields, validate


class RegisterUserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    psw = fields.Str(required=True, validate=validate.Length(min=8))
    name = fields.Str(required=True, validate=validate.Length(max=50))
    surname = fields.Str(required=True, validate=validate.Length(max=50))
    address = fields.Str(required=True, validate=validate.Length(max=500))
    role_id = fields.Int(default=1)
    date = fields.DateTime(dump_only=True)


class LoginUserSchema(Schema):
    email = fields.Email(required=True)
    psw = fields.Str(required=True)


class MedicineSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=100))
    description = fields.Str(required=True, validate=validate.Length(max=500))
    quantity = fields.Int(required=True, validate=validate.Range(min=1))
    price = fields.Decimal(required=True, as_string=True, validate=validate.Range(min=1))
    demand = fields.Int(dump_only=True)


class DemandGetSchema(Schema):
    demand = fields.Int()


class UserGetSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    surname = fields.Str()
    address = fields.Str()
    email = fields.Str()
    role_id = fields.Int(dump_only=True)


class MakePurchaseSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(dump_only=True)
    medicine_id = fields.Int(dump_only=True)
    quantity = fields.Int(required=True, validate=validate.Range(min=1))
    total_amount = fields.Decimal(dump_only=True)
    purchase_date = fields.Str(dump_only=True)

