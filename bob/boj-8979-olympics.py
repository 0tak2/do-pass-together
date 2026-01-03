'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/8979
- 유형: 정렬, 구현
'''

from functools import cmp_to_key

class Record:
    def __init__(self, id, gold, silver, bronze):
        self.id = id
        self.rnum = 0
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

# 정렬자
def compareRecord(a: Record, b: Record):
    if a.gold > b.gold:
        return -1
    elif a.gold < b.gold:
        return 1
    
    # 금메달 수가 같은 경우
    if a.silver > b.silver:
        return -1
    elif a.silver < b.silver:
        return 1
    
    # 금메달 수, 은메달 수가 같은 경우
    if a.bronze > b.bronze:
        return -1
    elif a.bronze < b.bronze:
        return 1
    
    return 0 # 같은 경우로 생각

# 금은동별 집계 테이블 초기화
[cases, targetId] = map(int, input().split())

ranking = []
idToRecord = {}

for _ in range(cases):
    [id, gold, silver, bronze] = map(int, input().split())
    record = Record(id, gold, silver, bronze)
    ranking.append(record)
    idToRecord[id] = record

# 정렬
ranking.sort(key=cmp_to_key(compareRecord))

# 집계
previousRecords = []
equalCount = 0
for record in ranking:
    if len(previousRecords) == 0:
        record.rnum = 1
        previousRecords = [record]
        continue

    previous = previousRecords[0]
    if (record.gold, record.silver, record.bronze) == (previous.gold, previous.silver, previous.bronze):
        previousRecords.append(record)
    else:
        record.rnum = previous.rnum + len(previousRecords)
        previousRecords = [record]

# 디버그
# for record in ranking:
#     print(f'id={record.id}')
#     print(f'rnum={record.rnum}')
#     print(f'gold={record.gold}')
#     print(f'silver={record.silver}')
#     print(f'bronze={record.bronze}')
#     print()

answer = idToRecord[targetId].rnum
print(answer)
