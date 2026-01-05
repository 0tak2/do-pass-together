'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/12919
- 유형: 문자열
'''

def reverse1(string):
    return string[:-1]

def reverse2(string):
    return "".join(reversed(list(string)))[:-1]

def solution(target, start):
    if len(target) == 0:
        return False

    result1 = False
    if target[-1] == 'A':
        reversed1 = reverse1(target)
        if reversed1 == start:
            return True
        else:
            result1 = solution(reversed1, start)
    
    result2 = False
    if target[0] == 'B':
        reversed2 = reverse2(target)
        if reversed2 == start:
            return True
        else:
            result2 = solution(reversed2, start)
    
    return result1 or result2

start = input()
target = input()
print('1' if solution(target, start) else '0')
