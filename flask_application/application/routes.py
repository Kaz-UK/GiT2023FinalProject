from flask import render_template, jsonify, request
from application.models.booking import Booking
from application.models.cafesession import Cafesession
from application.models.customer import Customer
from application.models.game import Game
from application.models.review import Review
from application.models.stock import Stock

from application import db
from application import app, service
from application.forms.game_search import SearchForm


# Creates a homepage using the Jinja template
@app.route('/')
@app.route('/home')
def show_home():
    return render_template('home.html', title="Welcome")


# Creates an about us page using the Jinja template
@app.route('/about')
def show_about():
    return render_template('about.html', title="About Us")


# Send information from navigation search bar (from all HTML pages)
@app.context_processor
def layout():
    form = SearchForm()
    return dict(form=form)


# Navigation bar search function
@app.route('/search', methods=['POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        title_search = form.searched.data
        result = service.get_search_game_name(title_search)
        return render_template('search.html', searched=result, title='Search Results')


# All customers
@app.route('/customers', methods=['GET'])
def show_customers():
    error = ""
    customers = service.get_all_customers()
    if len(customers) == 0:
        error = "There are no customers to display"
    #return render_template('customer.html', customers=customers, message=error, title="All Customer's Information")
    return jsonify(customers)


# All games
@app.route('/games', methods=['GET'])
def show_games():
    error = ""
    games = service.get_all_games()
    if len(games) == 0:
        error = "There are no games to display"
    #return render_template('customer.html', customers=customers, message=error, title="All Games")
    return jsonify(games)


# All reviews
@app.route('/reviews', methods=['GET'])
def show_reviews():
    error = ""
    reviews = service.get_all_reviews()
    if len(reviews) == 0:
        error = "There are no reviews to display"
    #return render_template('customer.html', reviews=reviews, message=error, title="All Reviews")
    return jsonify(reviews)


# All bookings
@app.route('/bookings', methods=['GET'])
def show_bookings():
    error = ""
    bookings = service.get_all_bookings()
    if len(bookings) == 0:
        error = "There are no bookings to display"
    #return render_template('customer.html', bookings=bookings, message=error, title="All Bookings")
    return jsonify(bookings)


# All cafesessions
@app.route('/cafesessions', methods=['GET'])
def show_cafesessions():
    error = ""
    cafesessions = service.get_all_cafesessions()
    if len(cafesessions) == 0:
        error = "There are no cafesessions to display"
    #return render_template('customer.html', cafesessions=cafesessions, message=error, title="All Sessions")
    return jsonify(cafesessions)


# All stock
@app.route('/stock', methods=['GET'])
def show_stock():
    error = ""
    stock = service.get_all_stock()
    if len(stock) == 0:
        error = "There is no stock to display"
    #return render_template('customer.html', stock=stock, message=error, title="All Stocks")
    return jsonify(stock)


# Individual games
@app.route('/games/<game_name>', methods=['GET'])
def show_game_details(game_name):
    error = ""
    game = service.get_game_by_name(game_name)
    if not game:
        error = "There is no game called " + game_name
    return render_template('game.html', game=game, message=error, game_name=game_name, game_id=str(game.game_id), title=game.game_name)
    # return jsonify(game)
