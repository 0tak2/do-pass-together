'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/1157
- 유형: 구현, 문자열
'''
def solution(letters):
  table = {}
  maxKeys = []
  maxCount = 0
  
  for c in letters:
    k = c.lower()
    table[k] = table.get(k, 0) + 1
  
  for k, v in table.items():
    if v == maxCount:
      maxKeys.append(k)
    elif v > maxCount:
      maxKeys = [k]
      maxCount = v
  
  if len(maxKeys) == 1:
    return maxKeys[0].upper()
  else:
    return "?"

letters = input()
answer = solution(letters)
print(answer)
