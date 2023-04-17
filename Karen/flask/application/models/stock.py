from application import db
from dataclasses import dataclass


@dataclass
class Stock(db.Model):

    stock_id: int
    game_id: int

    stock_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.game_id"), nullable=False)
    games = db.relationship("Game", back_populates="stocks")
    bookings = db.relationship("Booking", back_populates="stocks")
