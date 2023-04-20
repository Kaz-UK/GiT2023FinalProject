from application.models.booking import Booking
from application.models.cafesession import Cafesession
from application.models.customer import Customer
from application.models.game import Game
from application.models.review import Review
from application.models.stock import Stock

from application import db

# All customers
def get_all_customers():
    return db.session.query(Customer).all()


# All games
def get_all_games():
    return db.session.query(Game).all()


# All reviews
def get_all_reviews():
    return db.session.query(Review).all()


# All bookings
def get_all_bookings():
    return db.session.query(Booking).all()


# All cafesessions
def get_all_cafesessions():
    return db.session.query(Cafesession).all()


# All reviews
def get_all_stocks():
    return db.session.query(Stock).all()


# Search game title (for nav bar search function)
# def get_search_game_name(name):
#     return db.session.query(Game).filter_by(game_name=name).first()

# GAME BY NAME (Faye)
def get_game_by_name(game_name):
    if len(game_name) > 0:
        game = db.session.query(Game).filter_by(game_name=game_name).first()
        return game
    else:
        return None