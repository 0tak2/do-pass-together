'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/161990
- 유형: 구현
'''

def solution(wallpaper):
    answer = []
    files = []
    
    for id1, val1 in enumerate(wallpaper):
        for id2, val2 in enumerate(val1):
            if val2 == '#':
                files.append([id1, id2])
        
    
    lux = min([x[0] for x in files])
    luy = min([y[1] for y in files])
    rdx = max([x[0] for x in files]) + 1
    rdy = max([y[1] for y in files]) + 1
          
    if len(files) == 1:
        return [lux, luy, lux+1, luy+1]
    else:
        return [lux, luy, rdx, rdy]