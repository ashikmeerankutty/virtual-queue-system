from app import db
from app.models import BookingModel,BookingCounter,UserDepartmentModel,DoctorModel
tokenString = "T2019"
startCounter = 0

class BookingService(object):
    def addToken(self,phone,doctorid):
        global tokenString
        counter = BookingCounter.query.get(1)
        genToken = tokenString+str(counter.counter)
        booking = BookingModel(phone=phone,token=genToken)
        db.session.add(booking)
        db.session.commit()
        doctor = DoctorModel.query.get(doctorid)
        bookinguser = UserDepartmentModel(user=booking,department=doctor)
        db.session.add(bookinguser)
        db.session.commit()
        self.incrementCounter()
        return genToken

    def incrementCounter(self):               
        counter = BookingCounter.query.get(1)
        counter.counter = counter.counter + 1
        db.session.add(counter)
        db.session.commit()
