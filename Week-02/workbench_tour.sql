
/*
Ex1C - Workbench Readiness Check
Name: Ricardo Sanroman
Date: 2026-10-20

Q1: My local connection uses localhost on port 3306
and logs in as root.
Q2: I would click the plus (+) icon to create
a new database connection.
Q3: 1 is Navigator, 2 is Information,
3 is Query Editor, 4 is Output, and
5 is SQL Additions. We will not use
SQL Additions in this course.
Q4: My login user is root@localhost,
my port is 3306, and my MySQL
Server version is 26.7.0.
Q5: Two administration tools are
Server Status and Client Connections.
Q6: actor_id uses SMALLINT UNSIGNED.
AI stands for Auto-Increment, which automatically
generates ID numbers. PK stands for Primary Key,
which uniquely identifies each record.
Q7: The film_actor table contains actor_id,
film_id, and last_update. It has two
foreign keys. actor_id references the
actor table, and film_id references
the film table.
Q8: Clicking the grid icon opened a new
query tab and displayed records from
the film_actor table. The Output panel
showed the query execution results.
Q9: The actor query returned 200 records.
I found the number in the results/output
area at the bottom of MySQL Workbench.
Q10: USE sakila;, SELECT * FROM actor;, and SELECT * FROM sakila.film; succeeded. SELECT * FROM actr; failed with Error 1146 because the table sakila.actr does not exist.
Q11: Vertical output displays each record separately with its column names and values instead of displaying records in a table. It's helpful for reading records with many columns.
Q12: AKROYD.
Q13: Three actors.
Q14: VARCHAR(45), meaning the column stores text up to 45 characters long.
*/

USE sakila;
SELECT * FROM actor;
SELECT * FROM sakila.film;
SELECT * FROM actor;
