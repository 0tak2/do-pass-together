'''
- 플랫폼: 백준
- 문제: [햄버거 분배](https://www.acmicpc.net/problem/19941)
- 유형: 그리디

* 접근 아이디어: 왼쪽에 있는 햄버거부터 먹여야 오른쪽 사람들이 먹을 가능성이 높아진다 (그리디)
'''
def solution(bench, maxDistance):
  allocatedCount = 0

  for pos, c in enumerate(bench):
    if c == "P":
      # 햄버거 찾기
      for i in range(max(0, pos - maxDistance), min(len(bench), pos + maxDistance + 1)):
        if bench[i] == "H":
          allocatedCount += 1
          bench[i] = "_"
          break
  
  return allocatedCount

_, maxDistance = map(int, input().split())
bench = [x for x in input()]
ans = solution(bench, maxDistance)
print(ans)
