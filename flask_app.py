from flask import Flask, render_template, request, redirect
from datamodel import Base, Riderequest, perfect_match, potential_match, Session
from datetime import datetime

app = Flask(__name__)

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

        return redirect('/')
    requests = session.query(Riderequest).all()
    return render_template('index.html', requests = requests)

