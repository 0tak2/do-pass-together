'''
- 플랫폼: 백준
- 문제: [크로스 컨트리](https://www.acmicpc.net/problem/9017)
- 유형: 구현
'''

def solution(scores):
    lastTeamId = max(scores) # 마지막 팀 번호
    teamMatesCount = [0] * lastTeamId # 출전한 팀원 명 수
    scoresByTeams = [[] for _ in range(lastTeamId)] # 팀별로 파티션한 점수
    sumByTeams = [0] * lastTeamId # 팀별 점수 합계

    minTeamId = None
    minSum = int(1e9)

    for teamId in scores:
        teamMatesCount[teamId-1] += 1
    
    skipCount = 0
    for i, teamId in enumerate(scores):
        if teamMatesCount[teamId-1] != 6:
            skipCount += 1
            continue

        scoresByTeams[teamId-1].append(i+1-skipCount)

    for i, teamScores in enumerate(scoresByTeams):
        if not teamScores:
            continue

        for j in range(4):
            sumByTeams[i] += teamScores[j]

        if minTeamId is None:
            minTeamId = i + 1
            minSum = sumByTeams[i]
            continue

        if sumByTeams[i] < minSum:
            minTeamId = i + 1
            minSum = sumByTeams[i]
            continue
        elif sumByTeams[i] == minSum:
            if scoresByTeams[i][4] < scoresByTeams[minTeamId-1][4]:
                minTeamId = i + 1
                minSum = sumByTeams[i]

    if minTeamId is None:
        print('should not reach here...')

    return minTeamId

cases = int(input())
for _ in range(cases):
    _ = input()
    scores = list(map(int, input().split()))
    ans = solution(scores)
    print(ans)
