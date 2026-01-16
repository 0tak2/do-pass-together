'''
- 플랫폼: 백준
- 문제: [비슷한 단어](https://www.acmicpc.net/problem/2607)
- 유형: 문자열

* 해시테이블을 이용해 풀어보려고 했던 시도. 잘 하면 가능할 것 같지만, 기수 카운팅과 비교해 이점이 없어서 결국엔 포기했음.
'''
def isSimilar(a, b, compositionOfA):
#   print(f'a={a} b={b}')
  if not compositionOfA:
    for c in a:
      compositionOfA[c] = compositionOfA.get(c, 0) + 1
  
  compositionOfB = {}
  for c in b:
    compositionOfB[c] = compositionOfB.get(c, 0) + 1
  
  keysSet = set()
  for k in compositionOfA:
    keysSet.add(k)
  for k in compositionOfB:
    keysSet.add(k)

  diffCount = 0
  for k in keysSet:
    if diffCount > 1:
      return False

    v1 = compositionOfA.get(k, 0)
    v2 = compositionOfB.get(k, 0)

    print(f'k={k} abs(v1 - v2)={abs(v1 - v2)}')

    if abs(v1 - v2) > 1:
      return False
    elif abs(v1 - v2) == 1:
      diffCount += 1

  return diffCount <= 1

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

composition = {}
ans = 0
for w in words:
  if isSimilar(cmpTo, w, composition):
    ans += 1
print(ans)
