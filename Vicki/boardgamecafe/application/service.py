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