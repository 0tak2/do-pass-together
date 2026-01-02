'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120880
- 유형: 구현, 정렬
'''

def solution(numlist, n):
    answer = []
    small_group = []
    large_group = []
    
    numlist.sort()
    
    # n보다 큰지, 작은지 비교해서 저장
    for i in numlist:
        if i < n:
            small_group.append(i)
        else:
            large_group.append(i)

    # 비교
    while len(small_group) > 0 and len(large_group) > 0:
        if (n - small_group[-1]) < (large_group[0] - n):
            answer.append(small_group.pop())
        else:
            answer.append(large_group.pop(0))
    
    # 위에 while문에서 처리 안되고 남아있는 것들 처리
    if small_group:
        small_group = small_group[::-1]
        for s in small_group:
            answer.append(s)
    elif large_group:
        for l in large_group:
            answer.append(l)
    
    return answer