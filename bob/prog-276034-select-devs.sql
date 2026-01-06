-- https://school.programmers.co.kr/learn/courses/30/lessons/276034
-- select, bit

select ID, EMAIL, FIRST_NAME, LAST_NAME from DEVELOPERS
    where SKILL_CODE & (select (
        select CODE from SKILLCODES
            where NAME = 'Python'
        ) | (
        select CODE from SKILLCODES
            where NAME = 'C#'
    )) != 0
    order by ID asc;
