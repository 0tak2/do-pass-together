'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/181832
- 유형: 리스트, 구현
'''

def solution(n):
    answer = [[0] * n for _ in range(n)]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오 / 아 / 왼 / 위
    now = 0 # 현재 방향 인덱스
    x, y = 0, 0 # 현재 좌표
    
    for i in range(1, n*n+1):
        answer[x][y] = i
        
        # 다음 좌표 값
        nx = x + dir[now % 4][0]
        ny = y + dir[now % 4][1]
        
        if not (0 <= nx < n and 0 <= ny < n) or answer[nx][ny] != 0:
            now += 1
            nx = x + dir[now % 4][0]
            ny = y + dir[now % 4][1]
        
        x, y = nx, ny
            
    return answer