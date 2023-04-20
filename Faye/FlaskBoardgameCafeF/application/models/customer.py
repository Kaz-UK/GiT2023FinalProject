from application import db
from dataclasses import dataclass

@dataclass

class Customer(db.Model):
    customer_id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    account_status: str
    customer_password: str
    join_date: str

    customer_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    account_status = db.Column(db.String, nullable=False)
    customer_password = db.Column(db.String(100), nullable=False)
    join_date = db.Column(db.String, nullable=False)

    bookings = db.relationship("Booking", back_populates="customers")
    reviews = db.relationship("Review", back_populates="customers")