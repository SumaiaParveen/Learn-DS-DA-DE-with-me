### DECODE in PL/SQL

**Example 1:** Write a query to retrieve the following information for each order:

- The order ID
- The product name
- The quantity of the product ordered
- The price of the product
- The shipping class for the order (based on the total price of the order)

You have two tables.

Orders:

| order_id | product_id | quantity | price |
| -------- | ---------- | -------- | ----- |
| 1        | 1          | 1        | 100   |
| 2        | 2          | 2        | 400   |
| 3        | 3          | 1        | 300   |
| 4        | 1          | 3        | 300   |

Products:

| product_id | name       | price |
| ---------- | ---------- | ----- |
| 1          | Product 1  | 100   |
| 2          | Product 2  | 200   |
| 3          | Product 3  | 300   |

Query: 

`SELECT o.order_id, p.name, o.quantity, o.price,
  DECODE(o.price, 0..499, 'Standard', 500..999, 'Expedited', 'Overnight') as shipping_class
FROM orders o
JOIN products p
  ON o.product_id = p.product_id;`

Result: 

| order_id | name       | quantity | price | shipping_class |
| -------- | ---------- | -------- | ----- | -------------- |
| 1        | Product 1  | 1        | 100   | Standard       |
| 2        | Product 2  | 2        | 400   | Standard       |
| 3        | Product 3  | 1        | 300   | Standard       |
| 4        | Product 1  | 3        | 300   | Standard       |     
         
Explantion:

1. The FROM clause specifies the tables that the query will retrieve data from: orders and products.
2. The JOIN clause combines rows from the orders table with matching rows from the products table, based on the product_id column.
3. The SELECT clause specifies the columns that will be included in the query result set: o.order_id, p.name, o.quantity, o.price, and shipping_class.
4.The DECODE function is used to add the shipping_class column to the query result set. This function compares the price column in the orders table to a range of values (0 to 499, 500 to 999). If the value of price is within a particular range, the function returns a corresponding shipping class ('Standard', 'Expedited', or 'Overnight'). If the value of price is not within any of the specified ranges, the function returns NULL.
