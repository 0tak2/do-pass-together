'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/1806
- 유형: 부분합
* 오답. 연속된 수의 부분합을 구해야하므로 이러한 방식으로는 구할 수 없다.
'''
def solution(numbers):
    sum = 0
    result = 0
    for i, n in enumerate(numbers):
        sum += n
        if sum > s:
            result = i+1
            break
    
    return result


n, s = map(int, input().split())
numbers = sorted(list(map(int, input().split())), reverse=True)

result = solution(numbers)
print(result)
