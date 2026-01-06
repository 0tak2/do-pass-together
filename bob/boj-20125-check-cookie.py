'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/20125
- 유형: 구현
'''

size = int(input())

headPos = None
heartPos = None

leftArmLength = 0
rightArmLength = 0

legStarted = False
waistLength = 0
leftLegLength = 0
rightLegLength = 0

numberOfStartUnderHeart = 0

for y in range(size):
  line = input()

  # 머리와 심장 찾기
  if headPos is None:
    for x, c in enumerate(line):
        if c == "*":
          headPos = (y, x)
          heartPos = (y+1, x)
          continue
    
  # 팔 길이 재기
  if heartPos is not None \
    and leftArmLength == 0 \
    and rightArmLength == 0:
    for x, c in enumerate(line):
      if c != "*":
        continue

      if x < headPos[1]:
        leftArmLength += 1
        # print(f"left arm ++ //// x={x} y={y}")
      elif x > headPos[1]:
        rightArmLength += 1
        # print(f"right arm ++ //// x={x} y={y}")
  
  # 다리 길이 재기
  if heartPos is not None and y > heartPos[0] and not legStarted:
    if line.count('*') == 2:
      legStarted = True
    else:
      waistLength += 1
  
  if heartPos is not None and y > heartPos[0] and legStarted:
    for x, c in enumerate(line):
      if c == '*':
        if x < headPos[1]:
          leftLegLength += 1
        elif x > headPos[1]:
          rightLegLength += 1

print(heartPos[0]+1, end=' ')
print(heartPos[1]+1, end='\n')
print(leftArmLength, end=' ')
print(rightArmLength, end=' ')
print(waistLength, end=' ')
print(leftLegLength, end=' ')
print(rightLegLength, end='')
