'''
- 플랫폼: 백준
- 문제: [어두운 굴다리](https://www.acmicpc.net/problem/17266)
- 유형: 구현

* 선형 완전 탐색으로 구현. 구현에 문제는 없는 것 같지만 3중 루프로, 시간 복잡도가 O(N^3)이 된다. 시간 초과.
'''

def solution(length, lampPoses):
    road = [False] * length

    for h in range(length):
        for p in lampPoses:
            for i in range(p-h, p+h):
                if i >= 0 and i < len(road):
                    road[i] = True
        
        allOn = True
        for isOn in road:
            if not isOn:
                allOn = False
        if allOn:
            return h
    
    return length

length = int(input())
numberOfLamps = int(input())
lampPoses = list(map(int, input().split()))

ans = solution(length, lampPoses)
print(ans)
