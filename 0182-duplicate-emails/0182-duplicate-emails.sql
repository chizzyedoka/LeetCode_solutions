# Write your MySQL query statement below
SELECT DISTINCT(p1.email) from Person p1 
JOIN Person p2 
ON p1.id != p2.id AND p1.email=p2.email;


