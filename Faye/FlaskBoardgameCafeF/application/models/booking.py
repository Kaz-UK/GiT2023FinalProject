from application import db
from dataclasses import dataclass

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
@dataclass

class Booking(db.Model):
    booking_id: int
    stock_id: int
    session_id: int
    customer_id: int
    number_of_tables: int

    booking_id = db.Column(db.Integer, primary_key=True, nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.stock_id'))
    session_id = db.Column(db.Integer, db.ForeignKey('cafesession.session_id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    number_of_tables = db.Column(db.Integer)
    stocks = db.relationship("Stock", back_populates="bookings")
    cafesessions = db.relationship("Cafesession", back_populates="bookings")
    customers = db.relationship("Customer", back_populates="bookings")


