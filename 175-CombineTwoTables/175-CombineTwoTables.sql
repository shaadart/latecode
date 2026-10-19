-- Last updated: 19/10/2026, 16:30:20
# Write your MySQL query statement below




select Person.firstName, Person.lastName, Address.city, Address.state
From Person
Left Join Address
on Person.personId = Address.personId