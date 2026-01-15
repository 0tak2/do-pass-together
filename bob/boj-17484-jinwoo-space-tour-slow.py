'''
- 플랫폼: 백준
- 문제: [진우의 달 여행 (Small)](https://www.acmicpc.net/problem/17484)
- 유형: 브루트포스
'''

class MinValue:
  def __init__(self, value):
    self.value = value
  
  def set(self, newValue):
    if newValue < self.value:
      self.value = newValue

'''
우주선을 전진시킨다
prevDir: 직전에 선택한 방향. -1, 0, 1, None 중 하나
'''
def goForward(space, nextY, nextX, prevDir, accumFuel, minValueHolder):
  if nextY == len(space):
    minValueHolder.set(accumFuel)
    return

  if not (0 <= nextX < len(space[0])):
    return

  fuel = accumFuel + space[nextY][nextX]

  dirs = filter(lambda x: x != prevDir, [-1, 0, 1])
  for d in dirs:
    goForward(space=space, nextY=nextY+1, nextX=nextX+d, prevDir=d, accumFuel=fuel, minValueHolder=minValue)


n, m = map(int, input().split())
space = [[] for _ in range(n) ]

for y in range(n):
  row = list(map(int, input().split()))
  space[y] = row

minValue = MinValue(int(1e9))

for startPos in range(m):
  goForward(space=space, nextY=0, nextX=startPos, prevDir=None, accumFuel=0, minValueHolder=minValue)

print(minValue.value)
