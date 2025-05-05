from flask import Flask, render_template, request, redirect
from datamodel import Base, Riderequest, perfect_match, potential_match, Session
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
app = Flask(__name__)
ready = False


def send_email(to_email, subject, body):
    from_email = "candice2106.7@gmail.com"
    password = "owmn ooxt sdnn vjra"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, password)
        server.send_message(msg)

@app.route('/', methods = ['GET','POST'])
def index():
    global ready
    session = Session()
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
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
                    print(f'"{m[0].name}" at {m[0].datetime} matches with {m[1].email} at {m[1].datetime}"')
                    send_email(new_req.email, f'Ride match found for you, {new_req.name}!', f'Dear "{new_req.name}",You are matched with "{m[1].name}" who wishes to leave at {m[1].datetime}. We hope your trip to {m[1].airport} is pleasant! \n-- Flightmate')
                    send_email(m[1].email, f'Ride match found for you, {m[1].name}!', f'Dear "{m[1].name}", You are matched with "{new_req.name}" who wishes to leave at {new_req.datetime}. We hope your trip to {m[1].airport} is pleasant! \n-- Flightmate')
                    session.delete(m[0])
                    session.delete(m[1])
                    
                #session.delete(new_req)
                session.commit()
            else:
                pot = potential_match(new_req, all_reqs)
                if pot:
                    for m in pot:
                        print(f'your request "{m[0].name}" at {m[0].datetime} can potentially match with "{m[1].name}" at {m[1].datetime}')
                        send_email(m[0].email, f'Potential ride match found for you, {new_req.name}!', f'Dear "{new_req.name}",You can potentially be matched with "{m[1].name}" who wishes to leave at {m[1].datetime}. We hope your trip to {m[1].airport} is pleasant! \n-- Flightmate')
                        send_email(m[1].email, f'Potential ride match found for you, {m[1].name}!', f'Dear "{m[1].name}", You can potentially be matched with "{m[0].name}" who wishes to leave at {new_req.datetime}. We hope your trip to {m[1].airport} is pleasant! \n-- Flightmate')
                else:
                    print(f"no match now")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


 
        
        
    

