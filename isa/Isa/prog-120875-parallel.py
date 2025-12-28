'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120875
- 유형: 구현
'''

def solution(dots):
    a, b, c, d = dots
    
    if (b[1]-a[1])/(b[0]-a[0]) == (d[1]-c[1])/(d[0]-c[0]):
        return 1
    elif (c[1]-a[1])/(c[0]-a[0]) == (d[1]-b[1])/(d[0]-b[0]):
        return 1
    elif (d[1]-a[1])/(d[0]-a[0]) == (c[1]-b[1])/(c[0]-b[0]):
        return 1
    else:
        return 0