-- 1. Create the employees and departments tables:

CREATE TABLE employees (
  employee_id NUMBER PRIMARY KEY,
  name VARCHAR2(50),
  department_id NUMBER,
  salary NUMBER
);

CREATE TABLE departments (
  department_id NUMBER PRIMARY KEY,
  department_name VARCHAR2(50)
);

-- 2. Insert some rows into the employees and departments tables:

INSERT INTO departments (department_id, department_name)
VALUES (1, 'Sales');

INSERT INTO departments (department_id, department_name)
VALUES (2, 'Marketing');

INSERT INTO departments (department_id, department_name)
VALUES (3, 'IT');

INSERT INTO employees (employee_id, name, department_id, salary)
VALUES (1, 'Alice', 1, 30000);

INSERT INTO employees (employee_id, name, department_id, salary)
VALUES (2, 'Bob', 1, 40000);

INSERT INTO employees (employee_id, name, department_id, salary)
VALUES (3, 'Charlie', 2, 50000);

INSERT INTO employees (employee_id, name, department_id, salary)
VALUES (4, 'Diane', 2, 60000);

INSERT INTO employees (employee_id, name, department_id, salary)
VALUES (5, 'Eve', 3, 70000);

-- 3. Use a CTE to calculate the average salary for all employees:

WITH avg_salary AS (
  SELECT AVG(salary) avg_salary
  FROM employees
)

-- 4. Use a SELECT statement to join the employees and departments tables, and group the results by department name. Use the CTE to calculate the average salary, and use the SUM function to calculate the total salary for each department:

SELECT d.department_name, SUM(e.salary) total_salary, a.avg_salary
FROM employees e
JOIN departments d
  ON e.department_id = d.department_id
JOIN avg_salary a
GROUP BY d.department_name, a.avg_salary;
