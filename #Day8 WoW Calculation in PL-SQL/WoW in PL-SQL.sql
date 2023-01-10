--- create order table

CREATE TABLE orders (
  order_id NUMBER(10) PRIMARY KEY,
  order_date DATE NOT NULL,
  customer_id NUMBER(10) NOT NULL,
  amount NUMBER(10,2) NOT NULL
);

-- Insert some sample data into the table
INSERT INTO orders (order_id, order_date, customer_id, amount)
VALUES (1, '2022-01-01', 1001, 100.00);

INSERT INTO orders (order_id, order_date, customer_id, amount)
VALUES (2, '2022-01-03', 1002, 50.00);

INSERT INTO orders (order_id, order_date, customer_id, amount)
VALUES (3, '2022-01-05', 1003, 200.00);

INSERT INTO orders (order_id, order_date, customer_id, amount)
VALUES (4, '2022-01-07', 1004, 75.00);

INSERT INTO orders (order_id, order_date, customer_id, amount)
VALUES (5, '2022-01-09', 1005, 125.00);

-- Calculate the week over week growth/decline rate
DECLARE
  l_current_week_total NUMBER(10,2);
  l_prev_week_total NUMBER(10,2);
  l_growth_rate NUMBER(10,2);
BEGIN
  -- Calculate the total amount of orders for the current week
  SELECT SUM(amount) INTO l_current_week_total
  FROM orders
  WHERE order_date BETWEEN TRUNC(SYSDATE, 'IW') AND TRUNC(SYSDATE);

  -- Calculate the total amount of orders for the previous week
  SELECT SUM(amount) INTO l_prev_week_total
  FROM orders
  WHERE order_date BETWEEN TRUNC(SYSDATE - 7, 'IW') AND TRUNC(SYSDATE - 7);

  -- Calculate the growth rate
  l_growth_rate := (l_current_week_total - l_prev_week_total) / l_prev_week_total;

  -- Output the result
  DBMS_OUTPUT.PUT_LINE('Week over week growth rate: ' || TO_CHAR(l_growth_rate, 'FM999990.00') || '%');
END;
/

--- This PL/SQL block first creates the orders table and inserts some sample data into it. Then, it declares two variables to hold the total amount of orders for the current and previous weeks, and a third variable to hold the growth rate. It calculates the total amount of orders for the current and previous weeks using the SUM function and a BETWEEN clause to filter the data by the order dates. Finally, it calculates the growth rate using the formula (current_week_total - prev_week_total) / prev_week_total, and outputs the result using the DBMS_OUTPUT.PUT_LINE function.

--- If you run the PL/SQL script on a date that falls within the current week (for example, 2022-01-09), the script will calculate the total amount of orders for the current week (orders 4 and 5, for a total of $200.00) and the total amount of orders for the previous week (orders 1, 2, and 3, for a total of $325.00). The growth rate will then be calculated as (200 - 325) / 325 = -38.46%.
