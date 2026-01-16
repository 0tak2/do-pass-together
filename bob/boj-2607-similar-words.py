'''
- 플랫폼: 백준
- 문제: [비슷한 단어](https://www.acmicpc.net/problem/2607)
- 유형: 아스키코드, 구현
'''
def isSimilar(a, b):
  if abs(len(a) - len(b)) > 1: # 0 또는 1이어야 함. 그 초과인 경우 무조건 불가능.
    return False

  # 초기화
  counts = [0] * 26

  for c in a:
    index = ord(c) - ord('A')
    counts[index] += 1
  
  # 비교
  diff = 0
  for c in b:
    index = ord(c) - ord('A')
    
    cmpCount = counts[index]
    if cmpCount > 0:
      counts[index] -= 1
    else:
      diff += 1
  
  return diff <= 1 \
      and sum(counts) <= 1 # 'AAA'와 'AAB'와 같은 경우도 비슷한 경우이므로, 이런 경우를 세기 위해 추가

cmpTo = None
words = []

total = int(input())
for i in range(total):
  if i == 0:
    cmpTo = input()
    continue

  words.append(input())

# print(f'cmpTo: {cmpTo}')
# print(f'words: {words}')

ans = 0
for w in words:
  if isSimilar(cmpTo, w):
    ans += 1
print(ans)
