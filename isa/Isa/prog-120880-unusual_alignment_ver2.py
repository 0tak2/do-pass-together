'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120880
- 유형: 구현, 정렬
'''

def solution(numlist, n):
    numlist.sort(key=lambda x: (abs(x - n), -x))
    
    return numlist