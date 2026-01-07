'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/172928
- 유형: 구현
'''

def solution(park, routes):
    x, y = 0, 0
    directions = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = i, j
                break
    
    for route in routes:
        op, n = route.split()
        next_x, next_y = x, y
        can_move = True
        
        for r in range(int(n)):
            next_x += directions[op][0]
            next_y += directions[op][1]
            
            if not(0 <= next_x < len(park) and 0 <= next_y < len(park[0])):
                can_move = False
                break
            
            if park[next_x][next_y] == 'X':
                can_move = False
                break
        
        if can_move:
            x, y = next_x, next_y

    return [x, y]