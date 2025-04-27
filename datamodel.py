from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import timedelta

Base = declarative_base()

class Riderequest:
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
        if(request.airport == new_req.airport and abs(request.datetime - new_req.datetime) <= Tolerance_1):
            matches.append(request)
            exisiting_req.remove(request)
    return matches

def potential_match(new_req, exisiting_req):
    pot = []
    for request in exisiting_req:
        if(request.airport == new_req.airport 
           and abs(request.datetime - new_req.datetime) > Tolerance_1
           and abs(request.datetime - new_req.datetime) <= Tolerance_2):
            pot.append(request)
            exisiting_req.remove(request)
    return pot



