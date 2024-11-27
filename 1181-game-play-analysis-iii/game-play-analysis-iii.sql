# Write your MySQL query statement below

SELECT player_id,event_date,
SUM(games_played) over (
    partition by player_id
    order by event_date asc
    range between unbounded preceding and current row
) as games_played_so_far
FROM Activity
