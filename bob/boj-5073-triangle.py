'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/5073
- 유형: 수학, 구현
'''
while True:
  [a, b, c] = map(int, input().split())

  if a == 0 and b == 0 and c == 0:
    break

  maxLength = max(a, b, c)
  others = (a + b + c) - maxLength
  if maxLength >= others:
    print("Invalid")
    continue

  if a == b and b == c and a == c:
    print("Equilateral")
    continue

  if a == b or b == c or a == c:
    print("Isosceles")
    continue

  if a != b and b != c and a != c:
    print("Scalene")
