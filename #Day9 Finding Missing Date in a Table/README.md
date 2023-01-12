### How to Find a Missing Dates in a Table (T-SQL)

We need to write a SQL query that will find the missing date from a table, orders.
To solve this problem, we can use a combination of a calendar table and a LEFT JOIN. The calendar table will have all the dates between a certain range. When we left join the "orders" table with the calendar table on the "order_date" column, it will return all the dates from the calendar table that do not have a corresponding date in the "orders" table. This way we can find all the missing date in the table orders.

|order_date	|order_id|
|-----------|--------|
|2022-05-01	|1001    |
|2022-05-03	|1002    |
|2022-05-04	|1003    |
|2022-05-05	|1004    |
|2022-05-06	|1005    |
|2022-05-07	|1006    |

Solution 

- [T-SQL (MS SQL Server)](https://github.com/SumaiaParveen/Learn-DS-DA-DE-with-me/blob/main/%23Day9%20Finding%20Missing%20Date%20in%20a%20Table/Finding%20Missing%20Date%20T-SQL.sql)
