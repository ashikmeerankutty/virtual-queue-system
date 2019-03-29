from app import db
from app.models.base import BaseModel


class BookingModel(BaseModel):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(255), index=True)
    token = db.Column(db.String(255), index=True, unique=True)

    def to_dict(self):
        data = {
            'id': self.id,
            'phone': self.phone,
            'token': self.token,
        }
        return data

    def __repr__(self):
        return f'<Booking {self.phone}>'

class BookingCounter(BaseModel):
    __tablename__ = 'counter'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    counter = db.Column(db.Integer, autoincrement=True)

    def to_dict(self):
        data = {
            'id': self.id,
            'conter': self.counter,
        }
        return data

    def __repr__(self):
        return f'<Counter {self.counter}>'
