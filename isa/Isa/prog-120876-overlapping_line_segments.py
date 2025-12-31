'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120876
- 유형: 구현
- 참고자료: https://docs.python.org/3/library/stdtypes.html#set
'''

def solution(lines):
    interaction_segment = {}

    a = set(range(lines[0][0], lines[0][1]))
    b = set(range(lines[1][0], lines[1][1]))
    c = set(range(lines[2][0], lines[2][1]))
    
    interaction_segment = (a & b) | (b & c) | (c & a)
    
    return len(interaction_segment)