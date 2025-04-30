from flask import Flask, render_template, request, redirect
from datamodel import Base, Riderequest, perfect_match, potential_match, Session
from datetime import datetime

app = Flask(__name__)
ready = False

@app.route('/', methods = ['GET','POST'])
def index():
    session = Session()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['name']
        airport = request.form['airport']
        datetime_str = request.form['datetime']
        dt = datetime.strptime(datetime_str, "%Y/%m/%d %H:%M")

        new_req = Riderequest(name, email, airport, dt)
        session.add(new_req)
        session.commit()

        total_requests = session.query(Riderequest).count()

        if not ready and total_requests >= 10:
            ready = True
        
        if ready: 
            all_reqs = session.query(Riderequest).all()
            matches = perfect_match(new_req, all_reqs)

            if matches:
                for m in matches:
                    print(f'"{m[0].name}" at {m[0].datetime} matches with {m[1].name} at {m[1].datetime}"')
                    session.delete(m[0])
                    session.delete(m[1])
                session.delete(new_req)
                session.commit()
            else:
                pot = potential_match(new_req, all_reqs)
                if pot:
                    for m in pot:
                        print(f"-potentially with {m.name} at {m.datetime}")
                else:
                    print(f"no match now")
    return render_template("index.html")

        

           
        
        
    

