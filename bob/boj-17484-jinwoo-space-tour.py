'''
- 플랫폼: 백준
- 문제: [진우의 달 여행 (Small)](https://www.acmicpc.net/problem/17484)
- 유형: DP

방향성이 조건으로 있기 때문에 단순히 2차원 테이블로는 풀 수 없다. 방향성까지 포함해서 3차원 테이블을 만든다.
정의: dp[i][j][d]는 i행 j열까지 직전에 d방향을 선택해서 도착했을 때 최소 비용. d=0이면 왼쪽 위에서 오른쪽으로 내려옴, 1이면 수직 위에서 아래로 내려옴, 2이면 오른쪽 위에서 왼쪽으로 내려온 것으로 정의.
점화식
  dp[i][j][0] = {현재 셀에서 필요로 하는 연료} + min(dp[i-1][j-1][1], dp[i-1][j-1][2])
  dp[i][j][1] = {현재 셀에서 필요로 하는 연료} + min(dp[i-1][j][0], dp[i-1][j][2])
  dp[i][j][2] = {현재 셀에서 필요로 하는 연료} + min(dp[i-1][j+1][0], dp[i-1][j+1][1])

문제에서는 최소 누적 비용을 구하는 것이므로 dp[마지막 행][...][...] 중 최소값을 반환하면 된다.
'''

INF = int(1e9)

def dp(space):
  # table[row][col][direction]
  table = [[[0] * 3 for _ in range(len(space[0]))] for _ in range(len(space))] # 3차원 초기화
  
  # 시작값 초기화 (지구))
  for i in range(len(space[0])):
    table[0][i][0] = space[0][i]
    table[0][i][1] = space[0][i]
    table[0][i][2] = space[0][i]
  
  for i in range(1, len(space)):
    for j in range(len(space[0])):
      if j - 1 >= 0:
        table[i][j][0] = space[i][j] + min(table[i-1][j-1][1], table[i-1][j-1][2])
      else:
        table[i][j][0] = INF
      
      table[i][j][1] = space[i][j] + min(table[i-1][j][0], table[i-1][j][2])

      if j + 1 < len(space[0]):
        table[i][j][2] = space[i][j] + min(table[i-1][j+1][0], table[i-1][j+1][1])
      else:
        table[i][j][2] = INF
  
  minValue = INF
  for cell in table[-1]:
    for subcell in cell:
      if subcell < minValue:
        minValue = subcell
  
  return minValue

n, m = map(int, input().split())
space = [[] for _ in range(n) ]

for y in range(n):
  row = list(map(int, input().split()))
  space[y] = row

ans = dp(space)
print(ans)
