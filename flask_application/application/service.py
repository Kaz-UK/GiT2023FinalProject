from flask import flash
# from sqlalchemy import func

from application.models.booking import Booking
from application.models.cafesession import Cafesession
from application.models.customer import Customer
from application.models.game import Game
from application.models.review import Review
from application.models.stock import Stock
import datetime
from application import db


# ALL CUSTOMERS (VICKI)
def get_all_customers():
    return db.session.query(Customer).all()


# ALL GAMES (AMY)
def get_all_games():
    return db.session.query(Game).order_by(Game.game_name).all()


# ALL REVIEWS (VICKI)
def get_all_reviews():
    return db.session.query(Review).all()


# ALL BOOKINGS (VICKI)
def get_all_bookings():
    return db.session.query(Booking).all()


# GET BOOKING BY CUSTOMER ID (KAREN)
def get_customer_booking(customer_id):
    return db.session.query(Booking).filter_by(customer_id=customer_id).all()


# ALL CAFESESSIONS (VICKI)
def get_all_cafesessions():
    return db.session.query(Cafesession).all()


# ALL CAFESESSIONS - CUSTOMER DASHBOARD (KAREN)
def get_cafe_session(session_id):
    return db.session.query(Cafesession).filter_by(session_id=session_id).all()


# ALL STOCK (VICKI)
def get_all_stock():
    return db.session.query(Stock).all()


# GET ALL GAMES WITH STOCK INFORMATION (KAREN)
def get_game_stock():
    stock = db.session.query(Stock).all()
    stock_levels = {}
    for item in stock:
        game_details = db.session.query(Game).filter_by(game_id=item.game_id).first()
        if game_details.game_name in stock_levels:
            stock_levels[game_details.game_name] += 1
        else:
            stock_levels[game_details.game_name] = 1
    sorted_games = dict(sorted(stock_levels.items()))
    return sorted_games


# INDIVIDUAL GAMES PAGE - GET GAME BY GAME NAME (FAYE)*
def get_game_by_name(game_name):
    if len(game_name) > 0:
        game = db.session.query(Game).filter_by(game_name=game_name).first_or_404()
        return game
    else:
        return None


# REVIEW - GET GAME ID FROM GAME NAME (VICKI)
def get_game_id_by_name(game_name):
    game = db.session.query(Game).filter_by(game_name=game_name).first()
    return game.game_id


# REVIEW - GET GAME ID FROM GAME NAME (VICKI)
def show_game_details(game_name):
    if not game_name:
        game = db.session.query(Game).filter_by(game_name=game_name).first()
        return game
    else:
        return None


# GET CUSTOMER ID FROM EMAIL (KAREN/VICKI)
def get_customer_by_email(email):
    return db.session.query(Customer).filter_by(email=email).first()


# ADD NEW REVIEW (VICKI)
def add_new_review(review):
    db.session.add(review)
    db.session.commit()


# ADD NEW BOOKING (VICKI)
def add_new_booking(booking):
    db.session.add(booking)
    db.session.commit()


# GET REVIEW BY GAME ID (FAYE)
def get_reviews_by_game_id(game_id):
    return db.session.query(Review).filter_by(game_id=game_id).order_by(Review.review_date.desc()).all()


# BOOKING - GET CAFESESSION DETAILS (KAREN)
def get_cafesession_details(session_date):
    return db.session.query(Cafesession).filter_by(session_date=session_date).all()


# BOOKING - UPDATE TABLES (KAREN)
def update_table_count(session_id):
    session_info = db.session.query(Cafesession).filter_by(session_id=session_id).first()
    session_info.table_count -= 1
    db.session.commit()


# NAV BAR SEARCH FUNCTION (KAREN)
def get_searched_games(game_name):
    search = "%{}%".format(game_name)
    return db.session.query(Game).filter(Game.game_name.like(search)).all()


# ADD NEW CUSTOMER (KAREN)
def add_new_customer(customer):
    db.session.add(customer)
    db.session.commit()


# ADD NEW CUSTOMER - CHECK IF EXISTING CUSTOMER (KAREN)
def check_email_status(email):
    status = db.session.query(Customer).filter_by(email=email).first()
    if not status:
        return None
    else:
        return "This email is already in use"


# GAME REVIEWS - GET CUSTOMER BY CUSTOMER ID (FAYE)
def get_customer_by_customer_id(customer_id):
    return db.session.query(Customer).filter_by(customer_id=customer_id).first()


# GET CUSTOMER REVIEWS FOR CUSTOMER DASHBOARD (KAREN)
def get_reviews(customer_id):
    review_details = db.session.query(Review).filter_by(customer_id=customer_id).all()
    review_list = []
    if review_list == 0:
        return None
    for row in review_details:
        game_name = get_game_name_by_id(row.game_id)
        review_detail = {"review": row.review, "stars": row.stars, "review_date": row.review_date,
                         "game": game_name, "review_id": row.review_id}
        review_list.append(review_detail)
    return review_list


# GET GAMES BY GAME ID FOR CUSTOMER DASHBOARD (KAREN)
def get_game_name_by_id(game_id):
    game = db.session.query(Game).filter_by(game_id=game_id).first()
    return game.game_name


# GET CUSTOMER BOOKINGS FOR CUSTOMER DASHBOARD (KAREN)
def get_bookings(customer_id):
    booking_details = db.session.query(Booking).filter_by(customer_id=customer_id).all()
    booking_list = []
    if booking_list == 0:
        return None
    for row in booking_details:
        session_details = db.session.query(Cafesession).filter_by(session_id=row.session_id).first()
        if row.stock_id is None:
            booking_detail = {"date": session_details.session_date, "session_type": session_details.session_type,
                              "game_name": "No game selected", "booking_id": row.booking_id}
        else:
            stock_type = db.session.query(Stock).filter_by(stock_id=row.stock_id).first()
            game = db.session.query(Game).filter_by(game_id=stock_type.game_id).first()
            booking_detail = {"date": session_details.session_date, "session_type": session_details.session_type,
                              "game_name": game.game_name, "booking_id": row.booking_id}
        booking_list.append(booking_detail)
    return booking_list


# ADD NEW SESSION - ADMIN USER (FAYE)
def add_new_session(session):
    db.session.add(session)
    db.session.commit()


# SEARCH FOR GAME BY GAMEPLAY (FAYE)
def search_by_gameplay(gameplay):
    return db.session.query(Game).filter_by(gameplay=gameplay).all()


# SEARCH FOR GAME BY NUMBER OF PLAYERS (FAYE)
def search_games_by_num_of_players(num_of_players):
    return db.session.query(Game).filter_by(num_of_players=num_of_players).all()


# ADD NEW GAME (AMY)
def add_new_game(game):
    db.session.add(game)
    db.session.commit()


# ADD NEW STOCK (KAREN)
def add_stock(stock):
    db.session.add(stock)
    db.session.commit()


# DELETE REVIEW - GET DETAILS (KAREN)
def get_review_by_id(review_id):
    return db.session.query(Review).filter_by(review_id=review_id).first_or_404()


# DELETE REVIEW (KAREN)
def delete_review(review_id):
    db.session.delete(review_id)
    db.session.commit()


# DELETE BOOKING - GET BOOKING DETAILS (KAREN)
def get_booking_by_id(booking_id):
    return db.session.query(Booking).filter_by(booking_id=booking_id).first_or_404()


# DELETE BOOKING - GET SESSION DETAILS (KAREN)
def get_session_by_id(session_id):
    return db.session.query(Cafesession).filter_by(session_id=session_id).first_or_404()


# DELETE BOOKING (KAREN)
def delete_booking(booking_id, session_id):
    session_info = db.session.query(Cafesession).filter_by(session_id=session_id).first()
    session_info.table_count += 1
    db.session.delete(booking_id)
    db.session.commit()


# def get_cafesession_by_type(session_type):
#     return db.session.query(Cafesession).filter_by(session_type=session_type).first()
#
#
# # GET CAFESESSION BY SESSION ID
# def get_cafe_session_by_session_id(cafesession):
#     return db.session.query(Cafesession).filter_by(cafesession=cafesession).order_by(func.max(Cafesession.session_id))
#
#
# # CAFESESSION ID BY DATE AND SESSION
# def get_cafesession_by_date_and_type(session_date, session_type):
#     return db.session.query(Cafesession).filter_by(session_date=session_date, session_type=session_type).first()
#
#
# # CUSTOMERS BY ID*
# def get_customer_by_id(customer_id):
#     if customer_id > 0:
#         return db.session.query(Customer).filter_by(customer_id=customer_id).first()
#     else:
#         return None
#
#
# # BOOKING - CAFESESSION ID BY DATE AND SESSION (VICKI)
# def get_cafesession_by_date(session_date):
#     if not session_date:
#         return db.session.query(Cafesession).filter_by(session_date=session_date).first()
#     else:
#         return None
#
#
# # BOOKING - GET CAFESESSION DETAILS (KAREN)
# def get_cafesession_details(session_date):
#     booking_date = db.session.query(Cafesession).filter_by(session_date=session_date).all()
#     for session_info in booking_date:
#         if session_info.session_type == session_type:
#             booking_session_id = session_info.session_id
#             return booking_session_id
#     else:
#         return None
