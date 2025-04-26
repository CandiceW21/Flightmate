from matcher import RideRequest, perfect_match, potential_match
from datetime import datetime
existing_requests = []

def main()
    while True:
        name = input("Name")
        email = input("Email: ")
        airport = input("Airport (e.g., JFK, LGA):")
        datetime_str = input("Time (YYYY/MM/DD HH:MM)")
        dt = datetime.strptime(datetime_str, "%Y-%m-%d %H: %M")

        new_req = RideRequest(name, email, airport, dt)

        matches = perfect_match(new_req, existing_requests)
        if matches:
            for m in matches:
                print("f - {m.name}" at {m.datetime}")