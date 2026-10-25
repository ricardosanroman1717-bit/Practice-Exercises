-- Setup: Exercise 3B
DROP DATABASE IF EXISTS beanbrew_dev;
CREATE DATABASE beanbrew_dev;
USE beanbrew_dev;
SELECT DATABASE();
-- Task 1.1: Create category
CREATE TABLE category
(
    category_id TINYINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(30) NOT NULL
);

DESCRIBE category;

-- Task 1.2: Create the product table
CREATE TABLE product
(
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(60) NOT NULL,
    category_id TINYINT UNSIGNED NOT NULL,
    unit_price DECIMAL(6,2) NOT NULL,
    stock_qty INT UNSIGNED,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT fk_product_category FOREIGN KEY (category_id)
        REFERENCES category(category_id)
        ON DELETE RESTRICT ON UPDATE CASCADE

);

DESCRIBE product;
-- Task 1.3: Predict, then run
-- Prediction: The orders table will fail because customer does not exist yet.

CREATE TABLE orders
(
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    order_date DATE NOT NULL,
    quantity SMALLINT UNSIGNED NOT NULL DEFAULT 1,
    CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id)
        REFERENCES customer(customer_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_orders_product FOREIGN KEY (product_id)
        REFERENCES product(product_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);
-- Task 1.4: Create the customer table
CREATE TABLE customer
(
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(100),
    city VARCHAR(40),
    loyalty_points INT UNSIGNED NOT NULL DEFAULT 0,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DESCRIBE customer;
-- Task 1.6: Create the employee table
CREATE TABLE employee
(
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    job_title VARCHAR(40) NOT NULL,
    hire_date DATE NOT NULL,
    reports_to INT,
    CONSTRAINT fk_employee_manager FOREIGN KEY (reports_to)
        REFERENCES employee(employee_id)
        ON DELETE SET NULL
);
-- Task 1.6: Set employee IDs to start at 100
ALTER TABLE employee AUTO_INCREMENT = 100;
-- Task 1.6: Verify all five tables
SHOW TABLES;
-- Task 1.7: Load the starter data

-- Add four categories
INSERT INTO category (category_name) VALUES
('Coffee'), ('Tea'), ('Bakery'), ('Merchandise');

-- Add twelve products
INSERT INTO product (product_name, category_id, unit_price, stock_qty) VALUES
('House Blend Drip', 1, 2.75, 120),
('Espresso Single', 1, 3.25, 80),
('Caramel Latte', 1, 4.95, 60),
('Cold Brew', 1, 4.50, 45),
('Earl Grey', 2, 2.95, 50),
('Chai Latte', 2, 4.75, 40),
('Blueberry Muffin', 3, 3.50, 24),
('Butter Croissant', 3, 3.25, 30),
('Cinnamon Roll', 3, 3.95, 18),
('Logo Travel Mug', 4, 14.99, 25),
('Pumpkin Spice Latte', 1, 5.45, 35),
('Ceramic Pour-Over Set', 4, 29.99, NULL);

-- Add six customers
INSERT INTO customer (first_name, last_name, email, city, loyalty_points) VALUES
('Maria', 'Lopez', 'maria.lopez@example.com', 'Boston', 340),
('James', 'Carter', 'james.carter@example.com', 'Cambridge', 120),
('Aisha', 'Khan', 'aisha.khan@example.com', 'Boston', 560),
('Tom', 'Nguyen', NULL, 'Somerville', 75),
('Priya', 'Shah', 'priya.shah@example.com', 'Boston', 0),
('Daniel', 'Brooks', 'daniel.brooks@example.com', 'Quincy', 210);

-- Add nine orders
INSERT INTO orders (customer_id, product_id, order_date, quantity) VALUES
(1, 3, '2026-09-01', 1),
(2, 1, '2026-09-02', 2),
(3, 7, '2026-09-03', 1),
(1, 5, '2026-09-03', 1),
(3, 11, '2026-09-04', 2),
(4, 2, '2026-09-05', 1),
(6, 10, '2026-09-06', 1),
(1, 11, '2026-09-08', 1),
(2, 8, '2026-09-09', 3);

-- Add the operations manager
INSERT INTO employee (first_name, last_name, job_title, hire_date, reports_to) VALUES
('Dana', 'Reyes', 'Operations Manager', '2021-03-15', NULL);

-- Check Dana's generated employee ID
SELECT LAST_INSERT_ID();

-- Add the remaining employees
INSERT INTO employee (first_name, last_name, job_title, hire_date, reports_to) VALUES
('Marcus', 'Hill', 'Shift Lead', '2023-06-01', 100),
('Sofia', 'Alvarez', 'Barista', '2024-09-10', 101),
('Ken', 'Ito', 'Barista', '2025-01-20', 101);

-- Verify the row counts
SELECT 'category' AS table_name, COUNT(*) AS row_count FROM category
UNION ALL SELECT 'product', COUNT(*) FROM product
UNION ALL SELECT 'customer', COUNT(*) FROM customer
UNION ALL SELECT 'orders', COUNT(*) FROM orders
UNION ALL SELECT 'employee', COUNT(*) FROM employee;

-- Verify the employee records
SELECT employee_id, first_name, job_title, reports_to
FROM employee;
INSERT INTO category (category_name) 
VALUES ('Coffee');
-- Task 1.7: Check current row counts
SELECT 'category' AS table_name, COUNT(*) AS row_count FROM category
UNION ALL SELECT 'product', COUNT(*) FROM product
UNION ALL SELECT 'customer', COUNT(*) FROM customer
UNION ALL SELECT 'orders', COUNT(*) FROM orders
UNION ALL SELECT 'employee', COUNT(*) FROM employee;
-- Task 1.7: Verify existing category
SELECT * FROM category;
-- Task 1.7: Insert the three remaining categories
INSERT INTO category (category_name) VALUES
('Tea'),
('Bakery'),
('Merchandise');
-- Task 1.7: Verify all categories
SELECT * FROM category;
-- Task 1.7: Verify product records
SELECT product_id, product_name, category_id, unit_price
FROM product
ORDER BY product_id;