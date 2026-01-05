'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/340213
- 유형: 구현
'''

def opening(current_time, opening_start, opening_end):
    if opening_start <= current_time <= opening_end:
        current_time = opening_end
    return current_time
    

def solution(video_len, pos, op_start, op_end, commands):
    now_m, now_s = map(int, pos.split(':'))
    last_m, last_s = map(int, video_len.split(':'))
    ops_m, ops_s = map(int, op_start.split(':'))
    ope_m, ope_s = map(int, op_end.split(':'))
    
    now = 60 * now_m + now_s
    last = 60 * last_m + last_s
    ops = 60 * ops_m + ops_s
    ope = 60 * ope_m + ope_s
    
    for command in commands:
        now = opening(now, ops, ope)
        
        if command == 'prev':
            now -= 10
            
            now = opening(now, ops, ope)
            
            if now < 0:
                now = 0
            
            
        elif command == 'next':
            now += 10
            
            now = opening(now, ops, ope)
            
            if now > last:
                now = last
    
    now_m = str(now // 60)
    now_s = str(now % 60)

    if len(now_m) == 1:
        now_m = '0' + now_m
    
    if len(now_s) == 1:
        now_s = '0' + now_s
    
    return now_m + ":" + now_s