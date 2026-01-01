'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/10431
- 유형: 정렬, 구현
'''
def solution(heights):
    draft = []
    backCount = 0

    for cur in heights:
        if len(draft) == 0:
            draft.append(cur)
            continue
        
        inserted = False
        for cmpIndex in reversed(range(len(draft))):
            if draft[cmpIndex] > cur:
                # print(f'go back 1 step / index={cmpIndex} number={draft[cmpIndex]}')
                backCount += 1
            else:
                # print(f'{cur} inserted before {draft[cmpIndex]}')
                draft.insert(cmpIndex+1, cur)
                inserted = True
                break
        
        if not inserted:
            draft.insert(0, cur)

    return backCount

cases = int(input())
results = []
for _ in range(cases):
    heights = list(map(int, input().split()))[1:]
    results.append(solution(heights))
for idx, result in enumerate(results):
    print(f'{idx+1} {result}')
