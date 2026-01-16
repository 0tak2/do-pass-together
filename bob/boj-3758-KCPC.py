'''
- 플랫폼: 백준
- 문제: [KCPC](https://www.acmicpc.net/problem/3758)
- 유형: 구현, 정렬
'''

def solution(teams, questions, targetId, logs):
  sumByTeam = [0] * (teams + 1)
  submissionsByTeam = [0] * (teams + 1)
  lastSubmissionTime = [0] * (teams + 1)
  maxScoresByTeam = [[0 for _ in range(questions+1)] for _ in range(teams+1)] # maxScoresByTeam[t][q] -> t 팀의 q 문제 최고 점수

  for i, (t, q, s) in enumerate(logs):
    maxScoresByTeam[t][q] = max(maxScoresByTeam[t][q], s)
    submissionsByTeam[t] += 1
    lastSubmissionTime[t] = i
  
  for t, maxScores in enumerate(maxScoresByTeam):
    sumByTeam[t] += sum(maxScores)

  stats = [(0, 0, 0, 0)] # 더미 데이터로 초기화. (점수 합, 제출 횟수, 마지막 제출 시각, 팀 번호)
  for t in range(1, teams+1):
    stats.append((
      sumByTeam[t],
      submissionsByTeam[t],
      lastSubmissionTime[t],
      t
    ))
  
  stats.sort(key=lambda x: (-x[0], x[1], x[2])) # 내림차, 오름차, 오름차 => ⭐️ 이렇게 이전 방식의 비교 함수가 아니라 DSU 패턴으로 튜플을 이용해 간단하게 정렬할 수 있다
  for idx, (_, _, _, tId) in enumerate(stats):
    if tId == targetId:
      return idx + 1
  
  return -1

cases = int(input())
for _ in range(cases):
  teams, questions, targetTeamId, logsCount = map(int, input().split())
  logs = []
  for _ in range(logsCount):
    teamId, qId, score = map(int, input().split())
    logs.append((teamId, qId, score))
  ans = solution(teams, questions, targetTeamId, logs)
  print(ans)
