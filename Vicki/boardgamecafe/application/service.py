import application.models.review
from application.models.booking import Booking
from application.models.cafesession import Cafesession
from application.models.customer import Customer
from application.models.game import Game
from application.models.review import Review
from application.models.stock import Stock

from application import db


# ALL CUSTOMERS
def get_all_customers():
    return db.session.query(Customer).all()


# CUSTOMERS BY ID
def get_customer_by_id(customer_id):
    if customer_id > 0:
        return db.session.query(Customer).filter_by(customer_id=customer_id).first()
    else:
        return None


# ALL GAMES
def get_all_games():
    return db.session.query(Game).all()


# ALL Reviews
def get_all_reviews():
    return db.session.query(Review).all()


# ALL Bookings
def get_all_bookings():
    return db.session.query(Booking).all()


# ALL CAFESESSIONS
def get_all_cafesessions():
    return db.session.query(Cafesession).all()


# ALL STOCK
def get_all_stock():
    return db.session.query(Stock).all()


# GET GAME BY GAME NAME
def get_game_by_name(game_name):
    if len(game_name) > 0:
        game = db.session.query(Game).filter_by(game_name=game_name).first()
        return game
    else:
        return None


# ADD NEW REVIEW
def add_new_review(review):
    db.session.add(review)
    db.session.commit()


# ADD NEW BOOKING
def add_new_booking(booking):
    db.session.add(booking)
    db.session.commit()


