from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    psw = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.id}: {self.email}>"


class ProfileModel(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(500), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<Profile {self.id}: {self.name} {self.surname}>"


class MedicineModel(db.Model):
    __tablename__ = 'medicine'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    demand = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Medicine {self.id}: {self.name}>"


class PurchaseModel(db.Model):
    __tablename__ = 'purchase'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicine.id'))
    quantity = db.Column(db.Integer, nullable=False)
    total_amount = db.Column(db.DECIMAL(10, 2), nullable=False)
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Purchase {self.id}: {self.purchase_date}>"
