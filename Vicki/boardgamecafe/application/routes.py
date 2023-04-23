from flask import render_template, jsonify, request
from application.models.booking import Booking
from application.models.cafesession import Cafesession
from application.models.customer import Customer
from application.models.game import Game
from application.models.review import Review
from application.models.stock import Stock
from application.forms.ReviewForm import ReviewForm
from application.forms.BookingForm import BookingForm
import datetime
from application.forms.game_search import SearchForm
from application import db

from application import app, service


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
        result = service.get_game_by_name(title_search)
        return render_template('search.html', searched=result, title='Search Results')


# ALL CUSTOMER
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
    #return render_template('customer.html', customers=customers, message=error, title="All Games")
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


# GET GAME BY GAME NAME(USED IN REVIEW)
@app.route('/games/<game_name>', methods=['GET'])
def show_game_details(game_name):
    error = ""
    game = service.get_game_by_name(game_name)
    if not game:
        error = "There is no game called " + game_name
    return render_template('game.html', game=game, message=error, game_name=game_name, title=game.game_name)
    # return jsonify(game)


# GET CUSTOMER ID FROM EMAIL(FOR REVIEW)
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


# ADD NEW BOOKING
@app.route('/new_booking', methods=['GET', 'POST'])
def add_new_booking():
    error = ""
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.form)
        stock_id = form.stock_id.data
        session_id = form.session_id.data
        customer_id = form.customer_id.data
        number_of_tables = form.number_of_tables.data
        session = form.session_list.data
        customer = form.customer_list.data
        stock = form.stock_list.data
        if len(customer_id) == 0:
            error = "Please insert you customer ID"
        else:
            booking = Booking(stock_id=stock_id, session_id=session_id,
                        customer_id=customer_id, number_of_tables=number_of_tables)
            service.add_new_booking(booking)
            booking = service.get_all_bookings()
            return render_template('booking.html', booking=booking, message=error, stock_id=stock_id, session_id=session_id,
                        customer_id=customer_id, number_of_tables=number_of_tables)

    return render_template('new_booking_form.html', form=form, message=error)


