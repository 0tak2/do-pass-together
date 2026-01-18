'''
- 플랫폼: 백준
- 문제: [랭킹전 대기열](https://www.acmicpc.net/problem/20006)
- 유형: 구현
'''

rooms = [] # 원소 형태: ([], firstPlayerLevel)
totalPlayers, capacity = map(int, input().split())

for _ in range(totalPlayers):
  line = input().split()
  level = int(line[0])
  nickname = line[1]
  if not rooms:
    rooms.append((
      [(level, nickname)],
      level
    ))
  else:
    entered = False
    for users, firstLevel in rooms:
      if firstLevel - 10 <= level <= firstLevel + 10 \
        and len(users) < capacity:
        
        users.append((level, nickname))
        entered = True
        break
    
    if not entered:
      rooms.append((
        [(level, nickname)],
        level
      ))

for users, _ in rooms:
  if len(users) == capacity:
    print('Started!')
  else:
    print('Waiting!')
  
  users.sort(key=lambda x: x[1])
  for user in users:
    print(f'{user[0]} {user[1]}')
