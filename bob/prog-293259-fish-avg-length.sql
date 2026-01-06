-- https://school.programmers.co.kr/learn/courses/30/lessons/293259
-- AVG, NULL

select round(AVG(SAFE_LENGTH), 2) as AVERAGE_LENGTH
from (
    select
        if(LENGTH is null, 10, LENGTH) as SAFE_LENGTH
    from FISH_INFO
) as t;
