from app import db
from app.models import BookingModel,BookingCounter
tokenString = "T2019"
startCounter = 0

class BookingService(object):
    def addToken(self,phone):
        global tokenString
        counter = BookingCounter.query.get(1)
        genToken = tokenString+str(counter.counter)
        booking = BookingModel(phone=phone,token=genToken)
        db.session.add(booking)
        db.session.commit()
        self.incrementCounter()

    def incrementCounter(self):               
        counter = BookingCounter.query.get(1)
        counter.counter = counter.counter + 1
        db.session.add(counter)
        db.session.commit()
