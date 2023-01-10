### WoW (week over Week) Growth Rate

We want to create a PL/SQL script to calculate the week over week growth rate of an e-commerce company's sales. The script should calculate the total amount of orders placed during the current week and the total amount of orders placed during the previous week, and then calculate the growth rate as a percentage. The script should output the result to the console.

The orders table has the following structure:

orders

| order_id   | order_date | customer_id | amount |
|------------|------------|-------------|--------|
| NUMBER(10) | DATE       | NUMBER(10)  | NUMBER |


The order_id column is the primary key and is used to uniquely identify each order. The order_date column stores the date on which the order was placed. The customer_id column stores the ID of the customer who placed the order. The amount column stores the total amount of the order.

Our task is to write a PL/SQL script that meets the following requirements:

- Calculates the total amount of orders placed during the current week and the total amount of orders placed during the previous week.
- Calculates the growth rate as a percentage using the formula (current_week_total - prev_week_total) / prev_week_total.
Outputs the result to the console using the DBMS_OUTPUT.PUT_LINE function.

### Solution
- [PL/SQL](https://github.com/SumaiaParveen/Learn-DS-DA-DE-with-me/blob/main/%23Day8%20WoW%20Calculation%20in%20PL-SQL/WoW%20in%20PL-SQL.sql)
