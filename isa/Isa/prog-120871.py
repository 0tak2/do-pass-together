'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120871
- 유형: 구현
'''
def solution(n):
    answer = 0
    
    for _ in range(1, n+1):
        answer += 1
        
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
            
    return answer
