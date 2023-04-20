from application import db
from dataclasses import dataclass

@dataclass

class Game(db.Model):

    game_id: int
    game_name: str
    num_of_players: int
    min_age: int
    duration_of_play_time: int
    gameplay: str
    game_description: str

    game_id = db.Column(db.Integer, primary_key=True, nullable=False)
    game_name = db.Column(db.String, nullable=False)
    num_of_players = db.Column(db.Integer, nullable=False)
    min_age = db.Column(db.Integer, nullable=False)
    duration_of_play_time = db.Column(db.Integer, nullable=False)
    gameplay = db.Column(db.String(50), nullable=True)
    game_description = db.Column(db.String(10000), nullable=True)
    stocks = db.relationship("Stock", back_populates="games")
    reviews = db.relationship("Review", back_populates="games")