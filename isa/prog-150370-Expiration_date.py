'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/150370
- 유형: 구현
'''

def to_days(date_str):
    y, m, d = map(int, date_str.split('.'))
    return (y * 12 * 28) + (m * 28) + d

def solution(today, terms, privacies):
    answer = []
    term = {}
    
    today_date = to_days(today)
    
    # 약관 종류 dict에 저장
    for t in terms:
        kind, exp = t.split()
        term[kind] = int(exp) * 28
        
    for idx, val in enumerate(privacies):
        date, kind = val.split()
        privacy_information_date = to_days(date)
        
        if privacy_information_date + term[kind] <= today_date:
            answer.append(idx + 1)
    
    
    return answer