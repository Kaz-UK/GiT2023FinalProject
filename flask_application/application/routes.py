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
from application.forms.ReviewForm import ReviewForm

import datetime


# CREATES A HOMEPAGE
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Welcome")


# CREATES AN ABOUT US PAGE
@app.route('/about')
def about():
    return render_template('about.html', title="About Us")


# CREATES ERROR HANDLER (404 PAGE NOT FOUND)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found")


# CREATES ERROR HANDLER (405 METHOD NOT ALLOWED)
@app.errorhandler(405)
def invalid_token(e):
    return render_template('405.html', title="Method Not Allowed")


# SEND INFORMATION FROM NAVIGATION SEARCH BAR (FROM ALL HTML PAGE)
@app.context_processor
def layout():
    form = SearchForm()
    return dict(form=form)


# NAVIGATION BAR SEARCH FUNCTION (PRODUCES A LIST OF SEARCH RESULTS)
@app.route('/search', methods=['POST'])
def search():
    form = SearchForm()
    error = ""
    if form.validate_on_submit():
        title_search = form.searched_game_name.data
        results = service.get_searched_games(title_search)
        if not results:
            error = f"Sorry there are no games with the name '{title_search}'"
    else:
        results = ""
        error = "There was an error with your request, did you enter a game name?"
    return render_template('search.html', results=results, message=error, title='Search Results')


# ALL CUSTOMERS
@app.route('/customers', methods=['GET'])
def show_customers():
    error = ""
    customers = service.get_all_customers()
    if len(customers) == 0:
        error = "There are no customers to display"
    #return render_template('customer.html', customers=customers, message=error, title="All Customer's Information")
    return jsonify(customers)


# CUSTOMERS BY ID
@app.route('/customers/<int:customer_id>', methods=['GET'])
def show_customer(customer_id):
    error = ""
    customer = service.get_customer_by_id(customer_id)
    if not customer:
        return jsonify("There is no customer with ID: " + str(customer_id))
    else:
        print(customer.first_name, customer.last_name)
    return jsonify(customer)
    #return render_template('customer.html', customer=customer, customer_id=customer_id, message=error, title="Customer Information")


# ALL GAMES
@app.route('/games', methods=['GET'])
def show_games():
    error = ""
    games = service.get_all_games()
    if len(games) == 0:
        error = "There are no games to display"
    return render_template('games.html', games=games, message=error, title="All Games")


# ALL REVIEWS
@app.route('/reviews', methods=['GET'])
def show_reviews():
    error = ""
    reviews = service.get_all_reviews()
    if len(reviews) == 0:
        error = "There are no reviews to display"
    #return render_template('customer.html', reviews=reviews, message=error, title="All Reviews")
    return jsonify(reviews)


# ALL BOOKINGS
@app.route('/bookings', methods=['GET'])
def show_bookings():
    error = ""
    bookings = service.get_all_bookings()
    if len(bookings) == 0:
        error = "There are no bookings to display"
    #return render_template('customer.html', bookings=bookings, message=error, title="All Bookings")
    return jsonify(bookings)


# ALL CAFESESSIONS
@app.route('/cafesessions', methods=['GET'])
def show_cafesessions():
    error = ""
    cafesessions = service.get_all_cafesessions()
    if len(cafesessions) == 0:
        error = "There are no cafesessions to display"
    #return render_template('customer.html', cafesessions=cafesessions, message=error, title="All Sessions")
    return jsonify(cafesessions)


# ALL STOCK
@app.route('/stock', methods=['GET'])
def show_stock():
    error = ""
    stock = service.get_all_stock()
    if len(stock) == 0:
        error = "There is no stock to display"
    #return render_template('customer.html', stock=stock, message=error, title="All Stocks")
    return jsonify(stock)


# # GET GAME BY GAME NAME (USED IN REVIEW)
# @app.route('/games/<game_name>', methods=['GET'])
# def show_game_details(game_name):
#     error = ""
#     game = service.get_game_by_name(game_name)
#     if not game:
#         error = "There is no game called " + game_name
#     return render_template('game.html', game=game, message=error, game_name=game_name, title=game.game_name)
#     # return jsonify(game)


# GET CUSTOMER ID FROM EMAIL (FOR REVIEW)
@app.route('/customer/<email>', methods=['GET'])
def show_customer_details(email):
    error = ""
    customer = service.get_customer_by_email(email)
    if not customer:
        error = "There is no one with the email " + email
    else:
        for e in customer.email:
            return str(customer.customer_id)


# ADD A NEW REVIEW
@app.route('/new_review', methods=['GET', 'POST'])
def add_new_review():
    error = ""
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.form)
        review = form.review.data
        stars = form.stars.data
        review_date = datetime.date.today()
        customer = form.email.data
        game = form.game_list.data
        if not stars:
            error = "Please give a review"
        else:
            service.show_game_details(game)
            cust = show_customer_details(customer)
            review = Review(review=review, stars=stars,
                           review_date=review_date, customer_id=cust, game_id=game.game_id)
            service.add_new_review(review)
            reviews = service.get_all_reviews()
            return render_template('review.html', customer_id=cust, reviews=reviews, stars=stars, game_id=game.game_id, message=error)
    return render_template('new_review_form.html', form=form, message=error)


# INDIVIDUAL GAMES
@app.route('/games/<game_name>', methods=['GET'])
def show_game_details(game_name):
    error = ""
    game = service.get_game_by_name(game_name)
    reviews_for_game = service.get_reviews_by_game_id(game.game_id)
    first_names = []
    if not game:
        error = "There is no game called " + game_name
    else:
        for rev in reviews_for_game:
            customer = service.get_customer_by_customer_id(rev.customer_id)
            first_names.append(customer.first_name)
    return render_template('game.html', game=game, message=error, game_name=game_name, game_id=str(game.game_id),
                            first_names=first_names, reviews_for_game=reviews_for_game, title=game.game_name)
    # return jsonify(game)
