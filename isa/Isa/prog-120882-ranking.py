'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120882
- 유형: 구현
'''

def solution(score):
    answer = []
    average_score = []
    
    for i in score:
        average_score.append((i[0]+i[1])/2)
        
    for id1, s1 in enumerate(average_score):
        current_rank = 1
        for id2, s2 in enumerate(average_score):
            
            if id1 == id2:
                continue
            
            if s1 < s2:
                current_rank += 1
                
        answer.append(current_rank)
    
    return answer