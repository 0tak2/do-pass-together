'''
- 플랫폼: 백준
- 문제: [카드2](https://www.acmicpc.net/problem/2164)
- 유형: 큐
'''

from collections import deque

def solution(lastCard):
    q = deque()

    for i in range(lastCard):
        cardNumber = i + 1
        q.append(cardNumber)

    while len(q) > 1:
        q.popleft()

        top = q.popleft()
        q.append(top)

    return q.popleft()

lastCard = int(input())
ans = solution(lastCard)
print(ans)
