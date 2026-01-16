'''
- 플랫폼: 백준
- 문제: [수 이어 쓰기](https://www.acmicpc.net/problem/1515)
- 유형: 구현, 브루트포스

* 풀어보니 간단하지만 사고가 간단하지 않았던 문제
'''

numbers = input()
pos = 0

cur = 1
while pos < len(numbers):
    cmpTo = str(cur)
    for c in cmpTo:
        if pos >= len(numbers):
            break
        if c == numbers[pos]:
            pos += 1
    cur += 1

print(cur-1)
