'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120907
- 유형: 구현
'''

def solution(quiz):
    answer = []
    
    for q in quiz:
        q = q.split()
        a, op, b = q[:3]
        sol = q[-1]

        
        if op == "+":
            if int(a) + int(b) == int(sol):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(a) - int(b) == int(sol):
                answer.append("O")
            else:
                answer.append("X")
                
    return answer