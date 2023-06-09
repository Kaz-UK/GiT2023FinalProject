from flask import render_template, jsonify, request, redirect

from application.models.booking import Booking
from application.models.cafesession import Cafesession
from application.models.customer import Customer
from application.models.game import Game
from application.models.review import Review
from application.models.stock import Stock

from application import db
from application import app, service

from application.forms.ReviewForm import ReviewForm
from application.forms.BookingForm import BookingForm
from application.forms.game_search import SearchForm
from application.forms.GameForm import GameForm

import datetime

# Creates a homepage using the Jinja template*
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Welcome")


# Creates an about us page using the Jinja template*
@app.route('/about')
def about():
    return render_template('about.html', title="About Us")


# CREATES ERROR HANDLER (404 PAGE NOT FOUND)*
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found")


# CREATES ERROR HANDLER (405 METHOD NOT ALLOWED)
@app.errorhandler(405)
def invalid_token(e):
    return render_template('405.html', title="Method Not Allowed")


# Send information from navigation search bar (from all HTML pages)*
@app.context_processor
def layout():
    form = SearchForm()
    return dict(form=form)


# NAVIGATION BAR SEARCH FUNCTION (PRODUCES A LIST OF SEARCH RESULTS)*
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


# SEARCH ALL CUSTOMER-GENERAL QUERY-VICKI*
@app.route('/customers', methods=['GET'])
def show_customers():
    error = ""
    customers = service.get_all_customers()
    if len(customers) == 0:
        error = "There are no customers to display"
    #return render_template('customer.html', customers=customers, message=error, title="All Customer's Information")
    return jsonify(customers)


# SEARCH CUSTOMERS BY ID*
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
    return render_template('games.html', games=games, message=error, title="All Games", len=len(games))
    # return jsonify(games)


# SEARCH ALL REVIEWS-GENERAL QUERY-VICKI*
@app.route('/reviews', methods=['GET'])
def show_reviews():
    error = ""
    reviews = service.get_all_reviews()
    if len(reviews) == 0:
        error = "There are no reviews to display"
    #return render_template('customer.html', reviews=reviews, message=error, title="All Reviews")
    return jsonify(reviews)


# SEARCH ALL BOOKINGS - GENERAL QUERY - VICKI*
@app.route('/bookings', methods=['GET'])
def show_bookings():
    error = ""
    bookings = service.get_all_bookings()
    if len(bookings) == 0:
        error = "There are no bookings to display"
    #return render_template('customer.html', bookings=bookings, message=error, title="All Reviews")
    return jsonify(bookings)


# SEARCH ALL CAFESESSIONS - GENERAL QUERY - VICKI*
@app.route('/cafesessions', methods=['GET'])
def show_cafesessions():
    error = ""
    cafesessions = service.get_all_cafesessions()
    if len(cafesessions) == 0:
        error = "There are no cafesessions to display"
    #return render_template('customer.html', cafesessions=cafesessions, message=error, title="All Reviews")
    return jsonify(cafesessions)


# SEARCH ALL STOCK - GENERAL QUERY - VICKI*
@app.route('/stock', methods=['GET'])
def show_stock():
    error = ""
    stock = service.get_all_stock()
    if len(stock) == 0:
        error = "There is no stock to display"
    #return render_template('customer.html', stock=stock, message=error, title="All Reviews")
    return jsonify(stock)


# GET CUSTOMER ID FROM EMAIL - USED IN REVIEW & BOOKING FORM - VICKI*
@app.route('/customer/<email>', methods=['GET'])
def show_customer_details(email):
    error = ""
    customer = service.get_customer_by_email(email)
    if not customer:
        error = "There is no one with the email " + email
    else:
        for e in customer.email:
            return str(customer.customer_id)


# GET GAME ID BY GAME NAME - USED IN REVIEW & BOOKING FORM - VICKI
@app.route('/review_game/<game_name>', methods=['GET'])
def display_game_details(game_name):
    error = ""
    game = service.get_game_by_name(game_name)
    if not game:
        error = "There is no game called " + game_name
    return render_template('game.html', game=game, message=error, game_name=game_name, title=game.game_name)
    # return jsonify(game.game_id)


# ADD A NEW REVIEW USING WTF FORMS - VICKI*
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
            return render_template('review.html', customer_id=cust, stars=stars, game_id=game.game_id, message=error)
    return render_template('new_review_form.html', form=form, message=error)


# GET ALL CAFESESSION BY SESSION DATE AND SESSION TYPE - USED IN BOOKING WITH WTF FORMS - VICKI
@app.route('/cafesession/<session_date>', methods=['GET'])
def get_cafesession_by_date(session_date):
    error = ""
    cafesessions = service.get_cafesession_by_date(session_date)
    if not cafesessions:
        error = "There are no sessions to display"
    else:
        return jsonify(cafesessions)


# ADD A NEW BOOKING USING WTF FORMS - VICKI
@app.route('/new_booking', methods=['GET', 'POST'])
def add_new_booking():
    error = ""
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.form)
        game = form.game_list.data
        session_date = form.session_date_list.data
        session_type = form.session_list.data
        customer = form.email.data

        if not session_date:
            error = "Please select an available date"
        else:
            number_of_tables = 1
            # PULLS IN GAME ID FROM GAMES LIST
            service.show_game_details(game)
            # PULLS IN CUSTOMER ID FROM EMAIL
            cust = show_customer_details(customer)
            # PULLS IN SESSION ID
            get_cafesession_by_date(session_date)
            # ADDS THE BOOKING
            booking = Booking(stock_id=game.game_id, session_id=session_date.session_id, customer_id=cust, number_of_tables=number_of_tables)
            service.add_new_booking(booking)
            bookings = service.get_all_bookings()
            return render_template('booking.html', bookings=bookings, stock_id=game.game_id, session_id=session_date.session_id, customer_id=cust, number_of_tables=number_of_tables, message=error)

    return render_template('new_booking_form.html', game=Game, form=form, message=error)



# INDIVIDUAL GAMES - FAYE
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



# ADD NEW GAME FORM - AMY
@app.route('/new_game', methods=['GET','POST'])
def add_new_game():
    error = ""
    form = GameForm()

    if request.method == 'POST':
        form = GameForm(request.form)
        game_name = form.game_name.data
        num_of_players = form.num_of_players.data
        min_age = form.min_age.data
        duration_of_play_time = form.duration_of_play_time.data
        game_description = form.game_description.data
        gameplay = form.gameplay.data
        if len(game_name) == 0 or not num_of_players or not min_age or not duration_of_play_time:
            error = "Please supply all game details"
        else:
            game = Game(game_name=game_name, num_of_players=num_of_players,
                        min_age=min_age, duration_of_play_time=duration_of_play_time, gameplay=gameplay,
                        game_description=game_description)

            service.add_new_game(game)
            # games = service.get_all_games()
            return render_template('home.html')

    return render_template('new_game_form.html', form=form, message=error)

# Creates a menu page using the Jinja template* ADDED BY AMY 29/04/23
@app.route('/')
@app.route('/menu')
def menu():
    return render_template('menu.html', title="Menu")