create database boardgamecafe;
use boardgamecafe;

create table if not exists customer(
customer_id mediumint not null primary key auto_increment,
first_name varchar(50) not null,
last_name varchar(50) not null,
email varchar(50) not null,
phone_number varchar(20),
account_status enum("Active", "Disabled", "Closed") not null,
customer_password varchar(100) not null,
join_date date not null);

create table if not exists game(
game_id smallint not null primary key auto_increment,
game_name varchar(50) not null,
num_of_players smallint not null,
min_age smallint not null,
duration_of_play_time smallint not null,
gameplay enum("competitive", "co-operative"),
game_description text);

create table if not exists cafesession(
session_id mediumint not null auto_increment primary key,
session_type enum("Lunchtime", "Afternoon", "Evening") not null,
session_date date not null,
table_count smallint not null);

create table if not exists stock(
stock_id smallint not null auto_increment primary key,
game_id smallint not null, foreign key(game_id) references game(game_id));

create table if not exists review(
review_id mediumint not null auto_increment primary key,
review text(4000),
stars tinyint,
review_date date not null,
customer_id mediumint not null, foreign key(customer_id) references customer(customer_id),
game_id smallint not null, foreign key(game_id) references game(game_id));

create table if not exists booking(
booking_id mediumint not null primary key auto_increment,
-- table_total smallint not null,
-- guest_total smallint,
stock_id smallint, foreign key(stock_id) references stock(stock_id),
session_id mediumint not null, foreign key(session_id) references cafesession(session_id),
customer_id mediumint not null, foreign key(customer_id) references customer(customer_id),
number_of_tables tinyint);


-- Initial data imported into database
insert into customer values(1, "Melissa", "Rogen", "melissa.rogen@fakemail.com", "09745451215", "Active", "mypassword", "2023-04-10");
insert into customer values(2, "John", "Rogen", "john.rogen@fakemail.com", "09745174874", "Active", "mypassword", "2023-04-10");
insert into customer values(3, "Joel", "Takis", "joel.takis@fakemail.com", "09713914571", "Active", "mypassword", "2023-04-11");
insert into customer values(4, "Beth", "Moore", "beth.moore@fakemail.com", "09127984325", "Active", "mypassword", "2023-04-11");
insert into customer values(5, "David", "Smyth", "david.smyth@fakemail.com", "09314714987", "Active", "mypassword", "2023-04-11");
insert into customer values(6, "Liisa", "Virtanen", "liisa.virtanen@fakemail.com", "09651324987", "Active", "mypassword", "2023-04-11");
insert into customer values(7, "Olivia", "Moore", "olivia.moore@fakemail.com", "09754198211", "Active", "mypassword", "2023-04-12");
insert into customer values(8, "Isabella", "Davids", "isabella.davids@fakemail.com", "09445178451", "Active", "mypassword", "2023-04-12");
insert into customer values(9, "John", "Rogen", "john.rogen@fakemail.com", "09745174874", "Active", "mypassword", "2023-04-12");
insert into customer values(10, "Ahmed", "Aziz", "ahmed.aziz@fakemail.com", "09411214511", "Active", "mypassword", "2023-04-13");
insert into customer values(11, "Kelly", "Chadwick", "kelly.chadwick@fakemail.com", "09651324987", "Active", "mypassword", "2023-04-13");
insert into customer values(12, "Liam", "Thompson", "liam.munn@fakemail.com", "09541847514", "Active", "mypassword", "2023-04-13");
insert into customer values(13, "Andrzej", "Wojcik", "andrzej.wojcik@fakemail.com", "09332845196", "Active", "mypassword", "2023-04-13");
insert into customer values(14, "Andy", "Wright", "andy.wright@fakemail.com", "09654785144", "Active", "mypassword", "2023-04-14");
insert into customer values(15, "Noah", "Murphy", "noah.murphy@fakemail.com", "09654785144", "Active", "mypassword", "2023-04-14");
insert into customer values(16, "Jack", "Muller", "jack.muller@fakemail.com", "09654785144", "Active", "mypassword", "2023-04-14");
insert into customer values(17, "Felix", "Garcia", "felix.garcia@fakemail.com", "09654785144", "Active", "mypassword", "2023-04-14");
insert into customer values(18, "Ava", "Robinson", "ava.robinson@fakemail.com", "09654785144", "Active", "mypassword", "2023-04-14");
insert into customer values(19, "Ellie", "Hill", "ellie.hill@fakemail.com", "09654785144", "Active", "mypassword", "2023-04-14");
insert into customer values(20, "Sofia", "Garcia", "sofia.garcia@fakemail.com", "09654785144", "Active", "mypassword", "2023-04-14");

insert into game values(1, "Takenoko", 4, 8, 45, "competitive", "A long time ago at the Japanese Imperial court, the Chinese Emperor offered a giant panda bear as a symbol of peace to the Japanese Emperor. Since then, the Japanese Emperor has entrusted his court members (the players) with the difficult task of caring for the animal by tending to his bamboo garden.
In Takenoko, the players will cultivate land plots, irrigate them, and grow one of the three species of bamboo (Green, Yellow, and Pink) with the help of the Imperial gardener to maintain this bamboo garden. They will have to bear with the immoderate hunger of this sacred animal for the juicy and tender bamboo. The player who manages his land plots best, growing the most bamboo while feeding the delicate appetite of the panda, will win the game.
");
insert into game values(2, "Catan", 4, 10, 90, "competitive", "In CATAN players try to be the dominant force on the island of Catan by building settlements, cities, and roads. On each turn dice are rolled to determine what resources the island produces. Players build by spending resources (sheep, wheat, wood, brick and ore) that are depicted by these resource cards; each land type, with the exception of the unproductive desert, produces a specific resource: hills produce brick, forests produce wood, mountains produce ore, fields produce wheat, and pastures produce sheep.
Setup includes randomly placing large hexagonal tiles (each showing a resource or the desert) in a honeycomb shape and surrounding them with water tiles, some of which contain ports of exchange. Number disks, which will correspond to die rolls (two 6-sided dice are used), are placed on each resource tile. Each player is given two settlements (think: houses) and roads (sticks) which are, in turn, placed on intersections and borders of the resource tiles. Players collect a hand of resource cards based on which hex tiles their last-placed house is adjacent to. A robber pawn is placed on the desert tile.
A turn consists of possibly playing a development card, rolling the dice, everyone (perhaps) collecting resource cards based on the roll and position of houses (or upgraded cities—think: hotels) unless a 7 is rolled, turning in resource cards (if possible and desired) for improvements, trading cards at a port, and trading resource cards with other players. If a 7 is rolled, the active player moves the robber to a new hex tile and steals resource cards from other players who have built structures adjacent to that tile.
Points are accumulated by building settlements and cities, having the longest road and the largest army (from some of the development cards), and gathering certain development cards that simply award victory points. When a player has gathered 10 points (some of which may be held in secret), he announces his total and claims the win.
");
insert into game values(3, "Wingspan", 5, 10, 60, "competitive","Wingspan is a competitive, medium-weight, card-driven, engine-building board game from Stonemaier Games. It's designed by Elizabeth Hargrave and features over 170 birds illustrated by Beth Sobel, Natalia Rojas, and Ana Maria Martinez.
You are bird enthusiasts—researchers, bird watchers, ornithologists, and collectors—seeking to discover and attract the best birds to your network of wildlife preserves. Each bird extends a chain of powerful combinations in one of your habitats (actions). These habitats focus on several key aspects of growth: gain food tokens via custom dice in a birdfeeder dice tower, lay eggs using egg miniatures in a variety of colours, draw from hundreds of unique bird cards and play them
The winner is the player with the most points after 4 rounds.
");
insert into game values(4, "Herbaceous", 4, 8, 20, "competitive", "In Herbaceous, herb collectors compete to grow and store the most valuable medley of herbs. Everyone starts with four containers, each of which allows a different grouping action: group herbs of same type, group different types, group pairs, group any three types (same or different).
On your turn, you draw a herb, then decide to either keep it in your personal collection or put in into the communal pile. If kept, the next card goes to the communal pile; if placed in the communal pile, the next card goes in your personal collection.
At the start of your turn, you can decide to use a container. If so, you assemble cards from personal and communal spaces, group them, then turn them all over. You have then collected those and can't use the container again.
At the end of the game, collectors determine the best collection as a combination of value from their collection, matching herbs, and herb sets.
");
insert into game values(5, "Castle Panic", 6, 10, 60, "co-operative", "The forest is filled with all sorts of monsters. They watched and waited as you built your castle and trained your soldiers, but now they've gathered their army and are marching out of the woods. Can you work with your friends to defend your castle against the horde, or will the monsters tear down your walls and destroy the precious castle towers? You will all win or lose together, but in the end only one player will be declared the Master Slayer!
Castle Panic is a Fantasy themed, cooperative, light tactical wargame for 1 to 6 players ages 10 and up. Players must work together to defend their castle, in the centre of the board, from monsters that attack out of the forest at the edges of the board. Players trade cards, hit and slay monsters, and plan tactics together to keep their castle towers intact. The players either win or lose together, but only the player with the most victory points is declared the Master Slayer. Players must balance the survival of the group with their own desire to win.
");
insert into game values(6, "Stratego", 2, 8, 45, "competitive", "The gameboard is your battlefield. You have an army of men at your disposal and six bombs. Your mission--protect your flag and capture your opponent's flag.
Secretly place your men, bombs, and flag on the gameboard with these objectives in mind. But remember your opponent is doing the same thing, so you must plan a defense as well as an offense.
Once the armies are in place, advance your men. When you're one space away from an enemy, attack. You and your opponent declare ranks. The lower-ranking man is captured and out of play.
You control your pieces and risk your men in battles where the strength of your enemy is unknown. The suspense builds as your men move deeper into enemy territory. Move with caution and courage. The next piece you attack could be a bomb. And when attacked, it could blast your man off the board and out of play.
The first to capture an enemy flag is the winner!
");
insert into game values(7, "Lost Cities", 2, 10, 30, "competitive", "The object of the game is to gain points by mounting profitable archaeological expeditions to the different sites represented by the coloured suits of cards. On a player's turn, they must first play one card, either to an expedition or by discarding it to the colour-appropriate discard pile, then draw one card, either from the deck or from the top of a discard pile. Cards played to expeditions must be in ascending order, but they need not be consecutive. Handshakes are considered lower than a 2 and represent investments in an expedition. Thus, if you play a red 4, you may play any other red card higher than a 4 on a future turn but may no longer play a handshake, the 2, or the 3.
The game continues in this fashion with players alternating turns until the final card is taken from the deck. The rest of the cards in hand are then discarded and players score their expeditions. Each expedition that has at least one card played into it must be scored. Cards played into an expedition are worth their rank in points, and handshakes count as a multiplier against your final total; one handshake doubles an expedition's value, while two handshakes triples that value and three handshakes quadruple it. Expeditions start at a value of -20, so you must play at least 20 points of cards into an expedition in order to make a profit. If you are left with a negative value and have a handshake, the multiplier still applies. A 20-point bonus is awarded to every expedition with at least eight cards played into it. A complete game of Lost Cities lasts three matches, with scores for each match being added together.
Scoring example 1: An expedition has a 2,3,7,8,10 for a total of 30. This expedition is worth 10 total points: 30 plus the initial -20.
Scoring example 2: An expedition has 2 HS, and 4,5,6,7,8,10 for a total of 40. This expedition is worth 80 total points: 40 points for cards, plus the initial -20, ×3 for the two multipliers, plus the 20-pt bonus for playing 8+ cards.
Scoring example 3: An expedition has 1 HS, and 4,6,7 for a total of 17. This expedition is worth -6 total points: 17 plus the initial -20, ×2 for the multiplier.
");
insert into game values(8, "Qwirkle", 4, 6, 40, "competitive", "The abstract game of Qwirkle consists of 108 wooden blocks with six different shapes in six different colours. There is no board, players simply use an available flat surface.
Players begin the game with six blocks. The start player places blocks of a single matching attribute (colour or shape but not both) on the table. Thereafter, a player adds blocks adjacent to at least one previously played block. The blocks must all be played in a line and match, without duplicates, either the colour or shape of the previous block.
Players score one point for each block played plus all blocks adjacent. It is possible for a block to score in more than one direction. If a player completes a line containing all six shapes or colours, an additional six points are scored. The player then refills his hand to six blocks.
The game ends when the draw bag is depleted and one player plays all of his remaining blocks, earning a six point bonus. The player with the high score wins.
");
insert into game values(9, "Hive", 2, 9, 20, "competitive", "Hive is a strategic game for two players that is not restricted by a board and can be played anywhere on any flat surface. Hive is made up of twenty two pieces, eleven black and eleven white, resembling a variety of creatures each with a unique way of moving.
With no setting up to do, the game begins when the first piece is placed down. As the subsequent pieces are placed this forms a pattern that becomes the playing surface (the pieces themselves become the board). Unlike other such games, the pieces are never eliminated and not all have to be played. The object of the game is to totally surround your opponent's queen, while at the same time trying to block your opponent from doing likewise to your queen. The player to totally surround his opponent's queen wins the game.
");
insert into game values(10, "Santorini", 2, 8, 20, "competitive", "Santorini is a re-imagining of the purely abstract 2004 edition. Since its original inception over 30 years ago, Santorini has been continually developed, enhanced and refined by designer Gordon Hamilton.
Santorini is an accessible strategy game, simple enough for an elementary school classroom while aiming to provide gameplay depth and content for hardcore gamers to explore, The rules are simple. Each turn consists of 2 steps:
1. Move - move one of your builders into a neighboring space. You may move your Builder Pawn on the same level, step-up one level, or step down any number of levels.
2. Build - Then construct a building level adjacent to the builder you moved. When building on top of the third level, place a dome instead, removing that space from play.
Winning the game - If either of your builders reaches the third level, you win.
Variable player powers - Santorini features variable player powers layered over an otherwise abstract game, with 40 thematic god and hero powers that fundamentally change the way the game is played.
");
insert into game values(11, "Sagrada", 4, 14, 40, "competitive", "Draft dice and use the tools-of-the-trade in Sagrada to carefully construct your stained glass window masterpiece.
In more detail, each player builds a stained glass window by building up a grid of dice on their player board. Each board has some restrictions on which colour or shade (value) of die can be placed there. Dice of the same shade or colour may never be placed next to each other. Dice are drafted in player order, with the start player rotating each round, snaking back around after the last player drafts two dice. Scoring is variable per game based on achieving various patterns and varieties of placement...as well as bonus points for dark shades of a particular hidden goal colour.
Special tools can be used to help you break the rules by spending skill tokens; once a tool is used, it then requires more skill tokens for the other players to use them.
The highest scoring window artisan wins!
");
insert into game values(12, "Azul", 4, 8, 40, "competitive", "Introduced by the Moors, azuleijos (originally white and blue ceramic tiles) were fully embraced by the Portuguese when their king Manuel I, on a visit to the Alhambra palace in Southern Spain, was mesmerized by the stunning beauty of the Moorish decorative tiles. The king, awestruck by the interior beauty of the Alhambra, immediately ordered that his own palace in Portugal be decorated with similar wall tiles. As a tile-laying artist, you have been challenged to embellish the walls of the Royal Palace of Evora.
In the game Azul, players take turns drafting coloured tiles from suppliers to their player board. Later in the round, players score points based on how they've placed their tiles to decorate the palace. Extra points are scored for specific patterns and completing sets; wasted supplies harm the player's score. The player with the most points at the end of the game wins.
");
insert into game values(13, "Backgammon", 2, 8, 30, "competitive", "Backgammon is a classic abstract strategy game dating back thousands of years. Each player has a set of 15 checkers (or stones) that must be moved from their starting positions, around, and then off the board. Dice are thrown each turn, and each player must decide which of their checkers to move based on the outcome of the roll. Players can capture each other's checkers, forcing the captured checkers to restart their journey around the board. The winner is the first player to get all 15 checkers off the board. A more recent addition to the game is the doubling cube, which allows players to up the stakes of the game. Although the game relies on dice to determine movement, there is a large degree of strategy in deciding how to make the most effective moves given each dice roll and measuring the risk in terms of possible rolls the opponent may get.");
insert into game values(14, "Hanabi", 5, 8, 30, "co-operative", "Hanabi—named for the Japanese word for fireworks—is a cooperative game in which players try to create the perfect fireworks show by placing the cards on the table in the right order.
The card deck consists of five different colours of cards, numbered 1–5 in each colour. For each colour, the players try to place a row in the correct order from 1–5. Sounds easy, right? Well, not quite, as in this game you hold your cards so that they're visible only to other players. To assist other players in playing a card, you must give them hints regarding the numbers or the colours of their cards. Players must act as a team to avoid errors and to finish the fireworks display before they run out of cards.
An extra suit of cards, rainbow coloured, is also provided for advanced or variant play.
");
insert into game values(15, "Forbidden Island", 4, 10, 30, "co-operative", "Dare to discover Forbidden Island! Join a team of fearless adventurers on a do-or-die mission to capture four sacred treasures from the ruins of this perilous paradise. Your team will have to work together and make some pulse-pounding manoeuvres, as the island will sink beneath every step! Race to collect the treasures and make a triumphant escape before you are swallowed into the watery abyss!");

insert into cafesession values(1, "Lunchtime", "2023-04-30", 19);
insert into cafesession values(2, "Afternoon", "2023-04-30", 20);
insert into cafesession values(3, "Evening", "2023-04-30", 20);
insert into cafesession values(4, "Lunchtime", "2023-05-01", 20);
insert into cafesession values(5, "Afternoon", "2023-05-01", 20);
insert into cafesession values(6, "Evening", "2023-05-01", 20);
insert into cafesession values(7, "Lunchtime", "2023-05-02", 20);
insert into cafesession values(8, "Afternoon", "2023-05-02", 20);
insert into cafesession values(9, "Evening", "2023-05-02", 20);
insert into cafesession values(10, "Lunchtime", "2023-05-03", 20);
insert into cafesession values(11, "Afternoon", "2023-05-03", 20);
insert into cafesession values(12, "Evening", "2023-05-03", 20);
insert into cafesession values(13, "Lunchtime", "2023-05-04", 20);
insert into cafesession values(14, "Afternoon", "2023-05-04", 20);
insert into cafesession values(15, "Evening", "2023-05-04", 20);
insert into cafesession values(16, "Lunchtime", "2023-05-05", 20);
insert into cafesession values(17, "Afternoon", "2023-05-05", 20);
insert into cafesession values(18, "Evening", "2023-05-05", 20);
insert into cafesession values(19, "Lunchtime", "2023-05-06", 20);
insert into cafesession values(20, "Afternoon", "2023-05-06", 20);
insert into cafesession values(21, "Evening", "2023-05-06", 20);
insert into cafesession values(22, "Lunchtime", "2023-05-07", 20);
insert into cafesession values(23, "Afternoon", "2023-05-07", 20);
insert into cafesession values(24, "Evening", "2023-05-07", 20);
insert into cafesession values(25, "Lunchtime", "2023-05-08", 20);
insert into cafesession values(26, "Afternoon", "2023-05-08", 20);
insert into cafesession values(27, "Evening", "2023-05-08", 20);

insert into stock values(1, 1);
insert into stock values(2, 2);
insert into stock values(3, 3);
insert into stock values(4, 4);
insert into stock values(5, 5);
insert into stock values(6, 6);
insert into stock values(7, 7);
insert into stock values(8, 8);
insert into stock values(9, 9);
insert into stock values(10, 10);
insert into stock values(11, 11);
insert into stock values(12, 12);
insert into stock values(13, 13);
insert into stock values(14, 14);
insert into stock values(15, 15);

insert into review values(1, "Great game!", 5, "2023-04-15", 1, 1);
insert into review values(2, "Loved playing this game, its great to play multiple times and really makes you think", 5, "2022-06-25", 7, 14);
insert into review values(3, "Didn't like this game it was too hard!", 2, "2022-12-1", 9, 11);
insert into review values(4, "Good afternoon playing this game, it was a bit difficult for my children but we loved it!", 4, "2023-02-18", 12, 2);
insert into review values(5, "Found this game a little repetitive and boaring", 2, "2022-08-23", 19, 3);
insert into review values(6, "Fab game....Loved it!", 5, "2022-12-30", 17, 9);
insert into review values(7, "The whole family loved this game, we had so much fun playing!", 5, "2023-02-17", 4, 6);
insert into review values(8, "This game is rubbish!", 1, "2022-05-30", 20, 13);
insert into review values(9, "Really good fun!", 5, "2023-02-19", 11, 15);
insert into review values(110, "Good family game!", 4, "2022-09-4", 5, 8);

-- typo in last review so updated it
update review set review_id = 10 where review_id = 110;


insert into booking values(1, 1, 1, 1, 1);