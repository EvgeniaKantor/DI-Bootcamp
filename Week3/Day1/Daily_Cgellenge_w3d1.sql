-- create table actors(
-- actor_id serial primary key,
-- first_name varchar (50) not null,
-- last_name varchar (100) not null,
-- age date not null,
-- number_oscars smallint not null
-- )

-- select * from actors;

-- insert into actors (first_name, last_name, age, number_oscars)
-- values ('Matt','Damon','08/10/1970', 5),
-- ('George','Clooney','06/05/1961', 2)

-- -- insert into actors (first_name, Last_name, age, number_oscars)
-- values ('Emma', 'Watson', '15/04/1990', 1)

-- -- insert into actors (first_name, Last_name, age, number_oscars)
-- values ('Jennifer', 'Aniston', '11/02/1969', 2)
-- update actors set age = '1978-01-01' where first_name = 'Matt' 
-- returning *
-- delete from actors where actor_id = 3
-- returning *
-- select * from actors
-- update actors set first_name = 'Maty' where last_name = 'Damon'
-- returning *
-- update actors set number_oscars = 4 where last_name = 'Clooney'
-- returning *
-- alter table actors rename column "age" to "birthdate";

-- delete from actors where actor_id = 2
-- returning *
-- select * from actors where number_oscars >= 5
-- select * from actors where first_name ilike '%e%'
-- select count(*) as last_name from actors
-- insert into actors (first_name, last_name, birthdate, number_oscars)
-- values ('Mister', 'Kxe', '1980-10-10', 3)
-- insert into actors (first_name, last_name, birthdate, number_oscars)
-- values ('Mister', '', '1980-10-10', 3)
-- select * from actors
