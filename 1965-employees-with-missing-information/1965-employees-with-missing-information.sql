# Write your MySQL query statement below

SELECT e.employee_id  FROM Employees e
LEFT JOIN Salaries s
ON e.employee_id = s.employee_id
WHERE s.salary IS NULL

UNION

SELECT s.employee_id
FROM Salaries s
LEFT JOIN Employees e
ON e.employee_id = s.employee_id
WHERE e.name is NULL

ORDER BY employee_id

/*Select e.employee_id from Employees e 
LEFT JOIN Salaries s 
ON e.employee_id = s.employee_id
WHERE s.salary  is NULL

UNION

Select s.employee_id from Salaries s
LEFT JOIN Employees e 
ON e.employee_id = s.employee_id
WHERE e.name is NULL

ORDER BY employee_id;*/














/*SELECT employee_id
FROM Employees e
FULL JOIN Salaries s ON e.employee_id = s.employee_id
WHERE e.employee_id IS NULL OR s.employee_id IS NULL*/









