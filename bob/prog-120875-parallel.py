'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120875
- 유형: 수학, 조합
'''
def solution(dots):
    # 0, 1 -- 2, 3
    # 0, 2 -- 1, 3
    # 0, 3 -- 1, 2
    
    cases = [
        [0, 1, 2, 3],
        [0, 2, 1, 3],
        [0, 3, 1, 2],
    ]
    
    for [a, b, c, d] in cases:
        [x1, y1] = dots[a]
        [x2, y2] = dots[b]
        [x3, y3] = dots[c]
        [x4, y4] = dots[d]
        
        lean1 = (y2 - y1) / (x2 - x1) # y변화량 / x변화량
        lean2 = (y4 - y3) / (x4 - x3)
        if lean1 == lean2:
            return 1
    
    return 0
