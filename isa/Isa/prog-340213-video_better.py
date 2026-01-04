'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/340213
- 유형: 구현
'''

# 초로 변환
def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

# 분:초로 변환
def seconds_to_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02}:{seconds:02}"

# 오프닝인지 확인
def opening(current_time, opening_start, opening_end):
    if opening_start <= current_time <= opening_end:
        current_time = opening_end
    return current_time
    

def solution(video_len, pos, op_start, op_end, commands):
    video_len = time_to_seconds(video_len)
    current_pos = time_to_seconds(pos)
    op_start = time_to_seconds(op_start)
    op_end = time_to_seconds(op_end)
    
    for command in commands:
        current_pos = opening(current_pos, op_start, op_end)
        
        if command == 'prev':
            current_pos = max(0, current_pos - 10)
            
        elif command == 'next':
            current_pos = min(video_len, current_pos + 10)

        current_pos = opening(current_pos, op_start, op_end)
    
    return seconds_to_time(current_pos)