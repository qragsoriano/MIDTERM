from platform import uname
from flask import Flask, app, jsonify,request, render_template
from flask.helpers import url_for
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)

app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///MidtermExam.sqlite'
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Accounts(db.model):
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))

def __init__(self, username, password, firstname, lastname):
    self.username = username
    self.password = password
    self.firstname = firstname
    self.lastname = lastname

class AccountsMeta(ma.Schema):
    class Meta:
        acc = ("username", "password", "firstname", "lastname")
        account_meta = Accounts()
        account_meta = Accounts(many=True)

@app.route('/')
def main():
    return render_template("/register.html")

@app.route('/login.html', Method = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        print(username, password)

    if username != "" &password != "":
        check = Accounts.query.filter_by(username=username).first()

        if check is None:
            return
        redirect(url_for('register'))
    else:
            print ("no such acc")

@app.route('/register.html', METHOD = ['GET', 'POST'])
def reg():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        username = request.form.get('username')
        password = request.form.get('password')

        print(firstname, lastname, username, password)

        return render_template('/register.html')

    if __name__ == '__main__':
        app.run(host="0.0.0.0", port=5000)