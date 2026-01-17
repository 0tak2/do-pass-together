'''
- 플랫폼: 백준
- 문제: [타노스](https://www.acmicpc.net/problem/20310)
- 유형: 문자열, 그리디
'''

''' 틀린 접근. 반례: '1100', '111000'
S = input()
counts = [0] * 2
for c in S:
  if c == '0':
    counts[0] += 1
  elif c == '1':
    counts[1] += 1

counts[0] = counts[0] // 2
counts[1] = counts[1] // 2

ans = '0' * max(counts[0], 1) + '1' * max(counts[1], 1)
print(ans)
'''

S = input()
counts = [0] * 2
count0Goal = 0
count1Goal = 0

for c in S:
  if c == '0':
    counts[0] += 1
  elif c == '1':
    counts[1] += 1
count0Goal = counts[0] // 2
count1Goal = counts[1] // 2

sList = list(S) # 파이썬에서 String은 불변이므로 문자 배열을 만들었다

# 앞에서부터 절반의 1을 지운다
for i in range(len(sList)):
  if counts[1] == count1Goal:
    break

  if sList[i] == '1':
    sList[i] = '_'
    counts[1] -= 1

for i in range(len(sList)-1, -1, -1):
  if counts[0] == count0Goal:
    break

  if sList[i] == '0':
    sList[i] = '_'
    counts[0] -= 1

# 문자열을 재조합한다
ans = ""
for c in sList:
  if c != '_':
    ans += c
  
print(ans)
