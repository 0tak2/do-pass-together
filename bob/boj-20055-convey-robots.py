'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/20055
- 유형: 구현, 링크드리스트
'''

from collections import deque

def solution(n, k, durabilities):
    durabilities = deque(durabilities)
    robots = deque([False] * n)

    step = 0
    while True:
        step += 1

        # 1. 회전
        durabilities.rotate(1)
        robots.rotate(1)
        robots[n-1] = False

        # 2. 로봇 이동
        for i in reversed(range(n)):
            nextIndex = i + 1
            if nextIndex > n - 1:
                nextIndex = 0
            
            if robots[i] and not robots[nextIndex] and durabilities[nextIndex] > 0:
                robots[i] = False
                robots[nextIndex] = True
                durabilities[nextIndex] -= 1
            
            if nextIndex == n-1:
                robots[nextIndex] = False
        
        # 3. 로봇 올리기
        if durabilities[0] > 0 and not robots[0]:
            robots[0] = True
            durabilities[0] -= 1
        
        # 4. 내구도 세기
        lowDurabilities = 0
        for d in durabilities:
            if d == 0:
                lowDurabilities += 1
            
            if lowDurabilities >= k:
                return step


n, k = map(int, input().split())
durabilities = map(int, input().split())

result = solution(n, k, durabilities)
print(result)
