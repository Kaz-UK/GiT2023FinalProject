use boardgamecafe;

-- This is our username
create user webconnection@localhost identified by 'KHAFV';

grant select on boardgamecafe.* to webconnection@localhost;
grant insert on boardgamecafe.* to webconnection@localhost;
grant update on boardgamecafe.* to webconnection@localhost;

grant delete on boardgamecafe.customer to webconnection@localhost;

grant delete on boardgamecafe.booking to webconnection@localhost;
grant delete on boardgamecafe.review to webconnection@localhost;
grant delete on boardgamecafe.stock to webconnection@localhost;


