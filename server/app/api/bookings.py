from flask import jsonify,request
from app.api import bp
from app.utils import accessManager
from app.services import BookingService
from app.models import BookingModel,DoctorModel,UserDepartmentModel

@bp.route('/api/v1/booking.addBooking', methods=['POST'])
def setToken():
    data = request.get_json()
    bookingService = BookingService()
    booking = bookingService.addToken(data['phone'],data['doctorid'])
    return jsonify({"msg": booking}), 200

@bp.route('/api/v1/booking.getBookings', methods=['POST'])
def getTokens():
    datas = request.get_json()
    data = BookingModel.to_collection_dict(datas['page'],datas['count'])
    return jsonify({"data":data}), 200

@bp.route('/api/v1/booking.getBookingsAll', methods=['POST'])
def getBookings():
    data = request.get_json()
    data = UserDepartmentModel.to_collection_dict(data['page'],data['count'])
    return jsonify({"data": data}), 200


@bp.route('/api/v1/booking.getDoctors', methods=['GET'])
def getDoctors():
    data = request.get_json()
    data = DoctorModel.to_collection_dict(data['page'],data['count'])
    return jsonify({"data": data}), 200


@bp.route('/api/v1/booking.getBookingsDepartment', methods=['POST'])
def getBookingsDepartment():
    data = request.get_json()
    department = DoctorModel.query.get(data['id'])
    datas = UserDepartmentModel.query.filter_by(department=department).all()
    records = [data.to_dict() for data in datas]
    return jsonify({"data": records}), 200
