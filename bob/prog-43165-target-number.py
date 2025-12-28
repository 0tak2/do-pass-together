'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
- 유형: 구현
'''
def dfs(numbers, target, acc, nextIdx):
    if nextIdx == len(numbers):
        # 모든 문자를 순회했으면 종료
        return 1 if acc == target else 0
    
    currentNumber = numbers[nextIdx]
    return dfs(numbers, target, acc + currentNumber, nextIdx + 1) + dfs(numbers, target, acc - currentNumber, nextIdx + 1)

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)

'''
dfs([1, 1, 1, 1, 1], 3, 0, 0)
-> dfs([1, 1, 1, 1, 1], 3, 1, 1)
  -> dfs([1, 1, 1, 1, 1], 3, 2, 2)
    -> ...
    -> ...
  -> dfs([1, 1, 1, 1, 1], 3, 0, 2)
    -> ...
    -> ...
-> dfs([1, 1, 1, 1, 1], 3, -1, 1)
 -> dfs([1, 1, 1, 1, 1], 3, 1, 1)
 -> dfs([1, 1, 1, 1, 1], 3, 1, 1)
'''
