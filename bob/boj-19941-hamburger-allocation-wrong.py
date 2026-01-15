'''
- 플랫폼: 백준
- 문제: [햄버거 분배](https://www.acmicpc.net/problem/19941)
- 유형: 구현

* 잘못된 접근
'''
def solution(bench, maxDistance):
  allocatedCount = 0

  for pos, c in enumerate(bench):
    if c == "H":
      # 이 햄버거 먹을 사람 찾기
      for i in range(1, maxDistance + 1):
        leftIndex = pos - i
        rightIndex = pos + i

        # print(f'c={c}')
        # print(f'leftIndex={leftIndex}')
        # print(f'rightIndex={rightIndex}')

        if leftIndex >= 0 and bench[leftIndex] == "P":
          allocatedCount += 1
          bench[leftIndex] = "_"
          break

        if rightIndex < len(bench) and bench[rightIndex] == "P":
          allocatedCount += 1
          bench[rightIndex] = "_"
          break
  
  return allocatedCount

_, maxDistance = map(int, input().split())
bench = [x for x in input()]
ans = solution(bench, maxDistance)
print(ans)
