-- https://school.programmers.co.kr/learn/courses/30/lessons/131115
-- select, limit

-- 나 바본가봐
-- select
--     PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
-- from FOOD_PRODUCT
-- where PRICE = (select max(PRICE) from FOOD_PRODUCT);

select
    PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
from FOOD_PRODUCT
order by PRICE desc limit 1
