# Write your MySQL query statement below
select score,
(dense_rank() over (order by score desc)) as "rank"
from Scores

#pls upvote if you find solution easy to undestand....!! Thanks..!!!