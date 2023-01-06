### CTE in PL/SQL

**Example 1**: we have two tables: employees, and department. We want to calculate the total salary for each department, along with the average salary for all employees.

| employee_id | name  | department_id | salary |
| ----------- | ----- | ------------- | ------ |
| 1           | Alice | 1             | 30000  |
| 2           | Bob   | 1             | 40000  |
| 3           | Charlie | 2           | 50000  |
| 4           | Diane | 2             | 60000  |
| 5           | Eve   | 3             | 70000  |


| department_id | department_name |
| ------------- | --------------- |
| 1             | Sales           |
| 2             | Marketing       |
| 3             | IT              |

We can achieve it by two steps:

1. Use a CTE to calculate the average salary for all employees.
2. Use a SELECT statement to join the employees and departments tables, and group the results by department name. Use the CTE to calculate the average salary, and use the SUM function to calculate the total salary for each department. 

The output would be this: 

| department_name  | total_salary | avg_salary |
| --------------- | ------------ | ---------- |
| Sales           | 70000        | 50000      |
| Marketing       | 110000       | 50000      |
| IT              | 70000        | 50000      |
