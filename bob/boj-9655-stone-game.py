'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/9655
- 유형: 수학, DP
'''

'''
1. DP로 풀기 (32544KB	40ms)

n    턴을 시작한 사람 승리 여부    dp[n]
1    승리                     True 
2    패배                     False
3    승리                     True
4    패배                     False
  이유
  내가 1개를 가져가서 3개가 남음. (dp[3] == True) => 상대가 이김
  3개를 가져가서 1개가 남음. (dp[1] == True) => 상대가 이김
5    승리                     True
  이유
  내가 1개를 가져가서 4개가 남음. (dp[4] == False) => 상대가 짐
  3개를 가져가서 2개가 남음. (dp[2] == False) => 상대가 짐

즉 점화식 dp[n](n개 돌이 남았을 때 해당 턴을 시작한 사람이 승리할 지 여부)는 다음과 같이 정의할 수 있다.
dp[n] = !(다음 턴에 (n-1)개 돌이 있을 때 상대가 시작해서 이길 여부) OR !(다음 턴에 (n-3)개 돌이 있을 때 상대가 시작해서 이길 여부)
      = !dp[n-1] || !dp[n-3]
'''
def solution1(n):
  table = {}

  table[1] = True
  table[2] = False
  table[3] = True

  if n <= 3:
    return "SK" if table[n] else "CY"
  
  for i in range(4, n+1):
    table[i] = (not table[i-1]) or (not table[i-3])
  
  return "SK" if table[n] else "CY"

'''
2. 패턴 발견 (32412KB	40ms)

DP 풀이를 잘 보면, 항상 N이 홀수이면 상근이가 이기고, 짝수이면 창영이가 이긴다는 것을 알 수 있다.
'''
def solution2(n):
  isOdd = n % 2 == 1
  return "SK" if isOdd else "CY"


### INPUT ###
numberOfStones = int(input())
answer = solution2(numberOfStones)
print(answer)
