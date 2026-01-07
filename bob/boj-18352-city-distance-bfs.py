'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/18352
- 유형: 최단거리

* 간선에 가중치가 없기 떄문에 BFS로 충분히 풀이 가능.
* DFS로 풀었을 때보다 성능이 좋음. 100920KB, 716ms
'''

import sys
from collections import deque

def bfs(connections, start):
    dist = [-1] * len(connections)
    q = []
    
    dist[start] = 0
    q = deque()
    q.append(start)

    while q:
        city = q.popleft()

        for node in connections[city]:
            if dist[node] != -1:
                continue
            dist[node] = dist[city] + 1
            q.append(node)
    
    return dist

# INPUT
citiesCount, edgesCount, targetDistance, startCity = map(int, sys.stdin.readline().split())

connections = [[] for _ in range(citiesCount+1)] # 0번 인덱스는 더미

for _ in range(edgesCount):
    c1, c2 = map(int, sys.stdin.readline().split()) # input()을 쓰면 시간초과
    connections[c1].append(c2)

dist = bfs(connections, startCity)
didFind = False
for city, d in enumerate(dist):
    if d == targetDistance:
        didFind = True
        sys.stdout.write(f'{city}\n')

if not didFind:
    sys.stdout.write('-1')
