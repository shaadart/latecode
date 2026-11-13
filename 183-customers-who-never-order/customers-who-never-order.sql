# Write your MySQL query statement below
Select c.name as Customers
from Customers c
left join Orders o on o.customerid = c.id 
where o.id is Null