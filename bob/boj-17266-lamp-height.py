'''
- 플랫폼: 백준
- 문제: [어두운 굴다리](https://www.acmicpc.net/problem/17266)
- 유형: 구현, 이진탐색

* 이진탐색 적용 가능
* 높이에 따라 모든 블록을 밝힐 수 있는지 여부를 다음과 같이 나열해볼 수 있다.
 [ (min) 불가능, 불가능, 불가능, 가능, 가능, 가능, ... (max) ]
* 우리가 구해야하는 것은 처음으로 가능이 되는 높이값, 즉 최소 높이이다.
* 최소~최대 범위에서 시작해 중간 지점을 확인하는 방법을 반복해 이 값을 찾는다.
'''

def canCoverRoad(n, m, lamps, height):
    # 시작점을 비출 수 있나?
    if lamps[0] - height > 0:
        return False # 비출 수 없다
    
    # 램프와 램프 사이에 빈 공간이 없나?
    for i in range(1, m):
        if lamps[i-1] + height < lamps[i] - height:
            return False # 이전 램프 끝 점과 다음 램프 시작 점이 중첩되지 않아서 비출 수 없다
    
    # 끝 점을 비출 수 있나?
    if lamps[-1] + height < n:
        return False # 비출 수 없다
    
    # 모두 통과
    return True

def solution(n, m, lamps):
    low = 1
    high = n
    ans = n

    while low <= high:
        mid = (low + high) // 2
        if canCoverRoad(n, m, lamps, mid):
            ans = mid

            # 더 줄이기 시도
            high = mid - 1
        else:
            # 더 키우기 시도
            low = mid + 1
    
    return ans

length = int(input())
numberOfLamps = int(input())
lampPoses = list(map(int, input().split()))

ans = solution(length, numberOfLamps, lampPoses)
print(ans)
