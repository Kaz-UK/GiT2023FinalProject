from application import db
from dataclasses import dataclass


@dataclass
class Booking(db.Model):
    booking_id: int
    stock_id: int
    session_id: int
    customer_id: int
    number_of_tables: int

    booking_id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey("stock.stock_id"), nullable=True)
    session_id = db.Column(db.Integer, db.ForeignKey("cafesession.session_id"), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.customer_id"), nullable=False)
    number_of_tables = db.Column(db.Integer, nullable=True)
    stocks = db.relationship("Stock", back_populates="bookings")
    cafesessions = db.relationship("Cafesession", back_populates="bookings")
    customers = db.relationship("Customer", back_populates="bookings")
