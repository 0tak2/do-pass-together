people = []

# 입력
total = int(input())
for i in range(total):
  [m, h] = map(int, input().split())
  people.append((i, m, h))

# 계산
ranks = []
for p in people:
  (i1, m1, h1) = p
  currentRank = 1

  for q in people:
    (i2, m2, h2) = q
    if i2 == i1: # 동일 인물이면 스킵
      continue

    if m1 < m2 and h1 < h2:
      currentRank += 1

  ranks.append(currentRank)

print(" ".join(map(str, ranks)))
