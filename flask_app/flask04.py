# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect 
from flask import url_for 
from datetime import date
from database import db
from models import Note as Note
from models import User as User

app = Flask(__name__)     # create an app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)
# Setup models
with app.app_context():
    db.create_all()   # run under the app context
        
# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page
@app.route('/index')
def index():
    a_user =  db.session.query(User).filter_by(email='email').one()
    
    return render_template('index.html', user = a_user)
@app.route('/notes')
def getnotes():
    a_user = db.session.query(User).filter_by(email='email').one()
    my_notes = db.session.query(Note).all()            
    
    return render_template('notes.html', notes = my_notes, user = a_user)
@app.route('/notes/<note_id>')
def getnote(note_id):
    a_user = db.session.query(User).filter_by(email='email').one()
    my_notes = db.session.query(Note).filter_by(id=note_id).one()  
    
    return render_template('note.html', note = my_notes, user = a_user)
@app.route('/notes/new', methods = ['GET', 'POST']) 
def newnote(): 
    a_user = {'name': 'Eliseo', 'email':'email'}
    # Check method used for request. 
    print ('request method is', request.method) 
    if request.method == 'POST': 
        # Get title data.
        title = request.form['title']
        # Get note data.
        text = request.form['noteText']
        # Create data stamp.
        today = date.today()
        # Formate date mm/dd/yyyy.
        today = today.strftime("%m-%d-%Y")
        newEntry = Note(title, text, today)
        db.session.add(newEntry)
        db.session.commit()    
        return redirect(url_for('getnotes', name = a_user))
    else: 
        a_user = db.session.query(User).filter_by(email='email').one()
        return render_template('new.html', user=a_user)
app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.