from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import timedelta

Base = declarative_base()

class Riderequest(Base):
    __tablename__  = 'ride_requests'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String)
    airport = Column(String)
    datetime = Column(DateTime)
    
    def __init__(self, name, email, airport, datetime):
        self.name = name
        self.email = email
        self.airport = airport
        self.datetime = datetime

    def __str__(self):
        return f"{self.name} - {self.airport} at {self.datetime}"

Tolerance_1 = timedelta(minutes = 30)
Tolerance_2 = timedelta(minutes = 60)

def perfect_match(new_req, exisiting_req):
    matches = []
    for request in exisiting_req:
        if request.id == new_req.id:
            continue
        if(request.airport == new_req.airport and abs(request.datetime - new_req.datetime) <= Tolerance_1):
            matches.append((new_req,request))
            
            break
    return matches

def potential_match(new_req, exisiting_req):
    pot = []
    for request in exisiting_req:
        if request.id == new_req.id:
            continue
        if(request.airport == new_req.airport 
           and abs(request.datetime - new_req.datetime) > Tolerance_1
           and abs(request.datetime - new_req.datetime) <= Tolerance_2):
            pot.append((new_req, request))
            break
    return pot


engine = create_engine('sqlite:///rideinfo.db', echo=True)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

