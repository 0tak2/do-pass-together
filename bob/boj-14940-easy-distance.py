'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/14940
- 유형: BFS
'''

from collections import deque

dys = [-1, 1, 0, 0]
dxs = [0, 0, -1, 1]

def solution(mapData, startY, startX):
    q = deque()
    dist = [[-1] * len(mapData[0]) for _ in range(len(mapData))]

    q.append((startY, startX))
    dist[startY][startX] = 0

    while len(q) != 0:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dys[i]
            nx = x + dxs[i]

            if ny >= 0 and \
                ny < len(mapData) and \
                nx >= 0 and \
                nx < len(mapData[0]) and \
                mapData[ny][nx] != 0 and \
                dist[ny][nx] == -1:
                
                q.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1
    
    for y, row in enumerate(mapData):
        for x, c in enumerate(row):
            if c == 0:
                dist[y][x] = 0

    return dist

mapData = []
n, m = map(int, input().split())
startY = None
startX = None
for y in range(n):
    row = list(map(int, input().split()))

    for x, r in enumerate(row):
        if r == 2:
            startY = y
            startX = x

    mapData.append(row)

result = solution(mapData, startY, startX)
for row in result:
    print(" ".join(map(str, row)))
