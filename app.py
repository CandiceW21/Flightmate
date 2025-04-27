from datamodel import Riderequest, perfect_match, potential_match, Session
from datetime import datetime

existing_requests = []

def main():
    print("start!")
    session = Session()

    while True:
        name = input("Name: ")
        email = input("Email: ")
        airport = input("Airport (e.g., JFK, LGA): ")
        datetime_str = input("Time (YYYY/MM/DD HH:MM): ")
        dt = datetime.strptime(datetime_str, "%Y/%m/%d %H:%M")

        new_req = Riderequest(name, email, airport, dt)
        
        session.add(new_req)
        session.commit()
        print("req saved")

        total_requests = session.query(Riderequest).count()
        print(f"total req saved: {total_requests}")

        if total_requests >= 10:
            print("matching starts...")

            all_reqs = session.query(Riderequest).all()
            
            matches = perfect_match(new_req, all_reqs)

            if matches:
                for m in matches:
                    print(f" match with {m.name} at {m.datetime}")
                    session.delete(m)
                session.delete(new_req)
                session.commit()
            else:
                pot = potential_match(new_req, all_reqs)
                if pot:
                    for m in pot:
                        print(f"-potentially with {m.name} at {m.datetime}")
                        
                else:
                    print(f"no match now")
        cont = input("\n add? (y/n): ")
        if cont != 'y':
            break

    session.close()
    print("end of matching")
    
if __name__ == "__main__":
    main()
