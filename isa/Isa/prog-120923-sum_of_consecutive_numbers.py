'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120923
- 유형: 구현, 수학
'''

def solution(num, total):
    answer = []
    alpha = 0
    
    for a in range(1, num):
        alpha += a
    
    x = int((total - alpha) / num)
    
    for i in range(num):
        answer.append(x + i)
    
    return answer