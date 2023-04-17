use BoardgameCafe;

create user webconnection@localhost identified by 'KHAFV';

grant select on BoardgameCafe.* to webconnection@localhost;
grant insert on BoardgameCafe.* to webconnection@localhost;
grant update on BoardgameCafe.* to webconnection@localhost;
grant delete on BoardgameCafe.customer to webconnection@localhost;
grant delete on BoardgameCafe.booking to webconnection@localhost;
grant delete on BoardgameCafe.review to webconnection@localhost;
grant delete on BoardgameCafe.stock to webconnection@localhost;