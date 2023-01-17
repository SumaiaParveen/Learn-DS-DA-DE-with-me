-- Create the orders table with four columns: order_id, product, customer_id, and order_date
CREATE TABLE orders (
    order_id INT,
    product VARCHAR(255),
    customer_id INT,
    order_date DATE
);

-- Insert sample data into the orders table
INSERT INTO orders (order_id, product, customer_id, order_date) 
VALUES (1, 'Product A', 100, '2022-01-01'),
       (2, 'Product B', 101, '2022-01-02'),
       (3, 'Product C', 102, '2022-01-03'),
       (4, 'Product D', 103, '2022-01-04'),
       (1, 'Product A', 100, '2022-01-01');

-- Delete duplicate rows from the orders table
DELETE FROM orders
WHERE EXISTS (
    SELECT 1
    FROM orders
    WHERE order_id = orders.order_id
    AND product = orders.product
    AND customer_id = orders.customer_id
    HAVING COUNT(*) > 1
);

-- Select all columns and rows from the orders table
SELECT * FROM orders;
