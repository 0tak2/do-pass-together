'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/1806
- 유형: 부분합, 투 포인터
'''
def solution(numbers, target):
    currentSum = 0
    left = 0
    right = 0
    minLength = 100_001

    while left <= right:
        # 잘못돈 조건 처리
        # if currentSum < target: # 아직 부분합이 조건 미만인 경우 -> 부분합 늘리기
        #     if right + 1 == len(numbers):
        #         break
            # currentSum += numbers[right]
            # right += 1
        # else: # 부분합이 조건 이상인 경우 -> 길이 기록, 길이 줄이기
            # minLength = min(minLength, right-left)

            # currentSum -= numbers[left]
            # left += 1

        if currentSum >= target: # 부분합이 조건 이상인 경우 -> 길이 기록, 길이 줄이기 [먼저 체크]
            minLength = min(minLength, right-left)

            currentSum -= numbers[left]
            left += 1
        elif right == len(numbers): # 종료 조건
            break
        else: # 아직 부분합이 조건 미만인 경우 -> 부분합 늘리기
            currentSum += numbers[right]
            right += 1
    
    return minLength if minLength != 100_001 else 0

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

result = solution(numbers, s)
print(result)
