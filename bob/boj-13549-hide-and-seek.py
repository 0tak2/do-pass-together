'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/13549
- 유형: 최단거리
'''

from collections import deque

INF = 100_000_000_000

def seek(cur, target):
  q = deque()
  dist = [INF] * 100_001

  q.append(cur)
  dist[cur] = 0

  while len(q) != 0:
    pos = q.popleft()

    if pos == target:
      return dist[pos]

    candidates = [
      (pos*2, 0), # 새 위치, 소요 시간
      (pos-1, 1),
      (pos+1, 1),
    ]

    for newPos, time in candidates:
      if 0 <= newPos <= 100_000: # 파이썬은 부등식 연결이 가능
        if dist[newPos] <= dist[pos] + time:
          continue # 이전에 계산해둔 거리가 이미 최단거리면 아래를 추가할 필요가 없음
        
        dist[newPos] = dist[pos] + time # 방문처리 겸 거리(시간) 업데이트

        if time == 0:
          q.appendleft(newPos) # 먼저 탐색 강제
        else:
          q.append(newPos)

cur, target = list(map(int, input().split()))
print(seek(cur, target))
