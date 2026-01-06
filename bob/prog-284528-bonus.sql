-- https://school.programmers.co.kr/learn/courses/30/lessons/284528
-- Sub Query, Group By, AVG
-- CASE 내부에도 집계함수를 쓸 수 있음

SELECT 
    EMP_NO,
    EMP_NAME,
    GRADE,
    CASE
        WHEN GRADE = 'S' THEN SAL * 0.20
        WHEN GRADE = 'A' THEN SAL * 0.15
        WHEN GRADE = 'B' THEN SAL * 0.10
        ELSE 0
    END AS BONUS
FROM (
    SELECT
        e.EMP_NO,
        e.EMP_NAME,
        e.SAL,
        CASE
            WHEN AVG(g.SCORE) >= 96 THEN 'S'
            WHEN AVG(g.SCORE) >= 90 THEN 'A'
            WHEN AVG(g.SCORE) >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE
    FROM HR_EMPLOYEES AS e
    INNER JOIN HR_GRADE AS g ON e.EMP_NO = g.EMP_NO
    GROUP BY e.EMP_NO, e.EMP_NAME, e.SAL
) AS t
ORDER BY EMP_NO;
