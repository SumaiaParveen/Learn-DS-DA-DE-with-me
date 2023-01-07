-- create and populate the orders and products tables:

CREATE TABLE orders (
  order_id NUMBER PRIMARY KEY,
  product_id NUMBER,
  quantity NUMBER,
  price NUMBER
);

CREATE TABLE products (
  product_id NUMBER PRIMARY KEY,
  name VARCHAR2(50),
  price NUMBER
);

INSERT INTO products (product_id, name, price)
VALUES (1, 'Product 1', 100);

INSERT INTO products (product_id, name, price)
VALUES (2, 'Product 2', 200);

INSERT INTO products (product_id, name, price)
VALUES (3, 'Product 3', 300);

INSERT INTO orders (order_id, product_id, quantity, price)
VALUES (1, 1, 1, 100);

INSERT INTO orders (order_id, product_id, quantity, price)
VALUES (2, 2, 2, 400);

INSERT INTO orders (order_id, product_id, quantity, price)
VALUES (3, 3, 1, 300);

INSERT INTO orders (order_id, product_id, quantity, price)
VALUES (4, 1, 3, 300);

--use a SELECT statement with a DECODE function to add a new column that indicates the shipping class for each order:

SELECT o.order_id, p.name, o.quantity, o.price,
  DECODE(o.price, 0..499, 'Standard', 500..999, 'Expedited', 'Overnight') as shipping_class
FROM orders o
JOIN products p
  ON o.product_id = p.product_id;
