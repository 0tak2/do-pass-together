'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/4659
- 유형: 구현, 문자열
- 32412KB, 32ms
'''
def check(str):
  hasVow = False

  vows = ['a', 'e', 'i', 'o', 'u']
  acceptableSeqLetters = ['e', 'o']

  prev = ''
  seqConsOrVowsCount = 0
  for c in str:
    if c in vows:
      hasVow = True
    
    if (prev in vows and c in vows) or \
      ((not prev in vows) and (not c in vows)):
      seqConsOrVowsCount += 1
      # print(f'{c} -- {seqConsOrVowsCount}')

      if seqConsOrVowsCount >= 3:
        return False
    else:
      seqConsOrVowsCount = 1

    if not prev in acceptableSeqLetters and prev == c:
      return False

    prev = c
  
  return hasVow

while True:
  password = input()
  if password == "end":
    break
  
  if check(password):
    print(f'<{password}> is acceptable.')
  else:
    print(f'<{password}> is not acceptable.')
