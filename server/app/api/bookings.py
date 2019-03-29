from flask import jsonify,request
from app.api import bp
from app.utils import accessManager
from app.services import BookingService
from app.models import BookingModel

@bp.route('/api/v1/booking.addBooking', methods=['POST'])
def setToken():
    data = request.get_json()
    bookingService = BookingService()
    booking = bookingService.addToken(data['phone'])
    return jsonify({"msg": "Success"}), 200

@bp.route('/api/v1/booking.getBookings', methods=['GET'])
@accessManager()
def getTokens():
    data = request.get_json()
    data = BookingModel.to_collection_dict(data['page'],data['count'])
    return jsonify({"data": data}), 200
