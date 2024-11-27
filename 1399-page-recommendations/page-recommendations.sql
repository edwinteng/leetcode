# Write your MySQL query statement below
WITH friend_like as(
SELECT page_id
FROM Friendship f
JOIN Likes l
on f.user2_id=l.user_id or f.user1_id = l.user_id
WHERE f.user1_id=1 or f.user2_id=1
),
my_like as(
SELECT page_id
FROM Likes
WHERE user_id=1
)
SELECT distinct page_id as recommended_page
FROM friend_like
WHERE page_id 
not in (SELECT page_id FROM my_like)