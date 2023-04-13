create database BoardgameCafe;
use BoardgameCafe;

create table if not exists customer(
customer_id smallint not null primary key auto_increment,
first_name varchar(50) not null,
last_name varchar(50) not null,
email varchar(50) not null,
phone_number varchar(11),
account_status enum("Active", "Disabled", "Closed") not null,
customer_password varchar(20) not null,
join_date date not null);

create table if not exists game(
game_id smallint not null primary key auto_increment,
game_name varchar(50) not null,
num_of_players smallint not null,
min_age smallint not null,
duration_of_play_time smallint not null,
gameplay enum('competitive', 'co-operative'));

create table if not exists session(
session_id smallint not null auto_increment primary Key,
session_type enum("Lunchtime", "Afternoon", "Evening") not null,
session_date date not null,
table_count smallint not null);

create table if not exists stock(
stock_id smallint not null auto_increment primary key,
game_id smallint not null, foreign key(game_id) references game(game_id));

create table if not exists booking(
booking_id smallint not null primary key auto_increment,
customer_id smallint not null, foreign key(customer_id) references customer(customer_id),
session_id smallint not null, foreign key(session_id) references session(session_id),
stock_id smallint, foreign key(stock_id) references stock(stock_id));

create table if not exists review(
review_id smallint not null auto_increment primary key,
customer_id smallint not null, foreign key(customer_id) references customer(customer_id),
review text(4000),
stars tinyint,
game_id smallint not null, foreign key(game_id) references game(game_id),
review_date date not null);

insert into game values(1, "Takenoko", 4, 8, 45, 'competitive');
insert into game values(2, "Catan", 4, 10, 90, 'competitive');
insert into game values(3, "Wingspan", 5, 10, 60, 'competitive');
insert into game values(4, "Catan", 4, 10, 90, 'competitive');
insert into game values(5, "Castle Panic", 6, 10, 60, 'co-operative');
insert into game values(6, "Stratego", 2, 8, 45, 'competitive');
insert into game values(7, "Lost Cities", 2, 10, 30, 'competitive');
insert into game values(8, "Quirkle", 4, 6, 40, 'competitive');
insert into game values(9, "Hive", 2, 9, 20, 'competitive');
insert into game values(10, "Santorini", 2, 8, 20, 'competitive');
insert into game values(11, "Sagrada", 4, 14, 40, 'competitive');
insert into game values(12, "Azul", 4, 8, 40, 'competitive');
insert into game values(13, "Backgammon", 2, 8, 30, 'competitive');
insert into game values(14, "Hanabi", 5, 8, 30, 'co-operative');
insert into game values(15, "Forbidden Island", 4, 10, 30, 'co-operative');



  