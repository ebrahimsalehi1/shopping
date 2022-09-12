from email.policy import default
from xmlrpc.client import DateTime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    code = db.Column(db.Integer, unique=True)
    order = db.relationship('Order', backref='customer', lazy=True)

    def __init__(self, name, code):
        self.name = name
        self.code = code


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def __init__(self, date, customer_id):
        self.date = date
        self.customer_id = customer_id


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
