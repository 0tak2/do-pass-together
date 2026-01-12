'''
- 플랫폼: 백준
- 문제: [주유소](https://www.acmicpc.net/problem/13305)
- 유형: 구현, 그리디
'''

def solution(cities, distances, gasPrices):
    sum = 0
    minPrice = int(1e10)
    for i in range(cities-1):
        if gasPrices[i] < minPrice:
            minPrice = gasPrices[i]
        
        sum += minPrice * distances[i]

    return sum

cities = int(input())
distances = list(map(int, input().split()))
gasPrices = list(map(int, input().split()))

ans = solution(cities, distances, gasPrices)
print(ans)
