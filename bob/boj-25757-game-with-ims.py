'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/25757
- 유형: 구현
'''

def getMinimumUsers(gameCode):
  if gameCode == 'Y':
    return 2
  
  if gameCode == 'F':
    return 3

  if gameCode == 'O':
    return 4

firstLine = input().split()
requestCounts = int(firstLine[0])
game = firstLine[1]

requestUsers = set()

for _ in range(requestCounts):
  name = input()
  requestUsers.add(name)

answer = len(requestUsers) // (getMinimumUsers(game) - 1)
print(answer)
