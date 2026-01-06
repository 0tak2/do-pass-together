/* 
- 플랫폼: 리트코드
- URL: https://leetcode.com/problems/rank-scores/?envType=problem-list-v2&envId=database
- 유형: 랭킹
*/

# Write your MySQL query statement below
SELECT score, DENSE_RANK() OVER(ORDER BY score DESC) AS 'rank'
FROM Scores;