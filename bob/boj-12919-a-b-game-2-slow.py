'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/12919
- 유형: 문자열

* 시간초과
'''

def op1(str):
    return str + 'A'

def op2(str):
    return "".join(reversed(list(str + 'B')))

def solution(str, target):
    if len(str) > len(target):
        return False

    result1 = op1(str)
    if result1 == target:
        return True

    result2 = op2(str)
    if result2 == target:
        return True

    return solution(result1, target) or solution(result2, target)

start = input()
target = input()
print('1' if solution(start, target) else '0')
