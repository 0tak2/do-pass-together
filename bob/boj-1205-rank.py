'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/1205
- 유형: 구현
'''

def solution(scores, newScore, maxCount):
    scores.append(newScore)
    scores.sort(reverse=True)

    if len(scores) == 1 and maxCount >= 1:
        return 1

    targetRank = 1
    lastPos = 0
    for s in scores:
        if s > newScore:
            targetRank += 1
        
        if s >= newScore:
            lastPos += 1
    
    if lastPos <= maxCount:
        return targetRank
    else:
        return -1

existingCount, newScore, maxCount = map(int, input().split())

scores = []
if existingCount != 0:
    scores = list(map(int, input().split()))

ans = solution(scores, newScore, maxCount)
print(ans)
