-- EX_4: Scalar Functions with the Sakila Database
-- Week 3, Section 3.B (3.B.1 - 3.B.6)
-- Run one query at a time in MySQL Workbench and inspect the Results Grid.
-- The answers in comments below correspond to the standard Sakila sample database.

USE sakila;

-- =============================================================
-- WARM-UP: Scalar versus aggregate
-- =============================================================
SELECT AVG(rental_rate) AS average_rental_rate FROM film;

SELECT title, rental_rate, ROUND(rental_rate) AS rounded_rate
FROM film;

-- Checkpoints: AVG = 1 result row; ROUND = 1,000 result rows.
-- ROUND is scalar because it calculates one rounded value for each film row.

-- =============================================================
-- PART A: Conversion functions (3.B.2)
-- =============================================================
-- A1: Split a rental timestamp into date and time.
SELECT rental_id,
       rental_date,
       CAST(rental_date AS DATE) AS rental_day,
       CAST(rental_date AS TIME) AS rental_time
FROM rental
LIMIT 10;

-- A2: Convert numbers to text, decimals, and integers.
SELECT title,
       CONVERT(rental_rate, CHAR) AS rate_as_text,
       CAST(rental_duration AS DECIMAL(5,2)) AS duration_decimal,
       CAST(rental_rate AS SIGNED) AS rate_as_integer
FROM film
LIMIT 10;

-- A3: Convert base-10 film IDs to binary (base 2) and hex (base 16).
SELECT film_id,
       CONV(film_id, 10, 2) AS binary_id,
       CONV(film_id, 10, 16) AS hex_id
FROM film
WHERE film_id IN (10, 255);

-- Checkpoints: Rental 1's rental_day is 2005-05-24.
-- CAST(4.99 AS SIGNED) returns 5; MySQL rounds to a whole number.
-- Film 255 is 11111111 in binary and FF in hexadecimal.

-- =============================================================
-- PART B: String functions (3.B.3)
-- =============================================================
-- B1: Combine names and standardize emails.
SELECT customer_id,
       CONCAT_WS(' ', first_name, last_name) AS full_name,
       CONCAT_WS(', ', last_name, first_name) AS directory_name,
       LOWER(email) AS clean_email
FROM customer
LIMIT 10;

-- B2: Split, change case, replace spaces, and reverse film titles.
SELECT title,
       SUBSTRING(title, 1, 3) AS first_three,
       LOWER(title) AS lower_title,
       REPLACE(title, ' ', '_') AS file_name,
       REVERSE(title) AS backwards
FROM film
LIMIT 10;

-- B3: Additional string functions on sample text.
SELECT TRIM(' Sakila ') AS trimmed,
       INSERT('ACADEMY DINOSAUR', 1, 7, 'MUSEUM') AS inserted,
       STRCMP('ALIEN', 'ZORRO') AS compare_1,
       STRCMP('ACE', 'ACE') AS compare_2,
       FORMAT(1234567.891, 2) AS formatted;

-- B4: Create proper-case first names.
SELECT first_name,
       CONCAT(UPPER(SUBSTRING(first_name, 1, 1)),
              LOWER(SUBSTRING(first_name, 2))) AS proper_first
FROM customer
LIMIT 10;

-- Checkpoints: Customer 1 is SMITH, MARY in directory_name.
-- STRCMP returns 0 on a match and -1 if the first string comes earlier.
-- FORMAT(1234567.891, 2) displays 1,234,567.89.
-- Proper case uppercases the first letter and lowercases the rest.

-- =============================================================
-- PART C: Date functions (3.B.4)
-- =============================================================
-- C1: Extract date, weekday, day of year, and quarter.
SELECT rental_id,
       rental_date,
       DATE(rental_date) AS rental_day,
       DAYNAME(rental_date) AS weekday,
       DAYOFWEEK(rental_date) AS weekday_number,
       DAYOFYEAR(rental_date) AS day_of_year,
       QUARTER(rental_date) AS quarter
FROM rental
LIMIT 10;

-- C2: Determine days kept and the due date by joining three tables.
SELECT r.rental_id,
       r.rental_date,
       r.return_date,
       DATEDIFF(r.return_date, r.rental_date) AS days_kept,
       f.rental_duration,
       DATE_ADD(r.rental_date, INTERVAL f.rental_duration DAY) AS due_date
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
LIMIT 10;

-- C3: Create report-friendly dates and look one month earlier.
SELECT payment_id,
       payment_date,
       DATE_FORMAT(payment_date, '%M %d, %Y') AS report_date,
       DATE_FORMAT(payment_date, '%m/%d/%Y %h:%i %p') AS us_format,
       DATE_SUB(payment_date, INTERVAL 1 MONTH) AS one_month_earlier
FROM payment
LIMIT 10;

-- Current date/time; results depend on when you run the query.
SELECT CURDATE(), CURTIME(), CURRENT_TIMESTAMP;

-- Checkpoints: Rental 1 happened on Tuesday, was kept 2 days,
-- and was due 2005-05-31 22:53:30; payment 1 is May 25, 2005.
-- Comparing old Sakila rentals with today's date makes them appear years overdue.

-- =============================================================
-- PART D: NULL-related functions (3.B.5)
-- =============================================================
-- D1: Replace missing return dates with a label.
SELECT rental_id,
       rental_date,
       IFNULL(return_date, 'Not returned') AS return_status
FROM rental
WHERE return_date IS NULL;

-- D2: Count unreturned rentals.
SELECT COUNT(*) AS total_rentals,
       SUM(ISNULL(return_date)) AS not_returned
FROM rental;

-- D3: Pick the first available language ID.
SELECT title,
       original_language_id,
       language_id,
       COALESCE(original_language_id, language_id) AS display_language
FROM film
LIMIT 10;

-- D4: Treat the $0.99 rental rate as NULL so COUNT skips those films.
SELECT COUNT(*) AS all_films,
       COUNT(NULLIF(rental_rate, 0.99)) AS films_not_099
FROM film;

-- Additional checkpoint: payments missing a rental link.
SELECT payment_id, IFNULL(rental_id, 'No rental linked') AS rental_reference
FROM payment
WHERE rental_id IS NULL;

-- Checkpoints: 183 rentals have no return date; 659 films are not $0.99.
-- Unlinked payments: 424, 7011, 10840, 14675, and 15458.

-- =============================================================
-- PART E: Numeric functions (3.B.6)
-- =============================================================
-- E1: Compare rounding methods for break-even rental counts.
SELECT title,
       replacement_cost,
       rental_rate,
       replacement_cost / rental_rate AS raw_ratio,
       ROUND(replacement_cost / rental_rate, 2) AS rounded,
       CEILING(replacement_cost / rental_rate) AS rentals_to_break_even,
       FLOOR(replacement_cost / rental_rate) AS floored,
       TRUNCATE(replacement_cost / rental_rate, 1) AS truncated
FROM film
LIMIT 10;

-- E2: Compare each film's rate with the average rate.
SELECT title,
       rental_rate,
       ROUND(rental_rate - (SELECT AVG(rental_rate) FROM film), 2) AS diff_from_avg,
       ABS(ROUND(rental_rate - (SELECT AVG(rental_rate) FROM film), 2)) AS distance_from_avg
FROM film
LIMIT 10;

-- E3: Even and odd film IDs.
SELECT MOD(film_id, 2) AS even_or_odd, COUNT(*) AS films
FROM film
GROUP BY MOD(film_id, 2);

-- Ensure a minimum displayed price of 2.99.
SELECT title, rental_rate,
       GREATEST(rental_rate, 2.99) AS price_with_2_99_minimum
FROM film
LIMIT 10;

-- Additional numeric functions.
SELECT LEAST(4.99, 2.99, 0.99), POW(2, 10), SQRT(144), ROUND(PI(), 4);

-- Random film selection: run this query twice and compare.
SELECT title FROM film ORDER BY RAND() LIMIT 5;

-- Checkpoints: ACADEMY DINOSAUR: ROUND 21.20, CEILING 22,
-- FLOOR 21, TRUNCATE 21.2; diff_from_avg -1.99, distance_from_avg 1.99.
-- CEILING is appropriate because customers cannot rent a fraction of a time.
-- RAND typically produces a different set of five films each run.

-- =============================================================
-- GUIDED PRACTICE: G1-G5
-- =============================================================
-- G1: Mailing name tags in last-name order.
SELECT CONCAT_WS(', ', last_name, first_name) AS directory_name,
       LOWER(email) AS clean_email
FROM customer
ORDER BY last_name, first_name;
-- G1 answer: The first row is ABNEY, RAFAEL.

-- G2: Count rentals per named month.
SELECT DATE_FORMAT(rental_date, '%M') AS rental_month, COUNT(*) AS rentals
FROM rental
GROUP BY rental_month
ORDER BY rentals DESC;
-- G2 answer: July has the most rentals (6,709).

-- G3: Due date and actual return date for rental 1.
SELECT r.rental_id, r.rental_date,
       DATE_ADD(r.rental_date, INTERVAL f.rental_duration DAY) AS due_date,
       r.return_date
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
WHERE r.rental_id = 1;
-- G3 answer: Rental 1 was returned on time (May 26, before May 31).

-- G4: Show the status of every rental.
SELECT rental_id, IFNULL(return_date, 'Not returned') AS return_status
FROM rental;
-- G4 answer: 183 rentals say 'Not returned'.

-- G5: Find break-even rentals for each film.
SELECT title, CEILING(replacement_cost / rental_rate) AS rentals_to_break_even
FROM film;
-- G5 answer: ACADEMY DINOSAUR needs 22 rentals.

-- =============================================================
-- INDEPENDENT PRACTICE: P1-P9
-- Each task includes a one-line plain-English answer in a comment.
-- =============================================================
-- P1: Proper-case full names with lowercase emails, sorted by surname.
SELECT CONCAT_WS(' ',
       CONCAT(UPPER(SUBSTRING(first_name, 1, 1)), LOWER(SUBSTRING(first_name, 2))),
       CONCAT(UPPER(SUBSTRING(last_name, 1, 1)), LOWER(SUBSTRING(last_name, 2)))) AS full_name,
       LOWER(email) AS clean_email
FROM customer
ORDER BY last_name, first_name;
-- P1 answer: Rafael Abney is the first customer in the sorted mailing list.

-- P2: Count rentals returned later than the allowed rental duration.
SELECT COUNT(*) AS late_returns
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
WHERE DATEDIFF(r.return_date, r.rental_date) > f.rental_duration;
-- P2 answer: 7,269 rentals were returned late.

-- P3: Find the busiest weekday.
SELECT DAYNAME(rental_date) AS weekday, COUNT(*) AS rentals
FROM rental
GROUP BY weekday
ORDER BY rentals DESC;
-- P3 answer: Tuesday was the busiest day with 2,463 rentals.

-- P4: Summarize payment revenue by year and quarter.
SELECT YEAR(payment_date) AS yr, QUARTER(payment_date) AS qtr,
       FORMAT(SUM(amount), 2) AS revenue
FROM payment
GROUP BY YEAR(payment_date), QUARTER(payment_date)
ORDER BY yr, qtr;
-- P4 answer: The highest quarterly revenue was $52,446.02 in Q3 2005.

-- P5: Average number of rentals needed for a film to break even.
SELECT ROUND(AVG(CEILING(replacement_cost / rental_rate)), 2) AS avg_break_even
FROM film;

-- P5: List the films requiring more than that average.
SELECT title, CEILING(replacement_cost / rental_rate) AS rentals_to_break_even
FROM film
WHERE CEILING(replacement_cost / rental_rate) >
      (SELECT AVG(CEILING(replacement_cost / rental_rate)) FROM film)
ORDER BY rentals_to_break_even DESC, title;
-- P5 answer: Average break-even is 11.17 rentals; 326 films exceed it.
-- ARABIA DOGMA, BALLROOM MOCKINGBIRD, and BONNIE HOLOCAUST top the list at 31.

-- P6: Days outstanding as of the fixed Sakila reference date.
SELECT rental_id, rental_date,
       DATEDIFF('2006-02-14', rental_date) AS days_out
FROM rental
WHERE return_date IS NULL
ORDER BY days_out DESC;
-- P6 answer: 183 rentals were unreturned; the longest was out 177 days.

-- P7: Format a product code like ACA-0.99-1 for each film.
SELECT film_id,
       CONCAT_WS('-', UPPER(SUBSTRING(title, 1, 3)), rental_rate, film_id) AS product_code
FROM film;
-- P7 answer: The product code for film_id 2 is ACE-4.99-2.

-- P8: Count customers with a payment > $10 in Q3 of 2005.
SELECT COUNT(*) AS q3_big_spenders
FROM customer
WHERE customer_id IN (
    SELECT customer_id
    FROM payment
    WHERE YEAR(payment_date) = 2005
      AND QUARTER(payment_date) = 3
      AND amount > 10
);
-- P8 answer: 90 customers made a payment over $10 in Q3 of 2005.

-- P9: Average number of calendar days a returned rental was kept.
SELECT ROUND(AVG(DATEDIFF(return_date, rental_date)), 2) AS avg_days_kept
FROM rental;

-- P9: Count rentals kept longer than that average.
SELECT COUNT(*) AS kept_longer_than_avg
FROM rental
WHERE DATEDIFF(return_date, rental_date) >
      (SELECT AVG(DATEDIFF(return_date, rental_date)) FROM rental);
-- P9 answer: Average days kept is 5.03; 7,161 rentals exceeded it.
