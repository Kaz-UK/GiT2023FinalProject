from flask import render_template, jsonify, request, redirect, url_for, flash

from application.models.booking import Booking
from application.models.cafesession import Cafesession
from application.models.customer import Customer
from application.models.game import Game
from application.models.review import Review
from application.models.stock import Stock

from application import app, service, db
# from flask_wtf import FlaskForm
import datetime

from application.forms.ReviewForm import ReviewForm
from application.forms.BookingForm import BookingForm
from application.forms.SearchForm import SearchForm
from application.forms.RegistrationForm import RegistrationForm
from application.forms.LoginForm import LoginForm
from application.forms.SessionForm import SessionForm
from application.forms.GameForm import GameForm

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user


# HOMEPAGE
@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title="Welcome")


# ABOUT US PAGE
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title="About Us")


# FOOD & DRINK PAGE
@app.route('/food-and-drink', methods=['GET'])
def menu():
    return render_template('food-and-drink.html', title="Food and Drink")


# ERROR PAGE
@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html', title="Error")


# CREATES ERROR HANDLER - 401 UNAUTHORISED
@app.errorhandler(401)
def invalid_token(e):
    return render_template('401.html', title="Unauthorised")


# CREATES ERROR HANDLER - 404 PAGE NOT FOUND
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found")


# CREATES ERROR HANDLER - 405 METHOD NOT ALLOWED
@app.errorhandler(405)
def invalid_token(e):
    return render_template('405.html', title="Method Not Allowed")


# NAVIGATION SEARCH BAR - CONTEXT PROCESSOR (KAREN)
@app.context_processor
def layout():
    form = SearchForm()
    return dict(form=form)


# NAVIGATION BAR SEARCH FUNCTION (KAREN)
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


# ALL GAMES (AMY)
@app.route('/games', methods=['GET'])
def show_games():
    error = ""
    games = service.get_all_games()
    if len(games) == 0:
        error = "There are no games to display"
    return render_template('games.html', games=games, message=error, title="All Games")


# INDIVIDUAL GAMES (FAYE)
@app.route('/games/<game_name>', methods=['GET'])
def show_game_details(game_name):
    error = ""
    game = service.get_game_by_name(game_name)
    reviews_for_game = service.get_reviews_by_game_id(game.game_id)
    coop_games = service.search_by_gameplay('co-operative')
    two_player_games = service.search_games_by_num_of_players(2)
    first_names = []
    if not game:
        error = "There is no game called " + game_name
    else:
        for rev in reviews_for_game:
            customer = service.get_customer_by_customer_id(rev.customer_id)
            first_names.append(customer.first_name)
    return render_template('game.html', game=game, message=error, game_name=game_name, game_id=str(game.game_id),
                            first_names=first_names, reviews_for_game=reviews_for_game,
                           two_player_games=two_player_games, coop_games=coop_games, title=game.game_name)


# ADD NEW CUSTOMER (KAREN)
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.form)
        email = form.email.data
        join_date = datetime.date.today()
        if form.validate_on_submit():
            existing_customer = service.check_email_status(email)
            if existing_customer is None:
                # Password is hashed for security
                hashed_password = generate_password_hash(form.customer_password.data, "sha256")
                user = Customer(first_name=form.first_name.data, last_name=form.last_name.data, email=email,
                                phone_number=form.phone_number.data, account_status="Active",
                                customer_password=hashed_password, join_date=join_date)
                service.add_new_customer(user)
                login_user(user)
                flash("Sign up successful. Welcome to Roll With It!")
                return redirect(url_for('customer'))
            else:
                flash("An account with this email already exists")
                return redirect(url_for('register'))
        else:
            flash("There was an error with your registration, please ensure your passwords match")
            return redirect(url_for('register'))
    return render_template('registration.html', form=form, title="Register")


# LOGIN (KAREN)
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        customer = service.get_customer_by_email(form.email.data)
        if customer:
            # Check the password hash
            if check_password_hash(customer.customer_password, form.password.data):
                login_user(customer)
                if customer.email == "admin@kafv.co.uk":
                    return redirect(url_for('admin'))
                else:
                    return redirect(url_for('customer'))
            else:
                flash("Incorrect password")
                return redirect(url_for('login'))
        else:
            flash("Email does not exist")
            return redirect(url_for('login'))
    return render_template('login.html', form=form, title="Login")


# LOGOUT (KAREN)
@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return render_template('home.html')


# ADD A NEW BOOKING (VICKI/KAREN)
@app.route('/customer/booking', methods=['GET', 'POST'])
def add_booking():
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.form)
        session_information = form.session_date_list.data
        game = form.game_list.data
        if form.validate_on_submit():
            cust = service.get_customer_by_email(form.email.data)
            if cust:
                if session_information.table_count == 0:
                    flash("Sorry, this session is fully booked.")
                    return redirect(url_for('add_booking'))
                if game is None:
                    booking = Booking(session_id=session_information.session_id, customer_id=cust.customer_id,
                                      number_of_tables=1)
                else:
                    booking = Booking(stock_id=game.game_id, session_id=session_information.session_id,
                                      customer_id=cust.customer_id, number_of_tables=1)
                try:
                    service.add_new_booking(booking)
                    service.update_table_count(session_information.session_id)
                    return redirect(url_for('booking_confirmation'))
                except:
                    flash("There was a problem with your booking.")
                    return redirect(url_for('add_booking'))
            else:
                flash("Your email is not in our database. Please sign up before booking.")
                return redirect(url_for('add_booking'))
    return render_template('booking.html', form=form, message=error, title="Book")


# BOOKING CONFIRMATION
@app.route('/customer/booking/booking-confirmation', methods=['GET'])
def booking_confirmation():
    return render_template('booking-confirmation.html', title="Booking Confirmed")


# CUSTOMER DASHBOARD (KAREN)
@app.route('/customer', methods=['GET'])
@login_required
def customer():
    booking_list = service.get_bookings(current_user.customer_id)
    review_list = service.get_reviews(current_user.customer_id)
    return render_template('customer.html', bookings=booking_list, reviews=review_list, title="Customer Dashboard")


# ADD A REVIEW (KAREN)
@app.route('/review', methods=['GET'])
def review():
    if current_user.is_authenticated:
        return redirect(url_for('add_review'))
    else:
        flash("You need to login to write a review")
        return redirect(url_for('login'))


# CUSTOMER DASHBOARD - ADD A NEW REVIEW (VICKI)
@app.route('/customer/add-review', methods=['GET', 'POST'])
@login_required
def add_review():
    if current_user:
        error = ""
        form = ReviewForm()
        if request.method == 'POST':
            form = ReviewForm(request.form)
            review = form.review.data
            stars = form.stars.data
            review_date = datetime.date.today()
            game = form.game_list.data
            # if not stars:
            #     error = "Please give a review"
            # else:
            if form.validate_on_submit():
                review_details = Review(review=review, stars=stars, review_date=review_date,
                                        customer_id=current_user.customer_id, game_id=game.game_id)
                service.add_new_review(review_details)
                flash("Review submitted successfully")
                return redirect(url_for('customer'))
            else:
                flash("There was an error submitting your review")
                return redirect((url_for('add_review')))
        return render_template('add-review.html', message=error, form=form, title="Add Review")


# CUSTOMER DASHBOARD - DELETE A BOOKING (KAREN)
@app.route('/customer/delete-booking/<int:booking_id>')
@login_required
def delete_booking(booking_id):
    delete_booking_id = service.get_booking_by_id(booking_id)
    if current_user.customer_id == delete_booking_id.customer_id:
        session_info = service.get_session_by_id(delete_booking_id.session_id)
        try:
            # service.add_table_count(session_info.session_id)
            service.delete_booking(delete_booking_id, session_info.session_id)
            return redirect(url_for('customer'))
        except:
            flash("There was an error deleting your booking. If this persists, please contact us.")
            return redirect(url_for('error'))
    else:
        return render_template('401.html', title="Unauthorised")


# CUSTOMER DASHBOARD - DELETE A REVIEW (KAREN)
@app.route('/customer/delete-review/<int:review_id>')
@login_required
def delete_review(review_id):
    delete_review_id = service.get_review_by_id(review_id)
    if current_user.customer_id == delete_review_id.customer_id:
        try:
            service.delete_review(delete_review_id)
            return redirect(url_for('customer'))
        except:
            return redirect(url_for('405'))
    else:
        return render_template('401.html', title="Unauthorised")


# ADMIN DASHBOARD (KAREN)
@app.route('/admin', methods=['GET'])
@login_required
def admin():
    if current_user.email == "admin@kafv.co.uk":
        game_stock = service.get_game_stock()
        return render_template('admin.html', results=game_stock, title="Admin Dashboard")
    else:
        return redirect(url_for('401'))


# ADMIN - ADDING A SESSION (FAYE)
@app.route('/admin/add-session', methods=['GET', 'POST'])
@login_required
def add_session():
    if current_user.email == "admin@kafv.co.uk":
        form = SessionForm()
        if request.method == 'POST':
            form = SessionForm(request.form)
            date = form.session_date.data
            session_type = form.session_type.data
            tables = form.table_count.data
            session = Cafesession(session_type=session_type, session_date=date, table_count=tables)
            service.add_new_session(session)
            flash("Session added successfully")
            return redirect(url_for('admin'))
        return render_template('add-session.html', form=form, title="Add Session")
    else:
        return render_template('401.html', title="Unauthorised")


# ADD NEW GAME FORM (AMY)
@app.route('/admin/add-game', methods=['GET','POST'])
@login_required
def add_new_game():
    if current_user.email == "admin@kafv.co.uk":
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
                flash("Game added successfully")
                redirect(url_for('add_new_game'))
            else:
                game = Game(game_name=game_name, num_of_players=num_of_players,
                            min_age=min_age, duration_of_play_time=duration_of_play_time, gameplay=gameplay,
                            game_description=game_description)
                service.add_new_game(game)
                add_stock = Stock(game_id=game.game_id)
                service.add_stock(add_stock)
                flash("Game added successfully")
            return redirect(url_for('admin'))
        return render_template('add-game.html', form=form, title="Add Game")
    else:
        return render_template('401.html', title="Unauthorised")


# ADMIN - VIEW BOOKINGS (VICKI)
@app.route('/admin/bookings', methods=['GET'])
@login_required
def get_bookings():
    if current_user.email == "admin@kafv.co.uk":
        return render_template('bookings.html', title="Admin Dashboard")
    else:
        return render_template('401.html', title="Unauthorised")


# # SEARCH ALL REVIEWS-GENERAL QUERY (VICKI)
# @app.route('/reviews', methods=['GET'])
# def show_reviews():
#     error = ""
#     reviews = service.get_all_reviews()
#     if len(reviews) == 0:
#         error = "There are no reviews to display"
#     #return render_template('customer.html', reviews=reviews, message=error, title="All Reviews")
#     return jsonify(reviews)
#
#
# # SEARCH ALL BOOKINGS - GENERAL QUERY (VICKI)*
# @app.route('/bookings', methods=['GET'])
# def show_bookings():
#     error = ""
#     bookings = service.get_all_bookings()
#     if len(bookings) == 0:
#         error = "There are no bookings to display"
#     #return render_template('customer.html', bookings=bookings, message=error, title="All Reviews")
#     return jsonify(bookings)
#
#
# # SEARCH ALL CAFESESSIONS - GENERAL QUERY (VICKI)*
# @app.route('/cafesessions', methods=['GET'])
# def show_cafesessions():
#     error = ""
#     cafesessions = service.get_all_cafesessions()
#     if len(cafesessions) == 0:
#         error = "There are no cafesessions to display"
#     #return render_template('customer.html', cafesessions=cafesessions, message=error, title="All Reviews")
#     return jsonify(cafesessions)
#
#
# # SEARCH ALL STOCK - GENERAL QUERY (VICKI)*
# @app.route('/stock', methods=['GET'])
# def show_stock():
#     error = ""
#     stock = service.get_all_stock()
#     if len(stock) == 0:
#         error = "There is no stock to display"
#     # return render_template('customer.html', stock=stock, message=error, title="All Reviews")
#     return jsonify(stock)
#
#
# GET GAME BY GAME NAME (USED IN REVIEW) - THIS DOESN'T SEEM TO BE IN USE
# @app.route('/games/<game_name>', methods=['GET'])
# def show_game_details(game_name):
#     error = ""
#     game = service.get_game_by_name(game_name)
#     if not game:
#         error = "There is no game called " + game_name
#     return render_template('game.html', game=game, message=error, game_name=game_name, title=game.game_name)
#     # return jsonify(game)
#
#
# # SEARCH ALL CUSTOMER-GENERAL QUERY (VICKI)*
# @app.route('/customers', methods=['GET'])
# def show_customers():
#     customers = service.get_all_customers()
#     if len(customers) == 0:
#         error = "There are no customers to display"
#     return jsonify(customers)
#
#
# # SEARCH CUSTOMERS
# @app.route('/customers/<int:customer_id>', methods=['GET'])
# def show_customer(customer_id):
#     customer = service.get_customer_by_id(customer_id)
#     if not customer:
#         return jsonify("There is no customer with ID: " + str(customer_id))
#     else:
#         print(customer.first_name, customer.last_name)
#     return jsonify(customer)# # SEARCH ALL CUSTOMER-GENERAL QUERY (VICKI)*
# # @app.route('/customers', methods=['GET'])
# # def show_customers():
# #     customers = service.get_all_customers()
# #     if len(customers) == 0:
# #         error = "There are no customers to display"
# #     return jsonify(customers)
#
#
# # # SEARCH CUSTOMERS
# # @app.route('/customers/<int:customer_id>', methods=['GET'])
# # def show_customer(customer_id):
# #     customer = service.get_customer_by_id(customer_id)
# #     if not customer:
# #         return jsonify("There is no customer with ID: " + str(customer_id))
# #     else:
# #         print(customer.first_name, customer.last_name)
# #     return jsonify(customer)
#
#
# # GET ALL CAFESESSION BY SESSION DATE AND SESSION TYPE - USED IN BOOKING WITH WTF FORMS (VICKI)
# @app.route('/cafesession/<session_date>', methods=['GET'])
# def get_cafesession_by_date(session_date):
#     error = ""
#     cafesessions = service.get_cafesession_by_date(session_date)
#     if not cafesessions:
#         error = "There are no sessions to display"
#     else:
#         return jsonify(cafesessions)
#
#
# # GET CUSTOMER ID FROM EMAIL - USED IN REVIEW & BOOKING FORM (VICKI)*
# @app.route('/customer/<email>', methods=['GET'])
# def show_customer_details(email):
#     error = ""
#     customer = service.get_customer_by_email(email)
#     if not customer:
#         error = "There is no one with the email " + email
#     else:
#         for e in customer.email:
#             return str(customer.customer_id)
#
#
# # GET GAME ID BY GAME NAME - USED IN REVIEW & BOOKING FORM (VICKI)
# @app.route('/review_game/<game_name>', methods=['GET'])
# def display_game_details(game_name):
#     error = ""
#     game = service.get_game_by_name(game_name)
#     if not game:
#         error = "There is no game called " + game_name
#     return render_template('game.html', game=game, message=error, game_name=game_name, title=game.game_name)