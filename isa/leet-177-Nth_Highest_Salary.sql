/* 
- 플랫폼: 리트코드
- URL: https://leetcode.com/problems/nth-highest-salary/description/?envType=problem-list-v2&envId=database
- 유형: 정렬
*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    declare m int;
    set m = n - 1;

    RETURN (
      # Write your MySQL query statement below.
    select distinct salary
    from Employee
    order by salary desc
    limit 1
    offset m
    
  );
END