# Write your MySQL query statement below
SELECT name as customers
FROM Customers 
LEFT JOIN orders
ON Customers.id = orders.CustomerId
WHERE customerId IS NULL

