use BoardgameCafe;
-- random queries to check working
select booking_id, first_name, last_name, session_date, session_type from customer join booking on booking.customer_id = customer.customer_id join cafesession on cafesession.session_id = booking.session_id;

select booking_id, first_name, last_name, game_name, session_date, session_type from booking join cafesession on cafesession.session_id = booking.session_id join stock on stock.stock_id = booking.stock_id join game on game.game_id = stock.game_id join customer on customer.customer_id = booking.customer_id; 

select stars, game_name, review from review join game on game.game_id = review.game_id where stars = 5;
