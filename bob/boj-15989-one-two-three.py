'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/15989
- 유형: DP
'''

maxNumber = 10000

table = [1] * (maxNumber + 1) # 1만 쓸 수 있을 떄는 n별로 1번. table[0]도 그냥 1로 선언 해둠.

# 2를 허용하면, 현재 만들 수 있는 방법의 수에 이전에 2를 더하지 않았을 떄 케이스가 추가됨
for i in range(2, maxNumber + 1):
  table[i] += table[i-2]

# 3을 허용하면, 현재 만들 수 있는 방법의 수에 이전에 3를 더하지 않았을 떄 케이스가 추가됨
for i in range(3, maxNumber + 1):
  table[i] += table[i-3]

total = int(input())
for _ in range(total):
  target = int(input())
  print(table[target])
