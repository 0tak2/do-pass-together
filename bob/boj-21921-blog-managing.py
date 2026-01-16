'''
- 플랫폼: 백준
- 문제: [블로그](https://www.acmicpc.net/problem/21921)
- 유형: 슬라이딩 윈도우
'''

def solution(totalDays, counts, windowSize):
  maxCount = 0
  windows = 0

  currentCount = 0
  for i in range(windowSize):
    currentCount += counts[i]
    maxCount = currentCount
    windows = 1

  for i in range(1, totalDays - windowSize + 1):
    currentCount -= counts[i-1] # 사라지는 부분
    currentCount += counts[i+windowSize-1] # 추가되는 부분
    if currentCount > maxCount:
      maxCount = currentCount
      windows = 1
    elif currentCount == maxCount:
      windows += 1

  return maxCount, windows

totalDays, windowSize = map(int, input().split())
counts = list(map(int, input().split()))

maxCount, windows = solution(totalDays, counts, windowSize)
if maxCount == 0:
  print('SAD')
else:
  print(f'{maxCount}\n{windows}')
