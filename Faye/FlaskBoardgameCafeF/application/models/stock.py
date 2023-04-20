from application import db
from dataclasses import dataclass


@dataclass
class Stock(db.Model):

    stock_id: int
    game_id: int

    stock_id = db.Column(db.Integer, primary_key=True, nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey("game.game_id"), nullable=False)
    bookings = db.relationship("Booking", back_populates="stocks")
    games = db.relationship("Game", back_populates="stocks")