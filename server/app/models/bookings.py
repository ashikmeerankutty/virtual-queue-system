from app import db
from app.models.base import BaseModel


class BookingModel(BaseModel):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(255), index=True)
    token = db.Column(db.String(255), index=True, unique=True)
    departments = db.relationship('UserDepartmentModel', back_populates="user")


    def to_dict(self):
        data = {
            'id': self.id,
            'phone': self.phone,
            'token': self.token,
            'time': self.created_on,
            'department': self.departments.department
        }
        return data

    def __repr__(self):
        return "<Booking>"

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
        return "<Counter>"


class DoctorModel(BaseModel):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department = db.Column(db.String(255), index=True)
    patients = db.relationship('UserDepartmentModel', back_populates="department")


    def to_dict(self):
        data = {
            'id': self.id,
            'department': self.department,
        }
        return data

    def __repr__(self):
        return "<Booking>"

class UserDepartmentModel(BaseModel):
    __tablename__ = 'user_doctors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('bookings.id'))
    user = db.relationship('BookingModel', back_populates="departments")
    department_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    department = db.relationship('DoctorModel', back_populates="patients")

    def to_dict(self):
        data = {
            'id': self.id,
            'user':self.user.token,
            'phone':self.user.phone or "",
            'department': self.department.department or "",
            'time':self.created_on
        }
        return data

    def __repr__(self):
        return "<UserDepartment>"
