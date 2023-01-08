### LAG() in PL/SQl or shift() in Pandas

In PL/SQL, the LAG function is an analytic function that returns the value of a specified expression from a row preceding the current row within a group of rows. The LAG function has the following syntax:

`LAG(expression, offset, default) OVER (
    [query_partition_clause]
    order_by_clause
)`

In pandas, the shift() function is used to shift the values in a DataFrame or Series by a specified number of periods along a particular axis. The shift() function has the following syntax:

`DataFrame.shift(periods=1, freq=None, axis=0, fill_value=None)

We can use the LAG() function in PL/SQL and the shift() function in pandas to achieve similar results, in the sense that both functions allow us to shift the values in a data set by a specified number of periods. 
