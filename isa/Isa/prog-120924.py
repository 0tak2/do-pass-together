'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120924
- 유형: 구현
'''
def solution(common):
    answer = 0
    
    if common[1] - common[0] == common[2] - common[1]:
        answer = common[-1] + (common[1] - common[0])
    else:
        answer = common[-1] * (common[1]//common[0])
    
    return answer
