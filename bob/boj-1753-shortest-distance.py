'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/1753
- 유형: 최단거리, 다익스트라
'''

import sys
import heapq

inf = int(1e9)
input = sys.stdin.readline
write = sys.stdout.write

def dijk(graph, start):
    dist = [inf] * len(graph)
    dist[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        d, n = heapq.heappop(q)

        if dist[n] < d:
            continue

        for neighbor, weight in graph[n]:
            cost = d + weight

            if cost < dist[neighbor]:
                dist[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))
    
    return dist

nodesCount, edgesCount = map(int, input().split())
start = int(input())
graph = [[] for _ in range(nodesCount+1)] # [ 시작노드:[ [ 끝노드, 가중치 ], ... ] ]
for _ in range(edgesCount):
    n1, n2, c = map(int, input().split())
    graph[n1].append((n2, c))

dist = dijk(graph, start)
for i in range(1, len(dist)):
    d = dist[i]
    output = str(d) if d != inf else 'INF'
    write(f'{output}\n')
