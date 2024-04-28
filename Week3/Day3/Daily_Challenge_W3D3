-- Part 1
-- CREATE TABLE Customer(
-- id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE CustomerPofile(
-- id SERIAL PRIMARY KEY,
-- isLoggedIn BOOLEAN DEFAULT false,
-- customer_id INT UNIQUE,
-- FOREIGN KEY (customer_id) REFERENCES Customer(id)
-- );

-- INSERT INTO Customer (first_name, last_name)
-- VALUES ('John', 'Doe'), ('Jerome', 'Lalu'), ('Lea', 'Rive');

-- ALTER TABLE CustomerPofile RENAME TO CustomerProfile;

-- INSERT INTO CustomerProfile (isLoggedIn, customer_id)
-- VALUES (True, (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe')
-- 	   );
	   
-- INSERT INTO CustomerProfile (isLoggedIn, customer_id)
-- VALUES (FALSE, (SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

-- SELECT customer.first_name
-- from customer
-- JOIN customerprofile c ON customer.id = c.customer_id
-- WHERE isloggedin = True;

-- SELECT  customer.first_name,  c.isloggedin
-- from customer
-- LEFT JOIN customerprofile c ON customer.id = c.customer_id;

-- SELECT count(*)
-- FROM customer
-- JOIN customerprofile c ON customer.id = c.customer_id
-- WHERE isloggedin != True

-- Part 2
-- CREATE TABLE Book (
--     book_id SERIAL PRIMARY KEY,
--     title VARCHAR(255) NOT NULL,
--     author VARCHAR(255) NOT NULL
-- );

-- INSERT INTO Book (title, author)
-- VALUES ('Alice In Wonderland', 'Lewis Carroll'),
--        ('Harry Potter', 'J.K Rowling'),
--        ('To Kill a Mockingbird', 'Harper Lee');
	   
-- CREATE TABLE Student (
--     student_id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL UNIQUE,
--     age INTEGER CHECK (age <= 15)
-- );

-- INSERT INTO Student (name, age)
-- VALUES ('John', 12), ('Lera', 11), ('Patrick', 10), ('Bob', 14);

-- CREATE TABLE Library (
-- 	book_fk_id INTEGER,
-- 	student_fk_id INTEGER,
-- 	borrowed_date DATE,
-- 	PRIMARY KEY (book_fk_id, student_fk_id),
-- 	FOREIGN KEY (book_fk_id) REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	FOREIGN KEY (student_fk_id) REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
-- );

-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES (
--     (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--     (SELECT student_id FROM Student WHERE name = 'John'),
--     '2022-02-15'
-- ),
-- (
--     (SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'),
--     (SELECT student_id FROM Student WHERE name = 'Bob'),
--     '2021-03-03'
-- ),
-- (
--     (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--     (SELECT student_id FROM Student WHERE name = 'Lera'),
--     '2021-05-23'
-- ),
-- (
--     (SELECT book_id FROM Book WHERE title = 'Harry Potter'),
--     (SELECT student_id FROM Student WHERE name = 'Bob'),
--     '2021-08-12'
-- );

-- SELECT *
-- FROM library;

-- SELECT s.name, b.title
-- from library
-- join book b on b.book_id = library.book_fk_id
-- join public.student s on s.student_id = library.student_fk_id;

-- SELECT avg(s.age)
-- FROM library
-- join book b on b.book_id = library.book_fk_id
-- join public.student s on s.student_id = library.student_fk_id
-- WHERE b.title = 'Alice In Wonderland';

-- DELETE FROM student
-- WHERE student_id = 3; -- rows with student_id (3) deleted
