from application import db
from dataclasses import dataclass


@dataclass
class Cafesession(db.Model):

    session_id: int
    session_type: str
    session_date: str
    table_count: int

    session_id = db.Column(db.Integer, primary_key=True, nullable=False)
    session_type = db.Column(db.String, nullable=False)
    session_date = db.Column(db.String, nullable=False)
    table_count = db.Column(db.Integer, nullable=False)

    bookings = db.relationship("Booking", back_populates="cafesessions")