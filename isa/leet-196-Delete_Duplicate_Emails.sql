/* 
- 플랫폼: 리트코드
- URL: https://leetcode.com/problems/delete-duplicate-emails/
- 유형: 삭제
*/

DELETE p1
FROM Person AS p1
JOIN Person AS p2
ON p1.email = p2.email
WHERE p1.id > p2.id