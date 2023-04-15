use boardgamecafe;

-- Select tables
select * from customer;
select * from game;
select * from cafesession;
select * from stock;
select * from review;
select * from booking;

-- Drop tables (no warning given!)
drop table customer;
drop table game;
drop table cafesession;
drop table stock;
drop table review;
drop table booking;

-- Delete the entire database (no warning given!)
drop database boardgamecafe;
