-- select first_name, last_name from customer as full_name;
-- select DISTINCT create_date from customer;
-- select * from customer order by first_name DESC;
-- select film_id, title, description, release_year, rental_rate from film order by rental_rate ASC;
-- select address, phone from address where district = 'Texas';
-- select * from film where film_id in (15, 150);
-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE title = 'Titanic';
-- select * from film;
-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE title = 'Chamber Italian';
-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE (left (title, 2) ilike 'ch%');
-- #10
-- select * from film order by rental_rate asc limit 10;
-- #11
-- select * from film order by rental_rate asc fetch first 10 rows only offset 10;
-- #12
-- select customer.first_name, customer.last_name, payment.amount, payment.payment_date from customer inner join payment on customer.customer_id = payment.customer_id Order by payment.customer_id;
--#13
-- select * from film left join inventory on film.film_id = inventory.film_id where inventory_id is null;
--#14
-- select city, country from city inner join country on city.country_id = country.country_id;
--#15
-- select customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date, payment.staff_id from payment inner join customer on customer.customer_id = payment.customer_id order by payment.staff_id asc
