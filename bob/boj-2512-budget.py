'''
- 플랫폼: 프로그래머스
- 문제: [예산](https://www.acmicpc.net/problem/2512)
- 유형: 이진탐색
'''

def getSum(data, cut):
    sum = 0
    for val in data:
        if val > cut:
            sum += cut
        else:
            sum += val
    return sum

def find(requests, total):
    minCut = 0
    maxCut = max(requests)
    successCut = 0
    
    while minCut <= maxCut:
        middle = (minCut + maxCut) // 2
        currentSum = getSum(requests, middle)

        if currentSum < total:
            successCut = middle
            minCut = middle + 1
        elif currentSum > total:
            maxCut = middle - 1
        else:
            return middle

    return successCut

sublands = int(input())
requests = list(map(int, input().split()))
total = int(input())

print(find(requests, total))
