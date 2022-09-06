from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Interval
from datetime import timedelta

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    email_address = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    cards = db.relationship('Card')
    invoices = db.relationship('Invoice')
    is_active = db.Column(db.Boolean)
    is_admin = db.Column(db.Boolean)
    last_updated = db.Column(db.DateTime(timezone=False), default=func.now(), onupdate=func.now())
    
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(19), unique=True)
    status = db.Column(db.String(30))
    card_name = db.Column(db.String(30))
    creation_date = db.Column(db.Date(), default=func.now())
    expiry_date = db.Column(db.Date())
    last_updated = db.Column(db.DateTime(timezone=False), onupdate=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_reference = db.Column(db.String(30))
    invoice_date = db.Column(db.Date())
    payment_date = db.Column(db.Date())
    customer_address = db.Column(db.String(300))
    net_amount = db.Column(db.Numeric(19, 2))
    gross_amount = db.Column(db.Numeric(19, 2))
    vat_amount = db.Column(db.Numeric(19, 2))
    line_items = db.relationship('InvoiceLineItem')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class InvoiceLineItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    product_quantity = db.Column(db.Integer)
    net_amount = db.Column(db.Numeric(19, 2))
    gross_amount = db.Column(db.Numeric(19, 2))
    vat_amount = db.Column(db.Numeric(19, 2))
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))