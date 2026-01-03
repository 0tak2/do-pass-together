'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/12789
- 유형: 스택, 큐
'''
def solution(people):
    nextId = 1
    stash = []

    while len(people) != 0 or len(stash) != 0:
        # print(f"people: {people}")
        # print(f"stash: {stash}")
    
        if len(people) != 0 and people[0] == nextId:
            people.pop(0)
            nextId += 1
            continue
        
        if len(stash) != 0 and stash[-1] == nextId:
            stash.pop()
            nextId += 1
            continue
        
        # 이동
        if len(people) != 0:
            moving = people.pop(0)
            stash.append(moving)
        
        # 실패 조건
        if stash[-1] != nextId and len(people) == 0:
            print("Sad")
            return
    
    if people or stash:
        print("Sad")
    else:
        print("Nice")

input()
people = list(map(int, input().split()))
solution(people)
