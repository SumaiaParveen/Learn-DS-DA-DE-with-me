-- Create the orders table with sample data
CREATE TABLE orders (order_date DATE, order_id INT);
INSERT INTO orders (order_date, order_id)
VALUES ('2022-05-01', 1001), ('2022-05-03', 1002), ('2022-05-04', 1003),
       ('2022-05-05', 1004), ('2022-05-06', 1005), ('2022-05-07', 1006);

-- Create the calendar table
CREATE TABLE calendar (date DATE PRIMARY KEY);

-- Populate the calendar table with dates
DECLARE @start_date DATE = '2022-05-01';
DECLARE @end_date DATE = '2022-05-07';

WHILE (@start_date <= @end_date)
BEGIN
    INSERT INTO calendar (date) VALUES (@start_date);
    SET @start_date = DATEADD(day, 1, @start_date);
END;

-- Find missing dates
SELECT calendar.date
FROM calendar
LEFT JOIN orders
ON calendar.date = orders.order_date
WHERE orders.order_date IS NULL;
