from flask import render_template, jsonify, request
from application.models.booking import Booking
from application.models.cafesession import Cafesession
from application.models.customer import Customer
from application.models.game import Game
from application.models.review import Review
from application.models.stock import Stock

from application import db

from application import app, service

# Creates a homepage using the Jinja template
@app.route('/')
@app.route('/home')
def show_home():
    return render_template('home.html', title="Welcome")

# ALL CUSTOMER
@app.route('/customers', methods=['GET'])
def show_customers():
    error = ""
    customers = service.get_all_customers()
    if len(customers) == 0:
        error = "There are no customers to display"
    #return render_template('customer.html', customers=customers, message=error, title="All Customer's Information")
    return jsonify(customers)
# ALL GAMES
@app.route('/games', methods=['GET'])
def show_games():
    error = ""
    games = service.get_all_games()
    if len(games) == 0:
        error = "There are no games to display"
    #return render_template('games.html', customers=customers, message=error, title="All Games")
    return jsonify(games)
# ALL REVIEWS
@app.route('/reviews', methods=['GET'])
def show_reviews():
    error = ""
    reviews = service.get_all_reviews()
    if len(reviews) == 0:
        error = "There are no reviews to display"
    #return render_template('customer.html', reviews=reviews, message=error, title="All Reviews")
    return jsonify(reviews)


# ALL Bookings
@app.route('/bookings', methods=['GET'])
def show_bookings():
    error = ""
    bookings = service.get_all_bookings()
    if len(bookings) == 0:
        error = "There are no bookings to display"
    #return render_template('customer.html', bookings=bookings, message=error, title="All Reviews")
    return jsonify(bookings)

# ALL CAFESESSIONS
@app.route('/cafesessions', methods=['GET'])
def show_cafesessions():
    error = ""
    cafesessions = service.get_all_cafesessions()
    if len(cafesessions) == 0:
        error = "There are no cafesessions to display"
    #return render_template('customer.html', cafesessions=cafesessions, message=error, title="All Reviews")
    return jsonify(cafesessions)

# ALL STOCK
@app.route('/stock', methods=['GET'])
def show_stock():
    error = ""
    stock = service.get_all_stock()
    if len(stock) == 0:
        error = "There is no stock to display"
    #return render_template('customer.html', stock=stock, message=error, title="All Reviews")
    return jsonify(stock)


@app.route('/games/<game_name>', methods=['GET'])
def show_game_details(game_name):
    error = ""
    game = service.get_game_by_name(game_name)
    if not game:
        error = "There is no game called " + game_name
    return render_template('game.html', game=game, message=error, game_name=game_name, title=game.game_name)
    # return jsonify(game)
