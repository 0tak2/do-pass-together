'''
- 플랫폼: 백준
- 문제: [최소 힙](https://www.acmicpc.net/problem/1927)
- 유형: 자료구조, 힙
'''

import heapq
import sys

input = sys.stdin.readline
print = sys.stdout.write

h = []

for _ in range(int(input().strip())):
  cmd = int(input().strip())
  if cmd == 0:
    output = heapq.heappop(h) if h else 0
    print(str(output) + '\n')
  else:
    heapq.heappush(h, cmd)
