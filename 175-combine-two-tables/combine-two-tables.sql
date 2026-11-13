# WriteP.first your MySQL query statement below
SELECT P.firstName, P.lastName, A.city, A.state
From Person P LEFT JOIN Address A
on P.personId = A.personId