'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/18352
- 유형: 최단거리

* 모든 간선의 가중치를 1로 두면 다익스트라로 풀 수 있음
* BFS로 풀었을 때보다 성능이 나쁨. 가중치가 모두 같은데 우선순위 큐 떄문에 매번 연산이 발생해서 그런 듯. 109884KB, 2172ms
'''

import heapq
import sys

INF = int(1e9)

def dijk(connections, start):
    dist = [INF] * len(connections)
    q = []
    
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        d, city = heapq.heappop(q)

        if d > dist[city]:
            continue

        for node in connections[city]:
            cost = d + 1

            if cost < dist[node]:
                dist[node] = cost
                heapq.heappush(q, (cost, node))
    
    return dist

# INPUT
citiesCount, edgesCount, targetDistance, startCity = map(int, sys.stdin.readline().split())

connections = [[] for _ in range(citiesCount+1)] # 0번 인덱스는 더미

for _ in range(edgesCount):
    c1, c2 = map(int, sys.stdin.readline().split()) # input()을 쓰면 시간초과
    connections[c1].append(c2)

dist = dijk(connections, startCity)
didFind = False
for city, d in enumerate(dist):
    if d == targetDistance:
        didFind = True
        sys.stdout.write(f'{city}\n')

if not didFind:
    sys.stdout.write('-1')
