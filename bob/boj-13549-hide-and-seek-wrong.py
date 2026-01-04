'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/13549
- 유형: 최단거리
- 첫 접근, 틀린 풀이
'''

from collections import deque

def seek(cur, target):
  q = deque()
  vistied = [False] * 100_001

  q.append((cur, 0))
  vistied[cur] = True

  while len(q) != 0:
    pos, time = q.popleft()

    if pos == target:
      return time

    candidates = [
      (pos*2, time),
      (pos-1, time+1),
      (pos+1, time+1),
    ]

    for newPos, newTime in candidates:
      if newPos >= 0 and newPos < 100_000 and not vistied[newPos]:
        q.append((newPos, newTime))
        vistied[newPos] = True

cur, target = list(map(int, input().split()))
print(seek(cur, target))
