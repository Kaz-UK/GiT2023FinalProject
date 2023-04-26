from flask import flash
from sqlalchemy import func

import application.models.review
from application.models.booking import Booking
from application.models.cafesession import Cafesession
from application.models.customer import Customer
from application.models.game import Game
from application.models.review import Review
from application.models.stock import Stock
import datetime
from application import db


# ALL CUSTOMERS*
def get_all_customers():
    return db.session.query(Customer).all()


# CUSTOMERS BY ID*
def get_customer_by_id(customer_id):
    if customer_id > 0:
        return db.session.query(Customer).filter_by(customer_id=customer_id).first()
    else:
        return None


# ALL GAMES*
def get_all_games():
    return db.session.query(Game).order_by(Game.game_name).all()


# ALL Reviews*
def get_all_reviews():
    return db.session.query(Review).all()


# ALL Bookings*
def get_all_bookings():
    return db.session.query(Booking).all()


# ALL CAFESESSIONS*
def get_all_cafesessions():
    return db.session.query(Cafesession).all()


# CAFESESSION ID BY DATE AND SESSION
def get_cafesession_by_date_and_type(session_date, session_type):
    return db.session.query(Cafesession).filter_by(session_date=session_date, session_type=session_type).first()


# ALL STOCK*
def get_all_stock():
    return db.session.query(Stock).all()


# GET GAME BY GAME NAME (USED BY INDIVIDUAL GAMES PAGE)*
def get_game_by_name(game_name):
    if len(game_name) > 0:
        game = db.session.query(Game).filter_by(game_name=game_name).first()
        return game
    else:
        return None


# GET GAME ID FROM GAME NAME - USED IN REVIEW - VICKI
def get_game_id_by_name(game_name):
    game = db.session.query(Game).filter_by(game_name=game_name).first()
    return game.game_id


# GET GAME ID FROM GAME NAME - USED IN REVIEW - VICKI
def show_game_details(game_name):
    if not game_name:
        game = db.session.query(Game).filter_by(game_name=game_name).first()
        return game
    else:
        return None


# GET CUSTOMER ID FROM EMAIL*
def get_customer_by_email(email):
    return db.session.query(Customer).filter_by(email=email).first()


# ADD NEW REVIEW*
def add_new_review(review):
    db.session.add(review)
    db.session.commit()


# ADD NEW BOOKING*
def add_new_booking(booking):
    db.session.add(booking)
    db.session.commit()


# GET CUSTOMER BY CUSTOMER ID*
def get_customer_by_customer_id(customer_id):
    return db.session.query(Customer).filter_by(customer_id=customer_id).first()


# GET REVIEW BY GAME ID*
def get_reviews_by_game_id(game_id):
    return db.session.query(Review).filter_by(game_id=game_id).order_by(Review.review_date.desc()).all()


# CAFESESSION ID BY DATE AND SESSION - USED IN BOOKING FORM - VICKI
def get_cafesession_by_date(session_date):
    if not session_date:
        return db.session.query(Cafesession).filter_by(session_date=session_date).first()
    else:
        return None


def get_cafesession_by_type(session_type):
    return db.session.query(Cafesession).filter_by(session_type=session_type).first()


# GET CAFESESSION BY SESSION ID
def get_cafe_session_by_session_id(cafesession):
    return db.session.query(Cafesession).filter_by(cafesession=cafesession).order_by(func.max(Cafesession.session_id))


# SEARCH GAME BY NAME (USED BY SEARCH NAVIGATION BAR)
def get_searched_games(game_name):
    search = "%{}%".format(game_name)
    return db.session.query(Game).filter(Game.game_name.like(search)).all()

# ADD NEW SESSION (ADMIN FACILITY), USED IN ADD SESSION FORM
def add_new_session(session):
    db.session.add(session)
    db.session.commit()