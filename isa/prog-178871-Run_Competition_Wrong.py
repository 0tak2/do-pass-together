'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/178871
- 유형: 구현
'''

def solution(players, callings):
    for call in callings:
        idx = players.index(call)
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
    
    return players