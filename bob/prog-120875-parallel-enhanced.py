from itertools import combinations

'''
만약 dots가 4개 이상으로 늘어난다면?
'''
def are_parallel(p1, p2, p3, p4):
    """
    두 직선 (p1-p2)와 (p3-p4)가 평행한지 확인 (교차 곱 이용)
    """
    dx1, dy1 = p2[0] - p1[0], p2[1] - p1[1]
    dx2, dy2 = p4[0] - p3[0], p4[1] - p3[1]
    
    # dy1/dx1 == dy2/dx2  =>  dy1 * dx2 == dy2 * dx1
    return dy1 * dx2 == dy2 * dx1

def solution(dots):
    # 1. N개의 점 중 4개를 선택하는 모든 조합 탐색
    for indices in combinations(range(len(dots)), 4):
        # 선택된 4개 점의 실제 좌표 가져오기
        p = [dots[i] for i in indices]
        
        # 2. 4개의 점을 두 쌍으로 나누는 3가지 케이스 확인
        # 케이스 1: (0,1) (2,3)
        if are_parallel(p[0], p[1], p[2], p[3]): return 1
        # 케이스 2: (0,2) (1,3)
        if are_parallel(p[0], p[2], p[1], p[3]): return 1
        # 케이스 3: (0,3) (1,2)
        if are_parallel(p[0], p[3], p[1], p[2]): return 1
            
    return 0
