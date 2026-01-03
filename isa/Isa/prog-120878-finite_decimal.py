'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120878
- 유형: 구현, 수학
'''

from fractions import Fraction

def solution(a, b):
    frac = Fraction(a, b)
    
    p = frac.denominator
    
    while p > 1:
        if p % 2 == 0:
            p = p //2
        elif p % 5 == 0:
            p = p // 5
        else:
            return 2
        
    return 1

# 아래는 제미나이 추천 코드 (라이브러리 제약 대비)
import math

def solution(a, b):
    b //= math.gcd(a, b)
    
    while b % 2 == 0:
        b //= 2
        
    while b % 5 == 0:
        b //= 5
        
    return 1 if b == 1 else 2