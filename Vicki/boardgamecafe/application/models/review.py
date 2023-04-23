from application import db
from application import db
from dataclasses import dataclass


@dataclass
class Review(db.Model):

    review_id: int
    review: str
    stars: int
    review_date: str
    customer_id: int
    game_id: int

    review_id = db.Column(db.Integer, primary_key=True, nullable=False)
    review = db.Column(db.String(4000), nullable=True)
    stars = db.Column(db.Integer, nullable=True)
    review_date = db.Column(db.String(10), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.customer_id"), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey("game.game_id"), nullable=False)

    customers = db.relationship("Customer", back_populates="reviews")
    games = db.relationship("Game", back_populates="reviews")


