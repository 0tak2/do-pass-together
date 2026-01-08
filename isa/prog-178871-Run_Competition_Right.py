'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/178871
- 유형: 구현
'''

def solution(players, callings):
    players_dict = {}
    
    # players 딕셔너리 구조로 전환
    for idx, player in enumerate(players):
        players_dict[player] = idx
    
    for call in callings:
        idx = players_dict[call]
        front_player = players[idx - 1]
        
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        
        players_dict[call] -= 1
        players_dict[front_player] += 1

    return players