--- create a table called sales with three columns: store_id, sale_date, and total_sales:

CREATE TABLE sales (
  store_id INTEGER,
  sale_date DATE,
  total_sales INTEGER
);

INSERT INTO sales (store_id, sale_date, total_sales)
VALUES (1, '2022-01-01', 100),
       (1, '2022-01-02', 120),
       (1, '2022-01-03', 130),
       (2, '2022-01-01', 90),
       (2, '2022-01-03', 110);

--- use the LAG() function to shift the values in the total_sales column by one row, and it adds a new column called prev_sales to the table containing the shifted values. The LAG() function is applied within each store_id group (defined by the PARTITION BY clause) and is ordered by the sale_date column (defined by the ORDER BY clause). The default value of 0 is used for the first row within each group.

SELECT store_id, sale_date, total_sales,
       LAG(total_sales, 1, 0) OVER (PARTITION BY store_id ORDER BY sale_date) AS prev_sales
FROM sales;

--- The resulting table contains the store_id, sale_date, and total_sales values from the original table, along with a new prev_sales column containing the total_sales value from the preceding row within each store_id group (ordered by sale_date). If the current row is the first row within its group, the prev_sales column would contain the default value (0 in this case).
