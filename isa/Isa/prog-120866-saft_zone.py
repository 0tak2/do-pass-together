'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120866
- 유형: 구현
'''

def solution(board):
    answer = 0
    bomb_cor = []
    
    # 폭탄 좌표 찾기
    for idx1, val1 in enumerate(board):
        for idx2, val2 in enumerate(val1):
            if val2 == 1:
                bomb_cor.append((idx1, idx2))

    for bomb in bomb_cor:
        x = bomb[0]
        y = bomb[1]
        
        for i1, v1 in enumerate(board):
            for i2, v2 in enumerate(v1):
                if (i1 >= x-1 and i1 <= x+1) and (i2 >= y-1 and i2 <= y+1):
                    board[i1][i2] = 1
    
    answer = sum(row.count(0) for row in board)
                
    return answer