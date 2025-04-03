from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class District(db.Model):
    __tablename__ = 'districts'
    
    district_code = db.Column(db.Integer, primary_key=True)
    district_name = db.Column(db.String(100), nullable=False)
    
    pensioners = db.relationship('Pensioner', back_populates='district')

class Pensioner(db.Model):
    __tablename__ = 'pensioners'
    
    pensioner_id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50))
    birth_date = db.Column(db.Date, nullable=False)
    district_code = db.Column(db.Integer, db.ForeignKey('districts.district_code'))
    address = db.Column(db.Text, nullable=False)
    
    district = db.relationship('District', back_populates='pensioners')
    payments = db.relationship('Payment', backref='pensioner', lazy=True)

class Pension(db.Model):
    __tablename__ = 'pensions'
    
    pension_code = db.Column(db.Integer, primary_key=True)
    pension_name = db.Column(db.String(100), nullable=False)
    
    payments = db.relationship('Payment', backref='pension', lazy=True)

class Payment(db.Model):
    __tablename__ = 'payments'
    
    payment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pensioner_id = db.Column(db.Integer, db.ForeignKey('pensioners.pensioner_id'), nullable=False)
    pension_code = db.Column(db.Integer, db.ForeignKey('pensions.pension_code'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    additional_payment = db.Column(db.Numeric(10, 2), default=0.00)
    additional_info = db.Column(db.Text)