-- https://school.programmers.co.kr/learn/courses/30/lessons/293261
-- max

select
    ID, FISH_NAME, LENGTH
from FISH_INFO as f
join FISH_NAME_INFO as n
    on f.FISH_TYPE = n.FISH_TYPE
where (f.LENGTH, f.FISH_TYPE) in ( -- 둘 다 한 번에 비교해야함
    select
        max(LENGTH), FISH_TYPE
    from FISH_INFO
    group by FISH_TYPE
)
order by ID asc;
